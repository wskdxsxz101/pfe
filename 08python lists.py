for i in [1,2,3,[4,5],6,7]: # [4,5]变成一个整体了
    print(i)

num = [1, 2, 3, 4, 5]
print(num)
num[3] = 20
print(num)

print(list(range(4))) # 要有list才是[0, 1, 2, 3]
friends = ['a', 'b' ,'c']
print(list(range(len(friends)))) # range只能输出数字
for i in range(len(friends)):
    friend = friends[i]
    print("happy", friend ,i)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

stuff = []
stuff.append('I')
stuff.append('love')
stuff.append('you')
print(stuff)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(9 in c, 1 not in c, 3 in c)

friends = ['Chfualif', 'Adwa', 'Bfaujfd']
friends.sort() # 不能用=，sort直接改变内部顺序
print(friends)

numlist = []
while True:
    a = input("number:")
    if a == 'done':
        break
    a = float(a)
    numlist.append(a)
print(sum(numlist) / len(numlist)) # 占用更多储存但是方便

a = 'I love you'
b = a.split() # 删除空格
print(b)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) >= 3:
        print(words[2])