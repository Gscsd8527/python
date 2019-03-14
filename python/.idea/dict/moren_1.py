def get_formatted_name(first_name,tow_name,three_name=""):
    if three_name:
        name=first_name+" "+tow_name+" "+three_name;
    else:
        name= first_name+" "+tow_name;
    return name.title()
tan=get_formatted_name("tan","zhen","hua")
print(tan+"\n")
ta=get_formatted_name("huang","gui")
print(ta+"\n")
