#W.A.P to input two nos and print difference of both no difference must be a +ve no
a=int(input('Enter a no:'))
b=int(input('Enter a no:'))
if a>b:
    print('ans=',a-b)
else:
    print('ans=',b-a)
#==============================================================
a=int(input('Enter a no:'))
b=int(input('Enter a no:'))
if a>b:
    a,b=b,a
print('ans=',a-b)
