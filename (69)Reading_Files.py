#OPEN USED FOR READING FILE CONTENT
"""f= open("Reading_Files.txt","r")
f= open("Reading_Files.txt")#BY DEFAULT IT IS ONLY READABLE
data=f.read()
data=f.read(5) #READ ONLY FIRST 5 CHARACTERS
print(data)
f.close"""
#-------------------------------------
#READLINE USED TO READ A LINE PRESENT IN A FILE
"""f=open("Reading_Files.txt")
data=f.readline()
print(data)
f.close()"""
#------------------------------------
"""Mods For Reading File
r=read data
w=write data
a=append data
+=update data
'rb'=will open for read binary
'rt'=will open for read in text mode"""
#--------------------------------------
#WRITING FILES IN PYTHON
"""f=open("Reading_Files.txt","w")
data=f.write("Hii This is Vdr...")#WRITE OVERWRITES THE WHOLE CONTENTS PRESENT IN FILE
f.close()"""
#-------------------------------------
#APPENDING FILES IN PYTHON
"""f=open("Reading_Files.txt","a")
data=f.write("Vdr Is A Hacker.....\nHe Uses Kali Linux For Hacking.....")#APPEND APPENDS THE WRITTEN CONTENT IN THE FILE....
f.close()"""
#-------------------------------------
print("""****
***
**
*""")
s=input("Do You Want To Get Source Code [Y/N]: ")
s1=input("Do You Want To Edit Code [Y/N]: ")
if s=="Y" or s=="y":
    with open("Source_Code.txt","r") as f:
        code=f.read()
        print(code)
if s1=="Y" or s1=="y":
    with open ("Source_Code.txt","a") as f:
        code="\n"+str(f.write(input("Enter The Changes And Try to Use Correct Indent \n")))
        print("Open Source_Code.txt To See Changes!!!!")
