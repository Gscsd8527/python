user={
  "users1":{
      "uesr1":"tan",
      "user2":"zhe",
      "user3":"hua",
     },
  "users2":{
      "uesr4":"tan1",
      "user5":"zhe1",
      "user6":"hua1",
     },
}
for i,j in user.items():
    print ("username:",i)
    # print("key:",j['user1'])
    # print("key:",j["user2"])
    # print("key:",j["user3"])
    list=j["user1"]+" "+j["user2"]
    list1=j["user3"]
    print("\t xingming :",list)
    print("\t xingming :",list1)