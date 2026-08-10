import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From', line) :
        print(line)

x = 'a23aefka34435-2=94tit21'
y = re.findall('[0-9]+', x)
z = re.findall('[AEIOU]', x) # 就算没有东西也会有输出
print(y, z)

x = 'a:wafhiklsfj:fhjiaojk:faw awf'
y = re.findall('a.+:', x) # 获得到最后一个:的位置，尽可能多的匹配，贪婪匹配，我去多个起点都是汇集在一起然后选最长的
z = re.findall('a.+?:', x) # 非贪婪匹配，尽可能少的匹配
print(y, z)
for line in fhand:
    # if not line.startswith('From'): continue
    # dress = re.findall('\S+@\S+', line)
    dress = re.findall('^From (\S+@\S+)', line) # 更简单的写法
    if dress: # 表示非空
        print(dress)

numlist = []
for line in fhand:
    line = line.rstrip()
    stuff = re.findall(r'^X-DSPAM-Confidence:\s*([0-9.]+)', line) # ':'也是内容
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print(max(numlist))
