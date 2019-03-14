import queue

# 队列长度
q = queue.Queue(3)
q.put(6)
print('队列的大小{}'.format(q.qsize()))
q.put(3)
print('队列的大小{}'.format(q.qsize()))
# 队列是否是满的
print('Is queue full?',q.full())
# 队列是否为空
print('Is queue empty',q.empty())
q.put(7)
print('Is queue full?',q.full())
# 得到第一个队列数据
item = q.get()
print(item)
# 得到第二个队列数据
ite = q.get()
print(ite)
a =q.get()
print(q.empty())