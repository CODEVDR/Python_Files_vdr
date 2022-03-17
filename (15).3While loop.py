#wap to print even between two nos.
a=int(input("Enter the Value:"))
b=int(input("Enter the Value:"))
if a>b:
    a,b=b,a
while a<=b:
    if a%2==0:
        print(a,end=",")
    a=a+1
    
