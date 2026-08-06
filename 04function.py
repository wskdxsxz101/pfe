def thing():
    print("hello")
    print("fun")
thing()

x = 5
def a():
    print("this is a") # 只有使用才会有输出，这里只是定义
x = x + 2
a()
print(x)

def greet(name):
    if name == "a":
        print("hello a")
    elif name == "b":
        print("hello b")
    else:
        print("hello")
    return print("nice") # 我去return可以返回复杂的东西
name = input("who:")
greet(name)