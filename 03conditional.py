x = 5
if x < 10:
    print("smaller")
if x > 20:
    print("bigger")
print('finish')

num = int(input())
if num > 1:
    print("more than 1")
    if num < 100:
        print("less than 100")
print("all done")

if num < 2:
    print("less than 2")
elif num < 20:
    print("less than 20")
# elif num < 10:    顺序检索，不会运行
#     print('never play role')
elif num < 200:
    print("less than 200")
else:
    print("more than 200")

a = 'hello'
try:
    print(a) # 正常执行
    a = int(a)
    print(a) # 这里的不会执行，因为上一行报错直接到except了
except:
    print(a)

password = input("write your password:")
a=0
try:
    int(password)
except:
    a=-1
if a >= 0:
    print("yes")
else:
    print("no")