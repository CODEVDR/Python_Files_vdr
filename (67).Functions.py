# PROGRAM 1
# -------------------------------------
"""def add(num1,num2):
    sum=num1+num2
    return(sum)
v=add(55,66)
print(v)"""
# PROGRAM 2
# -------------------------------------
"""def greet(name="Stranger"):#name = stranger beacuse if someone haven't Entered a name it takes it as stranger Also Known as default parameter value
    print("Good Day, "+name)
greet("vdr")
greet()"""
# PROGRAM 3
# -------------------------------------
"""def fact(n):
    p=1
    for i in range(n):
        p*=(i+1)
    return(p)
print(fact(5))"""
# WAP using function to find greatest of three numbers:-
# --------------------------------------------------------------
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
# PROGRAM
# --------------------------------------------
"""def till_range(n):
    for i in range(1,n+1):
        print(i,end=" ")
v=till_range(int(input("Enter A Range: ")))
print(v)"""
# PROGRAM
# ----------------------------------------------
"""n=input("Do You Want To Break Line [Yes/No]: ")
n1=int(input("How Many Times You Want To Repeat Words: "))
def repeater(s):
    if "Yes" or "yes" == n:
        print((s+"\n")*n1)
    else:
        print(s*n1,end=" ")
s=repeater(input("Enter String: "))"""
# PROGRAM
# ---------------------------------------------
"""def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
n=table(float(input("Enter A Number For Table:")))"""
# PROGRAM
# -----------------------------------------
"""#WAP THAT REMOVES A GIVEN STRING IN A STRING:-
def remove(s,w):
    nw_str=s.replace(w,"")
    return nw_str
this="Code With Vdr    .. Ifinite"
n=remove(this,"Vdr")
print(n)"""
# PROGRAM
# -----------------------------------------
# WAP A FUNCTION THAT CALCULATE SIMPLE INTREST:-
"""def si(p,r,t):
    si=p*r*t/100
    return si
p=float(input("Enter Principle Amount: "))
r=float(input("Enter Rate: "))
t=float(input("Enter Time in Years: "))
v=si(p,r,t)
print(v)"""
# PROGRAM
# ------------------------------------------
# WAP THAT CLACULATE FACTORIAL OF A GIVEN VALUE:-
"""def fact(n):
    f=1
    if n==0:
        print("Factorial of 0 is 1")
    elif n<0:
        print("Factorial Not Possible")
    else:
        for i in range(1,n+1):
            f*=i
        print(f"Factorial of {n} is {f}")
v=fact(int(input("Enter a number: ")))"""
# PROGRAM
# -------------------------------------
# WAP A FUNCTION WHICH CHECKS IT IA A PRIME NO OR NOT:
"""def prime_no(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        print(f"{n} is a Prime Number.")
    else:
        print(f"{n} is a Not a Prinme Number.")
prime_no(int(input("Enter A Number: ")))  """
# PROGRAM
# --------------------------------------
# WAP THAT TAKES AMT IN DOLLORS AND CONVERT IT INTO RUPEE
"""def doll_to_rupee(n):
    print(n*72)
doll_to_rupee(72)#void
def doll(n):#non void
    return (n*72)
v=doll(72)
print(v)"""
# PROGRAN
# ---------------------------------------
# WAP A FUNCTION THAT CHECKS WEATER THE NUMBER IS PALINDROME OR NOT
"""def palindrome(n):
    n=str(n)
    if n==n[::-1]:
        print(f"{n} is Palindrome.")
    else:
        print(f"{n} is not Palindrome.")

palindrome(121)"""
# PROGRAM
# ---------------------------------------
# WAF TO CHECK WHETHER GIVEN NUMBER IS ARMSTRONG OR NOT.
"""def armstrong(n):
    temp=0
    for i in n:
        temp+=int(i)**3
    if n==str(temp):
        print(f"{n} is Armstrong.")
    else:
        print(f"{n} is not Armstrong.")
n=armstrong(input("Enter A Value: "))"""
# PROGRAM
# ----------------------------------------
# WAF TO CHECK NEON NO OR NOT
"""def neon(no):
   if no%10==0 or no%9==0:
       print(no,'is a neon number')
   else:
       print(no,'is not a neon number')
neon(int(input("Enter Value: ")))"""
#PROGRAM
#------------------------------
# WAF TO PRINT FIBONACCI SERIES
"""def fib(n):
    a,b=0,1
    print(a,f"\n{b}")
    for i in range(1,n):
        c=a+b
        a,b=b,c
        print(c)
fib(9)"""
# or
"""def fib(n):
    l=[0,1]
    for i in range(2,n+1):
        l.append(l[i-1]+l[i-2])
    for i in l:
        print(i)
fib(int(input("Enter A Value:")))"""
# PROGRAM
# -----------------------------------------
#============================================================================
#HOMEWORK
#--------
#WAF TO PRINT KRISHNAMURTHY NUMBER:-

