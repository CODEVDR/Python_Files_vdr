a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
c=int(input('Enter a number:'))
if a>b and a<c or a>c and a<b:
    print(a,'is the middle number','^_^')
elif b>c and b<a or b>a and b<c:
    print(b,'is the middle number','^_^')
else:
    print(c,'is the middle number','^_^')
