x = [3, 2, 1]
x.reverse()
print(x)
x = (1, 2, 3)
# x.reverse()完全不存在

l = list()
print(dir(l)) # dir()用于说明这个都能加什么后缀 

(a, b) = (99, 100)
print(a, b) # 可以,但是没必要

d = dict()
d['a'] = 2
d['b'] = 2
for k, v in d.items():
    print(k, v)
print(d.items())

print((1, 2, 3) < (0, 1, 999))
print(('Ha', 'ha', 'ha') > ('a', 'a'))
print((0, 1) < (0, 2)) # 可以比大小,先看第一个,然后往后走

d = {'a': 1, 'c': 3, 'b': 2,}
t = sorted(d.items())
print(t)

d = {'a': 22, 'b': 1, 'c': 3}
tmp = []
for (k, v) in d.items():
    tmp.append((v, k))
tmp = sorted(tmp)
print(tmp)

count = dict()
fhand = open('search.txt')
for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
lis = list()
# for (k, v) in count.items():
#     newtup = (v, k)
#     lis.append(newtup)
# lis = sorted(lis)
# for (v, k) in lis: # 为什么刚刚不行,现在又能跑了??????????
#     print(k, v)
print(sorted([(v, k) for k, v in count.items()])) # 我去,这么短,这么nb