#     1
#    121
#   12321
#  1234321
# 123454321
#another method
#n=int(input('Enter the no of rows'))
#n+=1
#for i in range(1,n):
#for i in range(1,10):
#    for j in range(1,10-i):
#        print(' ',end=' ');
#    for k in range(1,i+1):
#            print(k,end=' ');
#    for l in range(i-1,0,-1):
#        print(l,end=' ');
#    print();
#------------------------------------------
for i in range(10,0,-1):
    for j in range(1,10-i):
        print(' ',end=' ');
    for k in range(1,i+1):
            print(k,end=' ');
    for l in range(i-1,0,-1):
        print(l,end=' ');
    print();
