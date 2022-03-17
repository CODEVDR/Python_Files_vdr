#1.wap print fibonacci Series
#0,1,2,3,4,5,6,7,8,13.........n
#a=0
#b=1
#n=int(input('Enter the Range:'))
#print(a,end=',')
#print(b,end=',')
#c=a+b
#while(c<=n):
#    print(c,end=',')
#    a=b
#    b=c
#    c=a+b
#------------------------------------------------------
#2.wap print the sum of geometric series given below
#a+ar+ar²+ar³+ar^n
#a=int(input('Enter a Value:'))
#r=int(input('Enter r Value:'))
#n=int(input('Enter max Value:'))
#print('Series:--')
#sum=0
#for i in range(0,n+1):
#    t=a*(r**i)
#    sum=sum+t
#print('Sum of Series=',sum)
#----------------------------------------------------------
#3.wap to print following series
#1+1/2++1/3+................,1/n
#n=int(input('Enter a number:'))
#sum=0
#for i in range(1,n+1):
#    sum=sum+(1/i)
#print("Sum of series is:",(sum))#round(sum,2)
#------------------------------------------------------------
#4.wap to print following series
#1^2+2^2+3^2+..................+n^2
#n=int(input('Enter a number'))
#sum=0
#for i in range(1,n+1):
#    sum=sum+(i**2)
##    print(i,end=',')
#print(sum)
#-------------------------------------------------------------
#5.wap to print following series
#1^1+2^2+3^3+..................+n^n
#n=int(input('Enter a number'))
#sum=0
#for i in range(1,n+1):
#    sum=sum+(i**i)
##    print(i,end=',')
#print(sum)
#---------------------------------------------------------------
#n=int(input('Enter a number'))
#sum=0
#for i in range(1,n+1):
#    s=0
#    for j in range(1,i+1):
#        s=s+j
#    sum=sum+s
##    print(i,end=',')
#print(sum)
#----------------------------------------------------------------
#7.wap to print following series
#1+2/2!+3/3!+4/4!+......+n/n!
#5!=1x2x3x4x5=120
#n=int(input('Enter a number'))
#sum=0
#for i in range(1,n+1):
#    fact=1
#    for j in range(1,i+1):
#        fact*=j
#    print(fact)
#    sum+=(i/fact)
#print(round(sum,2))
#-------------------------------------------------------------------
inc = 1
for i in range(0, 5):
    for j in range(0, inc):
        
        
        ch = chr(value)
        value = value + 1
        inc = inc + 2
        print(ch, end=" ")
    print()
