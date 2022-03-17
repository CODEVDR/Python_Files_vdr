def fact_recurssion(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact_recurssion(n-1)
v=fact_recurssion(int(input("Enter Factorial: ")))
print(v)