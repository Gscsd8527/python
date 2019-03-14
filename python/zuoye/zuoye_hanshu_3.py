# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def my_seq(myseq):
    if len(myseq)>5:
        print('序列长度大于5')
    else:
        print('序列长度小于或等于5')
# seq=input('请输入要计算的字符串')
my_seq([1,2,3,4,5,6])