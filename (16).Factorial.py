print("Press1.Continue")
print("Press 2.Exit")
while True:
     n=int(input("Enter a number for factorial you want:"))
     c=1
     for i in range(1,n+1):
         c*=i
     print("Factorial of",n,"is",c)
     c=int(input("Enter 1 for continue or 2 for exit:"))
     if c==2:
         break
    
