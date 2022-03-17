#wap toinput a no and print factros the given no
no=int(input('Enter the no:'))
for i in range(1,no+1):
       if no%i==0:
           print(i,end=',')