"""def km(n):
    s = 0  # initializing for sum of factorial numbers
    m = int(n)  # Type casting string Value to int Value to a variable "m"
    # Passing Values
    # ----------------
    for i in n:
        # Factorial Part
        # -------------
        f = 1
        for j in range(1, int(i)+1):
            f *= int(j)
        # -------------
        s += f  # Storing Sum
    # ----------------
    # Checking Number is Krishnamurthy or not
    if s == m:
        print(f"{m} Is A Krishnamurthy Number")
    else:
        print(f"{m} Is Not A Krishnamurthy Number.")


s = input("Enter A Value: ")
km(s)"""
#--------------------------------------------------
# WAF TO CHECK NEON NO OR NOT
"""def neon(no):
   if no%10==0 or no%9==0:
       print(no,'is a neon number')
   else:
       print(no,'is not a neon number')
neon(int(input("Enter Value: ")))"""
#--------------------------------------------------
#WAF TO CHECK IT IS DUCK NUMBER OR NOT:-
"""def duck_no(n):
    l=list(n)
    if l[0]=="0":
        l.remove("0") 
        print(f"{n} is not a Duck Number.") 
    elif ("0" in l) and (l[0]!="0") and 0>int(n):
        print(f"{n} is a Duck Number.")
    else:
        print(f"{n} is not a Duck Number.")
duck_no(input("Enter A Value: "))"""
#--------------------------------------------------
#WAF TO CHECK THE NUMBER IS BUZZ NUMBER OR NOT:
"""def buzz_no(n):
    l=list(n)
    if l[-1]=="7":
        print(f"{n} is Buzz Number")
    elif int(n)%7==0:
        print(f"{n} is Buzz Number")
    else:
        print(f"{n} is Not Buzz Number")
buzz_no(input("Enter A Value: "))"""
#---------------------------------------------------
#ABOVE FUNCTION USING DIGIT EXTRACTION
#WAF TO CHECK PALINDROME OR NOT USING DIGIT EXTRACTION
"""def palindrome(n):
    m=n
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n//=10
    if rev==m:
        return(f"You Entered {m} \n{m} is A Palindrome Number.")
    else:
        return(f"You Entered {m}  \n{m} is Not A Palindrome Number.")

print(palindrome(int(input("Enter A Number: \n"))))"""
#WAF TO CHECK ARMSTRONG OR NOT USING DIGIT EXTRACTION
"""def armstrong(n):
    m=n
    cube=0
    while(n>0):
        digit=n%10
        cube+=digit**3
        n//=10
    if m==cube:
        return(f"You Entered {m} \nAnd It is An Armstrong Number.")
    else:
        return(f"You Entered {m} \nAnd It is Not An Armstrong Number.")

print(armstrong(int(input("Enter A Number: \n"))))
"""
#WAF TO PRINT AUM AND AVERAGE OF A LIST:-
"""def avg_sum (lst):
    lst1=type(lst)
    lst2=[]
    try:
        if lst1==type(lst2):
            sum=0
            avg=0
            for i in lst:
                sum+=i
                avg=sum/len(lst)
            v=sum,avg
            print(f"The Sum is = {v[0]} \nThe Average is = {v[1]}")
        else:
            print(f"The Code is not Working Because You Have To Enter List But You Entered {type(lst)}")
    except TypeError:
        print("Type Error: " + f"You Have To Enter list But You Entered {type(lst)}")
    except SyntaxError:
        print("Syntax Error : "+"unterminated string literal")
    except:
        print("Error!!!!!")

avg_sum(eval(input("Enter A List For Sum And Average: ")))"""
