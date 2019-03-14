import pyspark
from pyspark import SparkContext as sc
from pyspark import SparkConf
import os
os.environ['JAVA_HOME'] = 'D:\software\jdk1.8'
conf = SparkConf().setAppName('test').setMaster('local[*]')
sc = sc.getOrCreate(conf)
print(sc)
nums = sc.parallelize([1, 2, 3, 4])
# nums.reduce(lambda x,y: x+y)
print(nums)
print(nums.collect())
print(type(nums))
