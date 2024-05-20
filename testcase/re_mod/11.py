a = [1, 3, 12, 7, 3, 1, 5, 8, 12, 5, 21, 44]
print(sorted(a))
a.sort()
print(a)
a = set(a)
print(a)
print('===================================================')
import re

content = 'abcabcabc'
rex = re.search('c', content)
print(rex)
print(rex.group())

rex1= re.findall('c', content)
print(rex1)

print(len(a))

print('===================================================')

import requests

session = requests.session()
r1 = session.get()
# r2=session.post()
print('===================================================')







