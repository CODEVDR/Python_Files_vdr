#PROGRAM 1
#-------------------------------------
"""def add(num1,num2):
    sum=num1+num2
    return(sum)
v=add(55,66)
print(v)"""
#PROGRAM 2
#-------------------------------------
"""def greet(name="Stranger"):#name = stranger beacuse if someone haven't Entered a name it takes it as stranger Also Known as default parameter value
    print("Good Day, "+name)
greet("vdr")
greet()"""
#PROGRAM 3
#-------------------------------------
"""def fact(n):
    p=1
    for i in range(n):
        p*=(i+1)
    return(p)
print(fact(5))"""
#WAP using function to find greatest of three numbers:-
#--------------------------------------------------------------
"""def greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else :
          if b>c:
              return b
          else:
              return c
m=greatest(10,140,1000)
print("The Maximum is: "+str(m))"""
#PROGRAM
#--------------------------------------------
"""def till_range(n):
    for i in range(1,n+1):
        print(i,end=" ")
v=till_range(int(input("Enter A Range: ")))
print(v)"""
#PROGRAM
#----------------------------------------------
"""n=input("Do You Want To Break Line [Yes/No]: ")
n1=int(input("How Many Times You Want To Repeat Words: "))
def repeater(s):
    if "Yes" or "yes" == n:
        print((s+"\n")*n1)
    else:
        print(s*n1,end=" ")
s=repeater(input("Enter String: "))"""
#PROGRAM
#---------------------------------------------
"""def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
n=table(float(input("Enter A Number For Table:")))"""
#PROGRAM
#-----------------------------------------
#WAP THAT REMOVES A GIVEN STRING IN A STRING:-
def remove(s,w):
    nw_str=s.replace(w,"")
    return nw_str
this="Code With Vdr    .. Ifinite"
n=remove(this,"Vdr")
print(n)