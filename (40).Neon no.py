#for i in range(101,1000):
# s=0
# t=i
# while t>0:
#    d=t%10
#    s=s+d**3
#    t=t//10
# if s==i:
#    print(i,end=',')
#-----------------------------------------------------------
#Fibonacci Series
#0,1,2,3,4,5,8,13.....
#no=int(input('Enter the Number:'))
#a=0
#b=1
#c=0
#print(a,b,end=' ')
#c=a+b
#while c<no:
#    print(c,end=' ')
#    a=b
#    b=c
#    c=a+b
#------------------------------------------------------------
#for i in range(101,1000):
#    s=0
#    t=i
#    while t>0:
#        d=t%10
#        s+=d**3
#        t//=10
#    if s==i:
#        print(i,end=',')
#------------------------------------------------------------
#no=int(input('Enter the Number:'))
#s=0
#t=no
#while t>0:
#    d=t%10
#    s=s+d**3
#    t=t//10
#if no==s:
#    print(no,'is a armstrong number')
#else:
#    print(no,'not a armstrong number')
#-------------------------------------------------------------
no=int(input('Enter the no:'))
if no%10==0 or no%9==0:
    print(no,'is a neon number')
else:
    print(no,'is not a neon number')
