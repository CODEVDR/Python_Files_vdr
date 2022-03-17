#wap to input a character and check weather the given character is in uppercase
#or in lowewr case
ch = input("Enter a Character : ")
if(ch.isupper()):
    print("The Given Character ", ch, "is an Uppercase Alphabet")
elif(ch.islower()):
    print("The Given Character ", ch, "is a Lowercase Alphabet")
else:
    print("The Given Character ", ch, "is a special character")











