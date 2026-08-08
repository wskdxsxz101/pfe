fname = input('Enter a file name:')
fhand = open(fname)
word = dict()
for line in fhand:
    if not line.startswith("From"): continue
    words = line.split()
    if len(words) >= 3:
        # x = words[2]
        # word[x] = word.get(x, 0) + 1
        word[words[2]] = word.get(words[2], 0) + 1 # 不是何意味啊，为什么一开始这个跑不通，跑完上面的这个又能跑了？？？？？？？？？
print(word)

fname = input('Enter a file name:')
fhand = open(fname)
word = dict()
for line in fhand:
    if not line.startswith("From"): continue
    words = line.split()
    if len(words) >= 2:
        word[words[1]] = word.get(words[1], 0) + 1
print(word)
bigname = None
bignum = None
for name, num in word.items():
    if bignum is None or bignum < num:
        bignum = num
        bigname = name
print(bigname, bignum)

fname = input('Enter a file name:')
fhand = open(fname)
count = dict()
for line in fhand:
    if not line.startswith("From"): continue
    words = line.split()
    word = words[1].split('@')
    count[word[1]] = count.get(word[1], 0) + 1
print(count)