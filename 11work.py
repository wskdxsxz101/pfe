import re
fhand = open('mbox-short.txt')
count = 0
word = input('Enter a regular expression:')
for line in fhand:
    if word == 'done':
        quit()
    stuff = re.findall(word, line)
    if stuff:
        count = count + 1
print(count)

allnum = []
for line in fhand:
    x = line.find('New Revision:')
    line = line.rstrip()
    stuff = re.findall(r'^New Revision:\s*([0-9.]+)', line)
    if stuff:
        num = int(stuff[0])
        allnum.append(num)
print(sum(allnum) / len(allnum))

