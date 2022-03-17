print("                                  WELCOME TO WORD REPEATER")
print("Credits:-VDR")
while True:
    s=input("Enter a word that you want to repeat:")
    p=input("Do you want to enter a space (y/n):")
    d=input("Do you want to print a new line (y/n):")
    f=int(input("Enter number of time you want to repeat the entered word:"))
    if p=="y" or p=="Y":
          if  (p=="y" or p=="Y") and (d=="n" or d=="N"):
              for i in range(f+1):
                  print(s,end=" ")
          else:
              print("Please select one option!!!!")
    elif d=="y" or d=="Y":
          if  (p=="n" or p=="N") and (d=="y" or d=="Y"):
              for i in range(f+1):
                  print(s)
          else:
               print("Please select one option!!!!")
    else:        
          if s=="":
              print("Please Enter a word")
              print("Aborting!!!!")
          elif p=="":
              print("Please select option y/n")
              print("Aborting!!!!") 
          elif d=="":
              print("Please select option y/n")
              print("Aborting!!!!") 
          else:
              print("Enter a number!!!!")
              print("Aborting!!!!")
    print("\nAborting!!!!")
    br=int(input("Press 1 to continue and 2 to exit:"))
    if br==2:
        break
