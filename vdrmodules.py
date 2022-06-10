"""WELCOME TO MYMODULES 
© vdrmodules
Credits:-Master VDurgeshwar Rao"""


# Addition Of n Numbers Modules:
from unicodedata import name


def add(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
# Substraction of n Number Module:


def sub(*numbers):
    sum = 0
    for num in numbers:
        sum -= num
    return sum
# Multiplication of n numbers Module:


def mul(*numbers):
    sum = 1
    for num in numbers:
        sum *= num
    return sum
# Division Of n Numbers Module:


def div(*numbers):
    try:
        sum = 0
        for num in numbers:
            sum /= num
        return sum
    except ZeroDivisionError:
        return (f"Cannot divide by 0 ")
# Floor Division of n Numbers in Modules:


def fdiv(*numbers):
    try:
        sum = 0
        for num in numbers:
            sum //= num
        return sum
    except ZeroDivisionError:
        return (f"Cannot divide by 0 ")
# Table of entered number upto entered number:


def table(number, r):
    for i in range(1, r+1):
        print(f"{number} x {i} = {number*i}")
# Armstrong Number Check


def armstrongc(n):
    n = str(n)
    s = 0
    for i in n:
        s += int(i)**3
    if s == int(n):
        return(f"{n} is Armstrong Number")
    else:
        return(f"{n} is Not Armstrong Number")
# Palindrome Number Check:


def palindromec(n):
    s = str(n).lower()
    if s.isdigit():
        if s == s[::-1]:
            return(f"{n} is a Palindromic Number")
        else:
            return(f"{n} is Not A Palindromic Number")
    else:
        if s == s[::-1]:
            return(f"{n} is A Palindromic String")
        else:
            return(f"{n} is Not A Palindromic String")
# Factorial Of a Entered Number


def factorial(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return (s)
# Prime Number Check


def primec(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return (f"{n} is a Prime Number.")
    else:
        return (f"{n} is a Not a Prinme Number.")
# Dollar To Rupee


def doll_to_rupee(n, c):
    return(n*c)
# Neon Number Check


def neonc(no):
    if no % 10 == 0 or no % 9 == 0:
        return(no, 'is a neon number')
    else:
        return(no, 'is not a neon number')
# Fibonacci Series:


def fib(n):
    l = [0, 1]
    for i in range(2, n+1):
        l.append(l[i-1]+l[i-2])
    for i in l:
        return(i)
# KrishnaMurthy Number Check


def krishnamurthyc(n):
    s = 0
    m = int(n)
    for i in n:
        for j in range(1, int(i)+1):
            f *= int(j)
        s += f
    if s == m:
        return(f"{m} Is A Krishnamurthy Number")
    else:
        return(f"{m} Is Not A Krishnamurthy Number.")
# Duck Number Check


def ducknoc(n):
    l = list(n)
    if l[0] == "0":
        l.remove("0")
        print(f"{n} is not a Duck Number.")
    elif ("0" in l) and (l[0] != "0") and 0 > int(n):
        return(f"{n} is a Duck Number.")
    else:
        return(f"{n} is not a Duck Number.")
# Buzz Number Check


def buzznoc(n):
    l = list(n)
    if l[-1] == "7":
        return(f"{n} is Buzz Number")
    elif int(n) % 7 == 0:
        return(f"{n} is Buzz Number")
    else:
        return(f"{n} is Not Buzz Number")
# open file and print its data


def openf(filename):
    try:
        # "Python/" because it is in my directory
        with open(f"Python/{filename}.txt", "r") as f:
            content = f.read()
            return(content)
    except:
        return("Error \nYour File Should Be In Same Directory..")
# write a file


def writef(filename, extension, write):
    try:
        with open(f"Python/{filename}.{extension}", "w") as f:
            content = f.write(f"{write}")
    except:
        return ("Error \nYour File Should Be In Same Directory..")
# append a file


def appendf(filename, extension, append):
    try:
        with open(f"Python/{filename}.{extension}", "w") as f:
            content = f.write(f"\n{append}")
    except:
        return ("Error \nYour File Should Be In Same Directory..")


#JUST FOR FUN RELAXATION OF MIND
def type_cast(s,t):
    try:
        n=t.lower()
        if n=="int" and s.isdigit():
            v=int(s)
            return(v)
        elif n=="str" and s.isalpha():
            v=str(s)
            return(v)
        elif n=="alpha" and s.isalnum():
            return (f"{s} is Alphanumeric")
        elif n=="bool":
            v=bool(s)
            return(v)
        else:
            return(None)
    except TypeError:
        return "Please Enter A Valid Syntax!!!!"
#if __name__=="__main__":
    #s=""
    #s=input("Enter : ")
    #t=input("Enter Type : ")
    #print(type_cast(s,t))
def word_repeater(s="",n=0):
    v=s*n
    return v
#if __name__=="__main__":
    #s=input("Enter A String : ")
    #n=int(input("Enter Number Of Times You Want To Repeat : "))
    #print(word_repeater(s,n))
