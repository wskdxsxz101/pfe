count = 0
total = 0
while True:
    num = input('Enter a number:')
    try:
        if num == 'done': # 不需要括号
            break
        else:
            num = int(num)
            total = total + num
            count = count + 1
    except:
        print('Invalid input')
if count == 0:
    print(total, count, 0)
else:
    print(total, count, total / count)