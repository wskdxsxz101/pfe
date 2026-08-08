fhand = open('mbox-short.txt')
count = dict()
for line in fhand:
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) >= 2:
        count[words[1]] = count.get(words[1], 0) + 1
print(sorted([(v, k) for k, v in count.items()]))

fhand = open('mbox-short.txt')
count = dict()
for line in fhand:
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) >= 4:
        word = words[5].split(":")
        count[word[0]] = count.get(word[0], 0) + 1
print(sorted([(v, k) for k, v in count.items()]))

fhand = open('search.txt')
count = dict()
for line in fhand:
    line = line.rstrip().lower()
    # for letters in line:
    #     count[letters] = count.get(letters, 0) + 1 # 统计标点还是太变态了
    for char in line:
        if char.isalpha():
            count[char] = count.get(char, 0) + 1 # 更好的取字母法
print(sorted([(v, k) for k, v in count.items()]))

    
    