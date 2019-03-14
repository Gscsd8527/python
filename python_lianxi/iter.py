lst=list(range(1,10))
lst.__iter__()
def it(lst):
    for i in lst:
        yield i
a=it(lst)
print(a.__next__())