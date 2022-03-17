"""
PascalCase:
EmployeeName -->PascalCase

camelCase:
isNumeric, isFloat -->camelCase

"""
#PROGRAM
#--------------------------------------------
"""class VdrForm:
    formType = "VdrForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Id is {self.id} ")
vdrForm = VdrForm()#OBJECT INSTENTION
vdrForm.name = "V DURGESHWAR RAO"
vdrForm.id = "3502"
vdrForm.printData()"""
#---------------------------------------------------------
#CLASS ATTRIBUTES
"""class Employee:
    company="Google"
vdr=Employee()
vjr=Employee()
print(f"The Company vdr Working is {vdr.company}")
Employee.company="YouTube"
vdr=Employee
print(f"The Company vdr Working is {vdr.company}")"""
#---------------------------------------------------------
#INSTANCE ATTRIBUTES
"""class Employee:
    company="Google"
    salary=100 #CLASS ATTRIBUTE
vdr=Employee()
vjr=Employee()
#INSTANCE ATTRIBUTES
vdr.salary=1000#INSTANCE ATTRIBUTE VALUE MAY OR MAY NOT BE EQUAL TO CLASS ATTRIBUTE VALUE
vjr.salary=3000
#IF NO INSTANCE ATTRIBUTE IS PRESENT THEN IT SHOWS CLASS ATTRIBUTE AND IT THE ATTRIBUTE IS NOT PRESENT THEN IT SHOWS AN ERROR FOR EXAMPLE
#print(vdr.salary) AFTER THIS IT SHOWS OBJECT HAS NO ATTRIBUTE
print(f"The Company vdr Working is {vdr.company}")
Employee.company="YouTube"
vdr=Employee()
print(f"The Company vdr Working is {vdr.company}")"""
#-----------------------------------------------------
#SELF
#----
"""class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")
vdr=Employee()
vdr.salary=100000
vdr.getSalary() #or Employee.getsalary(vdr) both are same """
#STATIC METHOD
#------------------------------------
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning, Sir")

vdr=Employee()
vdr.salary=100000
vdr.greet()