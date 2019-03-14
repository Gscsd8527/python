current_users=["Adminstrators","username","admin","gscsd","USER"]
new_users=["Admins","username","admin","gscsd","user"]

for new_user in new_users:
    if (new_user in current_users) or (new_user.upper() in current_users):
        print new_user
        print("username yijing cuizai \n")
    else:
        print("username weishiyong \n")