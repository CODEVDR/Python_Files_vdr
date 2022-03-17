#wap to input a no and print revese of the given no
no=int(input('Enter a Number:'))
rev=0
while(no>0):
    d=no%10   #digit extraction
    rev=rev*10+d
    no=no//10 #digit Elimination
print(rev,'is the reverse number!!!!')
