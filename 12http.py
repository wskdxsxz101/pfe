import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  # 建议用完整域名
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(128)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close() # 太麻烦了，学习更简单的

import urllib.request, urllib.error, urllib.parse
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page2.htm')
for line in fhand:
    print(line.decode().strip())

import urllib.parse, urllib.error, urllib.request
from bs4 import BeautifulSoup
url = input("enter:")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))