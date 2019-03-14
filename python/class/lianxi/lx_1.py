class tanzhenhua:
    # 初始化方法，self一定要写，这是表示指向当前对象 不需要调用
    def __init__(self,new_name,new_sex):
        self.name=new_name
        self.sex=new_sex
    def sum(self):
        print('运筹于帷幄之中，决胜于千里之外')
    def pt(self):
        print('您好，{}在睡觉,{}'.format(self.name,self.sex))
tan=tanzhenhua('tanzhenhua','21')
tan.sum()
tan.pt()
