'''l = eval(input("Enter the list: "))
dedup = []
dup = []
for i in l:
    if i in dedup:
        dup.append(i)
    else:
        dedup.append(i)

l = dedup + dup

print("Modified List:")
print(l)'''
"""n=8
i=1
while i<=n:
    j=1
    while j<=i:
        if i==1 or j==1 or j==7 or i==4:
            print("*",end=" ")
            j+=1
        else:
            print(" ",end=" ")
            j+=1
    print()
    i+=1"""
"""l=[]
l=eval(input("Enter a List:"))
v=int(input("Enter a numbr that you want to find:"))
if v in l:
    print(v,"Found at Position",l.index(v)+1)
else:
    print("Element Not Found:")
 """
d={1:11,2:22,3:33}
s=input("Enter pw:")
u=input("Enter ID")
u=int(u)
s=int(s)
if d[u]==s:
    print("Yahoo")
else:
    print("u=",d[u],"p=",s)