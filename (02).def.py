s=input("Are you a male or female.[M/F]:")
def greet(n):
    if s=="m" or s=="M":
        return("How are you Sir "+n+"?")
    else:
        return("How are you Mam "+n+"?")    
n=input("Enter your Name:")
p=greet(n)
print(p)