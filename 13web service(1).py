# import xml.etree.ElementTree as ET
# data = '''
# <person>
#   <name>Check</name>
#   <phone type="intl">
#     +1 1111111111
#    </phone>
#    <email hide="yes"/>
# </person>'''
# tree = ET.fromstring(data)
# print("name:", tree.find('name').text)
# print('Attr', tree.find('email').get('hide'))

# import xml.etree.ElementTree as ET
# data = '''
# <stuff>
#     <users>
#         <user x='2'>
#             <id>002</id>
#             <name>Dick</name>
#         </user>
#         <user x='3'>
#              <id>003</id>
#             <name>Suck</name>
#         </user>
#     </users>
# </stuff>''' # <>内部=右边要加''
# stuff = ET.fromstring(data)
# lst = stuff.findall('users/user') # findall返回为列表，不能.text
# print(len(lst))
# for item in lst:
#     print(item.find('name').text) # 最后还需要转码
#     print(item.find('id').text)

# import json
# data = '''{
#     "name" : "Dick",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 1111111111"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }'''
# info = json.loads(data)
# print(info["name"])
# print(info["email"]["hide"])

import json
data = '''[
    {"id" : "001",
     "name" : "Dick",
     "x" : "2"
    },
    {"id" : "002",
     "name" : "Suck",
    "x" : "3"
    }
]'''
info = json.loads(data)
for item in info:
    print(item['name'])
    print(item['id'])