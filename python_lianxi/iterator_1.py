# lst=[1,2,3,4,5,6,7,8,9]
def my_iter(my_str):
    for i in range(my_str):
        yield i**2
for itrm in my_iter(5):
    print(itrm)


