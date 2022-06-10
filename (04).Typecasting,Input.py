# Type casting

"""In Python
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""

# Basically We Typecast in string to integer or int to str or int to float
# for e.g.
# Code Here
# Note While Typecasting be carefull in String it should be the digit..
s = '1234'
i = int(s)
print("Converting", s, type(s), "to", i, type(i))  # ---i
print(f"Converting {s} {type(s)} to {i} {type(i)}")  # ---ii
# f String allows us to use variables inside a String see in (i) we have to write more ,s And it Doesn't Look Cool So We use f string..'type' used to check type of value

# Code Here
s1 = "345"
s2 = int(s1)
s3 = float(s1)
s4 = complex(s1)
print(f"Converting {s1} {type(s1)} to {s2} {type(s2)}")
print(f"Converting {s1} {type(s1)} to {s3} {type(s3)}")
print(f"Converting {s1} {type(s1)} to {s4} {type(s4)}")

# Taking Input in Python
"""
For taking input in Python we write input()
input() stores values in form of String And We Will Tpyecast it to other forms"""
# e.g.
a = input("Enter : ")  # 1234
b = int(input("Enter : "))  # 1234
c = float(input("Enter : "))  # 1234
d = complex(input("Enter : "))  # 1234
print("Entered Sucessfully...")
print(f"String : {a} \nInteger : {b} \nFloat : {c} \nComplex :  {d}")
