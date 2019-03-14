#  4、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
def my_space(seq):
    if ' ' in seq:
        print('序列中存在空格')
    else:
        print('序列中不存在空格')
my_space('dsf dfsfd s dsf')