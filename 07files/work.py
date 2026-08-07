fhand = open('07files/mbox-short.txt')
for line in fhand:
    line = line.upper()
    print(line)

fhand = open('07files/mbox-short.txt')
count = 0
sum = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        print(line)
        x = line.find(':')
        y = line[x + 1:]
        y = float(y)
        sum = sum + y
        count = count + 1
print("average:", sum / count)

fname = input("enter the file:")
if fname == "egg":
    print('egggggggggg')
    quit()
try:
    fhand = open(fname)
except:
    print('nofound')
print('I found it')