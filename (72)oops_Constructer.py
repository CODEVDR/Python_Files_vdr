#CONSTRUCTER
#------------------------------
"""class Employee:
    Employee="Google"

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee Is Created")
    
    
    def getDetails(self):
        print(f"Employee's Name is {self.name}")
        print(f"Employee's Salary is {self.salary}")
        print(f"Employee's subunit is {self.subunit}")


vdr=Employee("vdr",10000,"Youtube")
vdr.getDetails()"""
#PRACTICE QUESTIONS FOR OOPS CONCEPT
#-------------------------------------
#CREATE A CLASS PROGRAMMER FOR STORING INFORMATION OF FEW PROGRAMMERS WORKING AT MICROSOFT
"""class Programmer:
    Company = "Microsoft"

    def __init__(self,empid,name,dob,salary):
        self.empid=empid
        self.name=name
        self.dob=dob
        self.salary=salary
    
    def getDetails(self):
        print(f"Company {self.Company}")
        print(f"Employee's Id is {self.empid}")
        print(f"Employee's Name is {self.name}")
        print(f"Employee's D.O.B is {self.dob}")
        print(f"Employee's Salary is {self.salary}")
vdr=Programmer(3502,"VDR","26-10-2004",100000)
vdr.getDetails()"""
#---------------------------------------------------------
#WRITE A CLASS CAPABLE OF FINDING SQUARE,CUBE,SQUAREROOT OF A NUMBER:
"""class eval:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"Square of {self.num} is {self.num**2}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num**3}")
    def sqrt(self):
        print(f"SquareRoot of {self.num} is {self.num**1/2}")


num=eval(int(input("Enter Number: ")))
num.square()
num.cube()
num.sqrt()"""
        