str = 'X-DSPAM-Confidence: 0.8475'
x = str.find(':')
y = len(str)
z = str[x + 1 : y]
print(float(z))