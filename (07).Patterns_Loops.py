# pattern1:
for i in range(1, 8):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
# pattern2:
for i in range(1, 9):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
# pattern3:
for i in range(8, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# Pattern4:
for i in range(1, 8):
    for j in range(1, (8-i)+1):
        print(' ', end=' ')
    for k in range(1, i+1):
        print("*", end=' ')
    print()
# Patterns From 1 to 9
s = input("Enter a Number between 1 to 9:")
if s == '1':
    for i in range(1, 12):
        for j in range(1, 12):
            if (i+j == 8 and (i >= 1 and i <= 4)) or j == 7 or (i == 11 and j >= 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif s == "2":
    for i in range(1, 8):
        for j in range(1, 8):
            if (j == 1 and i >= 4 and i <= 7) or (j == 7 and i >= 1 and i <= 4) or i == 1 or i == 4 or i == 7:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif s == "3":
    for i in range(1, 8):
        for j in range(1, 8):
            if i == 1 or i == 4 or i == 7 or j == 7:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif s == "4":
    for i in range(1, 8):
        for j in range(1, 8):
            if (j == 1 and i >= 1 and i <= 4) or i == 4 or j == 7:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif s == "5":
    for i in range(1, 8):
        for j in range(1, 8):
            if i == 1 or i == 4 or i == 7 or (j == 1 and i >= 1 and i <= 4) or (j == 7 and i >= 4 and i <= 7):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif s == "6":
    for i in range(1, 8):
        for j in range(1, 8):
            if i == 1 or i == 4 or i == 7 or j == 1 or (j == 7 and i >= 4 and i <= 7):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif s == "7":
    for i in range(1, 8):
        for j in range(1, 8):
            if i == 1 or (i == 4 and j >= 2 and j <= 6) or i+j == 8:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif s == "8":
    for i in range(1, 8):
        for j in range(1, 8):
            if (i == 1 and j >= 2 and j <= 6) or (j == 1 and i >= 2 and i <= 6) or (i == 7 and j >= 2 and j <= 6) or (j == 7 and i >= 2 and i <= 6) or i == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif s == "9":
    for i in range(1, 8):
        for j in range(1, 8):
            if (i == 1 and j >= 2 and j <= 6) or (j == 7 and i >= 2 and i <= 6) or (i == 7 and j >= 2 and j <= 6) or ((j == 1 and i >= 2 and i <= 3)) or (i == 4 and j >= 2 and j <= 6):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Enter a number between 1 to 9")
    print("Aborting!!!!")
print("You entered", s, "and its pattern printed above!!!!")
print('Aborting!!!!')
