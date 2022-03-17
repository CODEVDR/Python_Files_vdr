#WAP TO INPUT TWO PRINT ALL THE EVEN NOS B/W THEM
a=int(input('enter the no:'))
b=int(input('enter the no:'))
if a>b:
    a,b=b,a
for i in range(a,b+1):
    if i%2==0:
        print(i,end=',')
        
    
    
