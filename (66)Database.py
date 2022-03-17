user_id_password={}
while True:
    user=input("Enter User ID: ")
    password=input("Enter Password: ")
    s=input("Do You Want To Continue[Y/N]: ")
    user_id_password[user]=password
    if s=="N" or s=="n":
        break
    elif s=="y" or s=="Y":
        True
    else:
        print("Invalid Syntax!! .Please Enter [Y or N]")
        continue
print("Database Created.....")
print("User Id","\t","Password")
for i in user_id_password:
    print(i,"\t\t",user_id_password[i])

print("\n\n <<<<Welcome to VDR's Database>>>>")
print("Remember Your Id and Password!!!!")
for i in range(len(user_id_password)):
      user_id1=input("Enter Your user id: ")
      if user_id1 in user_id_password.keys():
          print("User Id Found!!!!")
          password1=input("Enter Your Password: ")
          for i in range(1,6):
            if user_id_password[user_id1]==password1:
                print("Login Sucessful!!!!")
                break
            else:
                print("Incorrect Password!!!!")
                print("You Have",5-i,"Attempts.....")
      else:
          print("Incorrect Id!!!!") 
          print("You Have",5-i,"Attempts.....")