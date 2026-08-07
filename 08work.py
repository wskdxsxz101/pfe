fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) >= 2:
        count += 1
        print(words[1])
print('there are', count, 'lines')

all = []
while True:
    num = input('Enter a number:')
    if num == 'done': break # 这一行不太熟
    int(num)
    all.append(num)
print(max(all), min(all))

