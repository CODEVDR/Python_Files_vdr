import pickle

s = open("Pickle/data.bat", "wb")
d = "The Password is 000:111:000"
pickle.dump(d,s)
sn = open("Pickle/data.bat", "rb")
s.close()
s1=pickle.load(sn)
print(s1)
s.close()