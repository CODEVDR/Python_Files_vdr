# loops


# In Python we have basically two types of loops
"""
(i)For Loop
(ii)While Loop"""

# using While Loops
# wap a program to print forward no 1 to 50 using while loop
no = 1
while no <= 50:
    print(no, end=' ')
    no = no+1
# wap a program to print backward no 50 to 1 using while loop
no = 50
while no >= 1:
    print(no, end=' ')
    no = no-1
# wap a program to print forward no 50 to 1 using for loop
for i in range(1, 51):
    print(i, end=" ")
# wap a program to print backward no 50 to 1 using for loop
for i in range(50, 0, -1):
    print(i, end=" ")
