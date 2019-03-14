list=['tanzhenhua','tanyongfei','tanyongjun']
list_mz=[]
def make_great(list_Name):
    while list_Name:
        name=list_Name.pop()
        name="the Great"+' '+name
        list_mz.append(name)
        print(name)
    list_Name=list_mz[:]
    return  list_Name

def show_magicians(list_name):
    print("list:", list_name)

tan=make_great(list)
print (tan)
show_magicians(list)
print (list)