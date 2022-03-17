#for i in range(6):
#    a=i
#        print(a,end=' ')  
#        a+=1  
#    print("")
#--------------------------------------------------------
#for i in range(0,5):  
#  for j in range(0,i+1):  
#        print("*",end=' ')  
#  print()  
#for i in range(5,0,-1):  
#    for j in range(0,i-1):  
#        print("*",end=' ')  
#    print()  
#----------------------------------------------------------
#for i in range(1,10):
#    if i<6:
#        for j in range(1,i+1):
#            print('*',end='')
#    else:
#        for k in range(i,10):
#            print('*',end='')
#    print()
#----------------------------------------------------------
print('''* * * * * *          *****           *****
 * * * * *           *    *          *    *
  * * * *            *    *          *****
   * * *             *    *          * *
    * *              *    *          *   * 
     *               *****           *     *''')
no=int(input('Enter the range:'))
for i in range(2,no+1,no%2):
    print(i,end=',')
