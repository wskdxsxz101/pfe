n = 5
while n > 0:
    print(n)
    n -= 1
print("end")

n = 0
while True:
    if n < 5:
        n = n + 1
        print(n)
        continue
    else:
        print(n)
        break
print("done")

for i  in [5, 4, 3, 2, 1]:
    print(i)
print("done")

friends = ['a', 'b', 'c']
for friend in friends:
    print('hello', friend)
print('all')

for num in [13,41234,25,125,56723]:
    if num > num_0:
        num_0 = num
print(num_0)

num = None # 我也觉得用随便一个数字怎么都可能存在特殊情况，就应该有一个空的标志
count = 0
sum = 0  
for a in [484,525,68,253,6854,253,573]:
    count = count + 1
    sum = a + sum
    print(count, sum)
print(sum / count)

biggest = None
for num in [13,41234,25,125,56723]: # 有None以后就要更新一下了
    if biggest is None:
        biggest = num
    elif biggest < num:
        biggest = num
print(biggest)