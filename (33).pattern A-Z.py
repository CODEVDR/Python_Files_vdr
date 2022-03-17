s=input('Enter a character between A to Z or 1 to 9 or special characters:')
if s=='A' or s=='a':
        for i in range(1,8):
            for j in range(1,8):
                if i==1 or j==1 or i==4 or j==7:
                        print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
elif s=='B' or s=='b':
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or j==2 or (i==4 and j>=2) or j==7 or i==7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=='C' or s=='c':
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or j==1 or i==7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=='D' or s=='d':
        for i in range(1,8):
                for j in range(1,8):
                        if i==1 or i==7 or j==2 or j==7:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=='E' or s=='e':
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or j==1 or i==4 or i==7:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=='F' or s=='f':
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or j==1 or i==4 :
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=='G' or s=='g':
        for i in range(1,8):
                for j in range(1,8):
                        if i==1 or i==7 or (i==4 and (j>=4 and j<=7)) or j==1 or (j==7 and (i>=4 and i<=7)):
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()


elif s=='H' or s=='h':
    for i in range(1,8):
        for j in range(1,8):
            if j==1 or j==7 or i==4 :
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=='I' or s=='i':
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or i==7 or j==4 :
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=='J' or s=='j':
        for i in range(1,8):
                for j in range(1,8):
                        if i==1 or j==4 or (i==7 and (j>=1 and j<=4)):
                                            print("*",end=" ")
                        else:
                                print(" " ,end=" ")
                print()
      
elif s=='K' or s=='k':
        for i in range(1,8):
                for j in range(1,8):
                        if j==3 or (i-j==0 and (j>=3 and j<=7)) or (i+j==8 and (j>=3 and j<=7)):
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()

elif s=='L' or s=='l':
        for i in range(1,8):
                for j in range(1,8):
                        if i==7 or j==1:
                                print('*',end=' ')
                        else:
                             print(' ',end=' ')
                print()

elif s=='M' or s=='m':
    for i in range(7):
        for j in range(7):
            if j==0 or j==6 or ((i==j) and (j>0 and j<4)) or (i==1 and j==5) or (i==2 and j==4):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=='N' or s=='n':
        for i in range(1,8):
                for j in range(1,8):
                        if j==1 or j==7 or i-j==0:
                                print('*',end=' ')
                        else:
                             print(' ',end=' ')
                print()
elif s=='O' or s=='o':
        print('This pattern is o!!!')
        for i in range(1,8):
                for j in range(1,8):
                        if i==1  or i==7 or j==7  or j==1:
                                print('*',end=' ')
                        else:
                             print(' ',end=' ')
                print()
elif s=='P' or s=='p':
       for i in range(1,8):
               for j in range(1,8):
                       if i==1 or j==1 or i==4 or(j==7 and(i>=1 and i<=4)):
                               print("*",end=" ")
                       else:
                                print(" ",end=" ")
               print()
elif s=='Q' or s=='q':
        for i in range(1,10):
                for j in range(1,10):
                     if (i==1 and (j<=7)) or (i==7 and (j<=7)) or (j==1 and (i<=7)) or (j==7 and (i<=7)):
                             print("*",end=" ")
                     elif (i-j==0 and (i>=5 and i<=9)):
                             print("*",end=" ")
                     else:
                             print(" ",end=" ")
                print()

elif s=='R' or s=='r':
        for i in range(1,8):
                for j in range(1,8):
                        if i==1 or j==1 or i==4 or(j==7 and(i>=1 and i<=4)):
                                print("*",end=" ")
                        elif (i-j==0 and (i>=5 and i<=9)):
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
                        

