cards = []
cards.append(3)
cards.append(5)
print(cards)
cards[1] += 2
print(cards)

carbinet = dict()
carbinet['summer'] = 4 # 相当于给4加了一个标签
carbinet['spring'] = 1
print(carbinet)
carbinet['spring'] += 1
print(carbinet)

count = dict()
names = ['a', 'b', 'c', 'a']
for name in names:
    # if name not in count:
    #     count[name] = 1
    # else:
    #     count[name] += 1
    count[name] = count.get(name, 0) + 1 # 如果不存在就加入一个并使'': 0     如果存在就指向这一个
print(count)

count = dict()
fhand = open('search.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word  not in ['the', 'and', 'to', 'of', 'that', 'etc.']:
            continue
        else:
            count[word] = count.get(word, 0) + 1
print(count)

jjj = {'mmk': 1, 'mmx': 2, 'mmm': 3}
print(list(jjj)) 
print(list(jjj.keys())) # 效果一样，因为遍历字典时默认遍历的就是键（keys）
print(list(jjj.values()))
print(list(jjj.items())) # 复合数据结构

jjj = {'mmk': 1, 'mmx': 2, 'mmm': 3}
for aaa,bbb in jjj.items():
    print(aaa, bbb) # aaa是mmk这一类，bbb是1这一类
