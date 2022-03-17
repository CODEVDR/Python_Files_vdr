#           # 
  #       #   
    #   #     
      #       
    #   #     
  #       #   
#           # 
#for i in range(1,8):
#    for j in range(1,8):
#        if i+j==8 or i-j==0:
#            print('#',end=' ')
#        else:
#            print(' ',end=' ')
#    print()
#===============================================
#1 
#1 2 
#1   3 
#1     4 
#1 2 3 4 5 
#for i in range(1,6):
#    for j in range(1,i+1):
#        if i==3 and j==2:
#            print(' ',end=' ')
#        elif i==4 and j==2:
#            print(' ',end=' ')
#        elif i==4 and j==3:
#            print(' ',end=' ')
#        else:
#            print(j,end=' ')
#    print()
#================================================
#         1 
#       2 1 2 
#     3 2 1 2 3 
#   4 3 2 1 2 3 4 
# 5 4 3 2 1 2 3 4 5 
#n=5
#s=n*2-1
#for i in range(1,n+1):
#    for j in range(0,s):
#        print(end=' ')
#    for k in range(i,0,-1):
#        print(k,end=' ')
#    for l in range(2,i+1):
#        print(l,end=' ')
#    s-=2
#    print()
#==================================================
#          1 
#        1 2 
#      1 2 3 
#    1 2 3 4 
#  1 2 3 4 5
#for i in range(1,6):
#    for j in range(1,(6-i)+1):
#        print(' ',end=' ')
#    for k in range(1,i+1):
#        print(k,end=' ')
#    print()
#==================================================
#        5 
#      5 4 
#    5 4 3 
#  5 4 3 2 
#5 4 3 2 1 
#for i in range(5):
#    for j in range(5-i-1):
#        print(' ',end=' ')
#    for k in range(i+1):
#        print(5-k,end=' ')
#    print()
#==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==x==
