# RECURSION FOR FINDING FACTORIAL:-
"""def fact(n):
    try:
        if n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
    except:
        return ("Please Enter A Number Less Than 1000")
v=fact(int(input("Enter A Number less than 1000:")))
print(v)"""
# Recurssion For Prime Number Or Not:-
"""count = 0
def prime(num,n) :
    if num==0:
        return "0 is Neither Prime Nor Composite"
    elif n == num :
        return num
    else :
        global count
        if num % n == 0 :
            count  += 1
        prime(num , n+1)

num = int(input("Enter a number : "))
prime( num , 0 )

if count > 0 :
    print(num, "is not prime number")
else :
    print(num , "is Prime number ")"""
"""def inp(n):
    n1=len(n)
    s=input("Enter Product Name : ")
    if s in n:
        if n1==1 or n1==0:
                return 1
        else:
            v=n1*inp(n1-1)
            print(f"The Product is {n[v]}")
    else:
        print(f"Value Not Found...")
d={}
while True:
    n=input("Enter Product Name : ")
    n1=input("Enter Price : ")
    d[n]=n1
    s=input("Do You Want To Enter More Data[Y/N] : ")    
    if s in "Nn":
        break
inp(d)
#print(d)
"""
# WAF IN RECURSION TO CALCULATE POWER OF A GIVEN NUMBER:-
"""def power(n,p=0):
    if p==0:
        return 1
    else:
        return n*power(n,p-1)
n=int(input("Enter A Number : "))
p=int(input("Enter A Power : "))
print(power(n,p))"""

# WAF IN RECURSION TO PRINT SUM OF ENTERED NUMBER STARTS FROM 0 TO ENTERED NUMBER:-
"""def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(10))"""
# WAF IN RECURSION TO PRINT DIVISION OF ENTERED NUMBER STARTS FROM 0 TO ENTERED NUMBER:-
"""def div(n):
    if n==1:
        return 1
    else:
        return n/div(n-1)
print(div(10))"""
# WAF IN RECURSION TO FIND POWER OF A NUMBER:
"""def pow(n=0, p=0):
    if p == 0:
        return 1
    else:
        return n*pow(n, p-1)
n = int(input("Enter A Number : "))
p = int(input("Enter A Power  : "))
# __main__
print(f"{n} power {p} is  {pow(n,p)}")"""
#WAP IN PYTHON TO FRINT FIBONACCI SERIES USING RECURSION:-
"""def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
n=int(input("Enter A Number : "))
for i in range(n):
    if n<=0:
        print("Please Enter A Positive Number")
    else:
        print(fibo(i))"""


def rv(sg,n):
    if n>0:
        print(sg[n],end="")
        rv(sg,n-1)
    elif n==0:
        print(sg[0])
#s=input("Enter A String : ")
#v=rv(s,len(s)-1)
#GCD
def gcd(p,q):
    if q==0:
        return p
    else:
        return gcd(q,p%q)
#Power
def pow(b,e):
    if e==0:
        return 1
    else:
        return b*pow(b,e-1)

def rev(sg,m):
    if m>0:
        print(sg[m],end="")
        rev(sg,m-1)
    elif m==0:
        print(sg[0])
rev("NEWS",len("NEWS")-1)