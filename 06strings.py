fruit = 'banana'
letter = fruit[0]
print(letter)
x = len(fruit)
print(x)
# index = 0
# while index < x:
#     print(fruit[index])
#     index += 1
for a in fruit:
    print(a) # 代码越少错误越少

for a in '123456': # str会每个一个空，[]整体是一个，得分开
    print(a)

s = "wo xi huan ni"
print(s[0:2])
print(s[3:5])
print(s[6:10])
print(s[11:13])

fruit = "banana"
n = 0
for a in fruit: # str会每个一个空，[]整体是一个，得分开，所以不能用[fruit]
    if 'n' == a:
        n = n + 1
print(n)

name = 'Z Hy'
lower_name = name.lower() # 小写
upper_name = name.upper() # 大写
print(lower_name, upper_name)

fruit = "banana"
x = fruit.find('na') # 找到na的位置
y = fruit.find("z") # 没有所以返回-1
print(x,y)

fruit = "banana"
x = fruit.replace('n', 'a') # 更换位置
print(x)

fruit = "      banana      "
x = fruit.lstrip()
y = fruit.rstrip()
z = fruit.strip() # 去除空格
print(x)
print(y)
print(z)

line = 'banana is delicious'
x = line.startswith('banana')
y = line.startswith('b') # 首个字母，首个单词都可以，但是严格大小写
print(x, y)

email = '2634658310@qq.com '
place = email.find('@')
space = email.find(' ', place)
host = email[place + 1: space]
print(host)
