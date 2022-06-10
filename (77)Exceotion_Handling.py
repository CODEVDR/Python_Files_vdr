#Exception handling used to avoid the crashing the program
"""while True:
    print("Press q to quit")
    a=input("Wanna Quit: ")
    b=input("Enter no: ")
    if a=="q" or a=="Q":
        break
    try:#Might Throw Exception
        b=int(b)
        if b>6:
            print("You Entered a Greater No Then 6")
    except Exception as e:#accepts acception
        print(f"Your input resulted an error: {e}")"""
#HANDLING MULTIPLE EXCEPTIONS:-
"""try:
    n=int(input("Enter a Value: "))
    c=1/n
    print(c)
except ZeroDivisionError as e:
    print("Make Sure You Shouldn't divide by zero")
except ValueError as e:
    print("Plese Enter a valid syntax..")
except :
    print("Error..")
print("Thanks For Using My Code..")"""
#USING/RAISING CUSTOM EXCEPTIONS:-
"""def increment(n):
    try:
        print(int(n)+1)
    except:
        raise ValueError("Are You Madd Or What????")#raise is a keyword used to raise excepction.
increment(1)
increment("vdr")"""
#try with else clause
"""try:
    n=int(input("Enter a Number: "))
    c=1/n
except:
    print("Error 1/0 is not possible")
else:
    print(f"Code is scucessful \nThe Value of 1/{n} is {c}")"""
#try with finally
"""python offers a finally clasuse which ensures execution of a piece of code irrespective of the exception"""
"""try:
    n=int(input("Enter a Number: "))
    c=1/n
except:
    print("Error 1/0 is not possible")
    exit()
finally:
    print("Code is scucessful")"""
