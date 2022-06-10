import csv


print("1.For Write Data")
print("2.For Read Data And Check Eligiblity")
try:
    n = int(input("Select And Enter : "))
except:
    print("Error : Type Error")
    n = int(input("Select And Enter Again  : "))
if n == 1:
    with open("student.csv", "a") as f:
        r = []
        n = int(input("Enter A Number : "))
        l = []
        for i in range(n):
            try:
                n = input("Enter Student Name : ")
                cls = int(input("Enter Student Class : "))
                cgp = float(input("Enter Student CGPA : "))
                n = n.lower()
                cls = cls.lower()
                cgp = cgp.lower()
            except:
                n = input("Enter Student Name : ")
                cls = int(input("Enter Student Class : "))
                cgp = float(input("Enter Student CGPA : "))
                n = n.lower()
                cls = cls.lower()
                cgp = cgp.lower()
            l.append(n)
            l.append(cls)
            l.append(cgp)
            r.append(l)
        content = csv.writer(f)
        content.writerows(r)
        print("Writing Data")
        f.close()
elif n == 2:
    with open("student.csv", "r") as f:
        content = csv.reader(f)
        l1 = []
        for i in content:
            l = i
            l1.append(l)
        nm = input("Enter Student Name : ")
        nm = nm.lower()
        s = "Processing"
        v = ""
        for i in s:
            v += i
            print(v)
        for i in range(len(l1)):
            if l1[i][0] == nm:
                if float(l1[i][2]) >= 8.5:
                    v = 1
                elif float(l1[i][2]) >= 7.5:
                    v = 2
                elif float(l1[i][2]) >= 6.5:
                    v = 3
                elif float(l1[i][2]) >= 4.5:
                    v = 4
                else:
                    v = 0
        if v == 1:
            print("Student Eligible For Computer Science")
        elif v == 2:
            print("Student Eligible For Electrical Science")
        elif v == 3:
            print("Student Eligible For Mechanical Science")
        elif v == 4:
            print("Student Eligible For Matellergy")
        elif v == 0:
            print("Score More Than 4.5 Cgpa To Get Admission")
else:
    print("Select and Enter From[1/2]")