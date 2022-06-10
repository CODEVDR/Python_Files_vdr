#Operators overloading
"""operators in python can be overloded using dender(__) method"""
class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):#__add__ is A method
        return self.num+ num2.num
    
n1=Number(6)
n2=Number(4)
sum=n1 + n2
print(sum)
