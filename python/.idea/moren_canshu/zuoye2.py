moshushi=["admin","user","Administrators"]
lst=[]
def show_magicians(list):
   while list:
      l=list.pop()
      lst.append(l)
   print "list: ",list
tan=show_magicians(moshushi[:])
print(moshushi)