#wap to print all the prime numbers between 2 to 100
#for i in range(2,101):
#    ctr=0
#    for j in range(1,(i+1)):
#        if i%j==0:
#            ctr=ctr+1
#    if ctr==2:
#        print(i,end=',')
#-------------------------------------------------------
#wap to print all the pallondromic nos between 11 to 100
for i in range(10,100):
    a=i
    rev=0
    while a>0:
        d=a%10
        rev=(rev*10)+d
        a=a//10
    if i==rev:
        print(i,end=',')
#---------------------------------------------------------

