# CONDITIONAL STATEMENTS
# ----------------------
# In Python we Have Three Conditional Statements i.e. if , elif , else
# <syntax>
"""
if <Syntax>:
   <Statements>
elif <syntax>:
   <Statements>
else:
   <Statements>
"""
# Wap in python to check the candidate is eligible for voting or not
n = int(input("Enter Your age : "))

if n == 18:
    print("Think And Vote")
elif n > 18:
    print("You Are Eligible For Vote")
else:
    print("Note You are Not Eligible For Voting ")
