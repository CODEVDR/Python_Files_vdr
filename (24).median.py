#waP to input three nos and print the smallest no Home
#wap to input three nos and print the middle no
a=int(input("Input first number: "))
b=int(input("Input second number: "))
c=int(input("Input tird number: "))
if a>b:
    if a<c:
        median= a
    elif b>c:
        median= b
    else:
        median=c
else:
    if a>c:
        median= a
    elif b<c:
        median=b
    else:
        median= c
print("The middle number is",median)
