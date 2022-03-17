#wap to input a no and check weather it is a prime no
no=int(input('Enter a no:'))
ctr=0
for i in range(1,no+1):
       if no%i==0:
           ctr=ctr+1
if ctr==2:
#ctr!=2:
       #print('composite number')
    print('Prime number')
else:
    print('not Prime')
