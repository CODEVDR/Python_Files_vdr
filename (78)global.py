"""a=54#global value
def func1():
    global a
    print(f"1,{a}")
    a=8#Local Value converted to global value i.e. a=54 now a=8 and it is global
    print(f"2,{a}")
func1()
print(f"3,{a}")"""
x=10
def demo(आ):
    आ=आ+x
    b=15
    print("2",x)
    print("3",आ)
    print("4",आ+b)
print("1",x)
demo(20)
#print(आ) #Error