import sys
import time
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def writeResultToFile(rdd):
    with open('dswordcount/{0}'.format(time.time()),'wb+') as f:
        for i in rdd.collect():
            f.write(str(i).encode())
            f.write('\n'.encode())
# 当前模块以main方式导入就执行，否则不执行
if __name__=='__main__':
    #判断使用时控制台是否传入三个参数，如果不是接结束程序
    if len(sys.argv) != 3:
        print("Usage: direct_kafka_wordcount.py <broker_list> <topic>", file=sys.stderr)
        sys.exit(-1)
    #是的话从第二个参数分别获取 2 3 赋值给brokers和topic
    #<broker_list> 会赋值给brokers  <topic>则会给topic
    brokers, topic = sys.argv[1:]
    #自定义SparkConf
    conf = SparkConf()
    #创建SparkContext上下文，建立driver和worker的会话
    sc = SparkContext(master='local[4]',appName='my streaming word count',conf=conf)
    #创建sparkStreaming
    ssc = StreamingContext(sc,5)
    #使用KafkaUtils的静态方法创建kafka直连流DStream
    kk = KafkaUtils.createDirectStream(ssc,[topic],{'metadata.broker.list':brokers})
    #kk里面的元素是一个Tuple，这个Tuple有两个数据，（key,value），value是真实的数据，而key是偏移量
    lines = kk.map(lambda  x:x[1])
    words = lines.flatMap(lambda x:x.split(' '))
    pairs = words.map(lambda x:(x,1))
    wordcounts = pairs.reduceByKey(lambda x,y:x+y)
    #上面的都叫转换transformation，下边是行为action
    wordcounts.foreachRDD(writeResultToFile)
    #启动上面的流，并保持终端为等待不退出
    ssc.start()
    ssc.awaitTermination()

