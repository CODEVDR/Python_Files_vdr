#1
#1 2
#1 2 3 4
#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1
"""for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()"""
#---------------------------------------------
row=6
for r in range(1,6):
    no=1
    for j in range(row,0,-1):
        if j>r:
            print(" ", end=' ')
        else:
            print(no,end=' ')
            no+=1
    print()
print('''          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 ''')

        
