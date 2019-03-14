user1=["admin","user","Adminstrators"]
user2=[]
def get_user(user):
    for toup in user:
        user2.append(toup)
        print(toup+"\n")
    return user2
tan=get_user(user1)
print(tan)