elif s=='S' or s=='s':
  for i in range(1,8):
    for j in range(1,8):
        if i==1 or i==4 or i==7 or (j==1 and(i>=1 and i<=4)) or (j==7 and(i>=4 and i<=7)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
elif s=='T' or s=='t':
        for i in range(1,8):
                for j in range(1,8):
                        if i==1 or j==4:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
elif s=='U' or s=='u':
        for i in range(1,8):
                for j in range(1,8):
                        if i==7 or j==1 or j==7:
                                print('*',end=' ')
                        else:
                                print(' ',end=' ')
                print()
elif s=='V' or s=='v':
        for i in range(8):
                for j in range(10):
                        if (i-j==0 and(j>=0 and j<=4)) or (i+j==8 and (j>=4 and j<=9)):
                                   print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
                        

elif s=='W' or s=='w':
        a=0
        b=3
        for i in range(4):
                for j in range(7):
                        if j==0 or j==6 or (j==5 and i==2) or (j==4 and i==1):
                                print("*",end=" ")
                        elif i==a and j==b:
                                print("*",end=" ")
                                a+=1
                                b-=1
                        else:
                                print(" ",end=" ")
                print()
                        
elif s=='X' or s=='x':
       
    for i in range(1,8):
        for j in range(1,8):
            if i-j==0 or i+j==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=='Y' or s=='y':
        for i in range(1,8):
                for j in range(1,8):
                        if i+j==8 or (i-j==0 and (j>=1 and j<=4)):
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()

        
elif s=='Z' or s=='z':
           
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or i==7 or i+j==8:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
elif s=="1":
        for i in range(1,12):
                for j in range(1,12):
                        if (i+j==8 and (i>=1 and i<=4) )or j==7 or (i==11 and j>=3):
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="2":
        for i in range(1,8):
                for j in range(1,8):
                        if i==1 or i==4 or i==7 or j==1 and i>=4 or j==7 and i<=4:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="3":
        for i in range(1,8):
                for j in range(1,8):
                        if i==1 or i==4 or i==7 or j==1:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="4":
        for i in range(1,8):
                for j in range(1,8):
                        if i==4 or j==1 and i<=4 or j==7:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="5":
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or i==4 or i==7 or (j==1 and i>=1 and i<=4) or (j==7 and i>=4 and i<=7):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
elif s=="6":
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or i==4 or i==7 or j==1 or (j==7 and i>=4 and i<=7):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
elif s=="7":
    for i in range(1,8):
        for j in range(1,8):
            if i==1 or (i==4 and j>=2 and j<=6) or i+j==8:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
elif s=="8":
    for i in range(1,8):
        for j in range(1,8):
            if (i==1 and j>=2 and j<=6) or (j==1 and i>=2 and i<=6) or (i==7 and j>=2 and j<=6) or (j==7 and i>=2 and i<=6) or i==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
elif s=="9":
    for i in range(1,8):
        for j in range(1,8):
            if (i==1 and j>=2 and j<=6) or (j==7 and i>=2 and i<=6) or (i==7 and j>=2 and j<=6) or ((j==1 and i>=2 and i<=3)) or(i==4 and j>=2 and j<=6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
##SPECIAL CHARACTERS
###OPERATORS
elif s=="*":
        for i in range(1,8):
                for j in range(1,8):
                        if i==4 or j==4 or i+j==8 or  i-j==0:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="+":
        for i in range(1,8):
                for j in range(1,8):
                        if i==4 or j==4:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="-":
        for i in range(1,8):
                for j in range(1,8):
                        if i==4:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="/":
        for i in range(1,8):
                for j in range(1,8):
                        if i+j==8 and j>=2:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
###CHARACTERS
elif s=="%":
        for i in range(1,8):
                for j in range(1,8):
                        if i+j==8 or i==1 and j<=2 or i==2 and j<=2 or i==6 and j>=6 or i==7 and j>=6:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="?":
        for i in range(1,8):
                for j in range(1,8):
                        if i==1 and (j>=2 and j<=6)  or i==5 and j>=2 and j<=6 or j==7 and i<=4 and i>=2 or j==2 and i>=5 or j==1 and i<=2 and i>=2:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="!":#PENDING
        for i in range(1,8):
                for j in range(1,8):
                        if j==4 and i!=6:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()     
elif s=="@":
        for i in range(1,10):
                for j in  range(1,10):
                        if i==1 or j==1 or i==9 and j<=6 or j==9:
                                print("*",end=" ")
                        elif i==3 and j>=3 and j<=7:
                                print("*",end=" ")
                        elif j==3 and i>=3 and i<=7:
                                print("*",end=" ")
                        elif j==7 and i>=3:
                                print("*",end=" ")
                        elif i==7 and j>=3 and j<=7:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="#":
        for i in range(1,8):
                for j in range(1,8):
                        if i==2 or i==6 or j==2 or j==6:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print() 
elif s=="$":
        for i in range(1,8):
                for j in range(1,8):
                        if i==2 and j>=2 or i==6 and j<=6 or j==2 and i>=2 and i<=4 or j==6 and i>=4 and i<=6 or j==4 or i==4 and j>=2 and j<=6:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()  
elif s=="^":
        for i in range(1,8):
                for j in range(1,8):
                        if i-j==0 and j>=4 or (i+j==8 and (j>=1 and j<=4)):
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s=="(":
        for i in range(1,8):
                for j in range(1,5):
                        if i==1 and j>=2 or j==1 and i>=2 and i<=6 or i==7 and j>=2:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()
elif s==")":
        for i in range(1,8):
                for j in range(1,5):
                        if i==1 and j<=3 or j==4 and i>=2 and i<=6 or i==7 and j<=3:
                                print("*",end=" ")
                        else:
                                print(" ",end=" ")
                print()

else:
        print('Enter a character between A to Z !!!!')
        print('Aborting!!!!')
print("You entered",s,"And its pattern printed above !!!!")
#FINISHED
