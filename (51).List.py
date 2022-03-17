s=input("Enter a string:")
l=[]
for i in s:
    if s not in l:
        l.append(i)
for a in l:
    print(a,"-",s.count(a))
