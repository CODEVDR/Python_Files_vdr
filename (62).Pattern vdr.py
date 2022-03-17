#str1="VDR"
print_V=[[" " for i in range(10)] for j in range(10)]
print_D=[[" " for i in range(10)] for j in range(10)]
print_R=[[" " for i in range(10)] for j in range(10)]
#Code for V
for i in range(8):
    for j in range(10):
        if (i-j==0 and(j>=0 and j<=4)) or (i+j==8 and (j>=4 and j<=9)):
                    print_V[i][j]="*"
#Code for D
for i in range(1,8):
                for j in range(1,8):
                        if i==1 or i==7 or j==2 or j==7:
                             print_D[i][j]="*"
#Code for R
for i in range(1,8):
                for j in range(1,8):
                        if i==1 or j==1 or i==4 or(j==7 and(i>=1 and i<=4)) or (i-j==0 and (i>=5 and i<=9)):
                                print_R[i][j]="*"
#Main
for i in range(10):
    for j in range(10):
        print(print_V[i][j],end=" ")
    for j in range(8):
        print(print_D[i][j],end=" ")
    for j in range(8):
        print(print_R[i][j],end=" ")
    print()

                                
                       
                                              
                       
