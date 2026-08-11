# import urllib.request, urllib.error, urllib.parse
# url = input("Enter:")
# html = urllib.request.urlopen(url)
# count = 0
# target = 1000
# for line in html:
#     words = line.decode().split()
#     if count + len(words) < target: 
#         print(line.decode().strip())
#         count = count + len(words)
#     else:
#         n = target - count
#         print(' '.join(words[: n])) 
#         break # 最好加一个，不然还是会遍历全部文本

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
url = input("Enter:")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    # print(tag.get('href', None)) # <a href=...>为常见格式，所以检索href
    href = tag.get('href', None)
    full_url = urllib.parse.urljoin(url, href) # 填充完整
    print(full_url)
