no=int(input("Enter a number:"))
s=0
t=no
while t>0:
   d=t%10
   s=s+d**3
   t=t//10
if no==s:
   print(no,"is an Armstrong number")
else:
   print(no,"is not an Armstrong number")
