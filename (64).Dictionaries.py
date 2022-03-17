#WAP in python to input total number of sections and strength in class and display all
#information on the output screen.
'''n=int(input("Enter no of Sections:"))
d={}
s=input("Enter Your Class:")
for i in range(n):
    a=input("Enter Section:")
    b=int(input("Enter Strength:"))
    d[a]=[b]
print("Class","\t","Strength","\t","Strength:")
for i in d:
    print(s,"\t",i,"\t",d[i])'''
#WAP in python to store Employee details like EmpId, Name, Salary, Age in a dictionary and
#display information on the basis of EmpId. 
'''n=int(input("Enter no of Employee:"))
d={}
for i in range(n):
    a=int(input("Enter Employee ID:"))
    b=input("Enter Employee Name:")
    c=float(input("Enter Salary:"))
    A=int(input("Enter Employee's age:"))
    d[a]=[b,c,A]
print("ID","\t","Name","\t","Salary","\t","Age")
for i in d:
    print(a,"\t",b,"\t",c,"\t",A)'''
#WAP in python to input names of n employees and their salary details like basic salary,
#house rent, and conveyance allowance. Calculate total salary of each employee and
#display.
"""n=int(input("Enter no of Employee:"))
d={}
for i in range(1,n+1):
    a=float(input("Enter Basic Salary:"))
    b=float(input("Enter House Rent Allowance:"))
    c=float(input("Enter Conveyance Allowance:"))
    s=a+b+c
    d[i]=[b,c,a]
print(d)
print("Basic Salary","\t","House Rent Allowance","\t","Conveyance Allowance","\t")
for i in d:
    print(a,"\t\t",b,"\t\t",c,"=","\t\t",s,"[Total Salary]")"""
#WAP in python to input names of ‘n’ states and their capital, store it in dictionary and
#display in tabular form. Also search and display for a particular country.
"""n=int(input("Enter the number of countries to be be entered: "))
d={}
for i in range(n):
   x=input("Enter the country name: ")
   y=input("Enter the capital: ")
   z=input("Enter the currency: ")
   d[x] = y, z
print(d)
print("Country", "\t\t", "Capital", "\t\t\t", "Currency")
for i in d:
    print(i,"\t\t\t", d[i][0],"\t\t\t", d[i][1])
S=input("Enter the country:")
if S in d:
    print(S,":",d[S])
else:
    print("No such country in the given dictionary.")"""
#WAP in python to store names and their percentage in dictionary, delete a particular student name from the dictionary. Also display dictionary after deletion.
'''n=int(input("Enter Number of Students:"))
d={}
for i in range(n):
   s=input("Enter student Name:")
   x=float(input("Enter PHYSICS marks:"))
   y=float(input("Enter Chemistry marks:"))
   z=float(input("Enter MATHS marks:"))
   d[s]=x, y, z
print(d)
name=input("Enter Student Name:")
if name in d.keys():
    print("Avg student marks:",d.values())
else:
    print("Enter a Valid Name:")'''
"""rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")+
        k += 1
   
    k = 0
    print()"""
"""class vdr:
        print("hello world")
    """
"""from locale import DAY_2


my_dict={}
n=int(input("How many Elements do you Want to Enter: "))
for i in range(1,n+1):
    a=input("Enter Your Name: ")
    b=float(input("Enter Your Age: "))
    c=float(input("Enter Salary: "))
    d=input("Enter Your Designation: ")
    my_dict[a]=b,c,d
print("Your Dictionary: \n",my_dict)"""
"""t=()
t=eval(input("Enter a Tuple:"))
l=list(t)
l1=l.remove(2)
t1=tuple(l)
print(t1)"""
"""l=[]
l1=[]
l2=[]
l=eval(input("Enter a List: "))
for i in l:
    if i==0:
        l2.append(i)
    else:
        l1.append(i)
print(l1+l2)"""
"""l=[]
l=eval(input("Enter a List:"))
u=list(set(l))
d=[]
for i in l:
  c=l.count(i)
  if i in l:
    v=l.count(i)
    print(i,"freq",v)
for i in l:
    if i not in u:
        d.append(i)


print("Original",l)
print("unique",u)
print("duplicate",d)"""
"""l=["22-02-2022"]
l1=l[: : -1]
if l==l1:
    print("Yahoo It's a Palindromic Date",l1)"""
"""l=[]
a=int(input("How Many Rows you Want: \n"))
b=int(input("How many Colums Do You Want: \n"))
for i in range((a)):
    r=[]
    for j in range(b):
        c=[]
        n=eval(input("Enter Any DataType[BUT,For String You have to write inside ("''"),For LIST You Have To Use [],For Tuple You Have To Use ():\n"))
        r.append(n)
        print("Element of "+str(int(i+1))+" of "+str(int(j+1))+" is:")
    l.append(r)
print("The List Created Is \n",l)"""
"""d={}
while True:
    p=input("Enter Product: ")
    v=float(input("Enter Price: "))
    s=input("Do You Want To Continue[Y/N]: ")
    d[p]=[v]
    if s=="N" or s=="n":
        break
print(d)"""
"""l1=[2,3,4,5,6,7,8,8,9,9,0,0,66,78,99]
l2=[]
l3=[]
for i in range(len(l1)):
    if l1[i]%2==0:
        l2.append(l1[i])
    else:
        l3.append(l1[i])
print("Eve Nos:",l2)
print("Odd Nos:",l3)"""
import random
i=0
s=int(input("Enter a Number: "))
s=str(s)
while True:
    v=(random.randint(000000,999999))
    print(str(v))
    i+=1
    if str(v)==s:
        break
print("You Entered:",s,"Total Number Of counts is",i)