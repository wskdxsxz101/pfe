stuff = "x \n y"
x = len(stuff) # 五个字符，\n只算一个
print(stuff, x)

xfile = open('better.txt')
x = 0
for y in xfile:
    x = x + 1
    print(y)
print(x)

xfile = open('better.txt')
book = xfile.read()
print(len(book))
print(book[:100])

xfile = open('better.txt')
for y in xfile:
    y = y.rstrip() # 没有这个的话会把换行也读取进去
    if y.startswith('However'):
        print(y) # 神奇

xfile = open('better.txt')
for y in xfile:
    y = y.rstrip()
    if not 'tools' in y:
        continue
    print(y)

fname = input('enter the file name:')
try:
    fhand = open(fname)
except:
    print('nothing there')
    quit()
count = 0
for line in fhand:
    if line.startswith('However'):
        count += 1
print(count)    
