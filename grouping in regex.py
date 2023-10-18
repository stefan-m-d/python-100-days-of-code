import re
phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
print (phoneNumRegex.search('Nomerat mi e 0888888888'))
mo = phoneNumRegex.search('Nomerat mi e 0888888888')
print (mo.group())
phoneNumRegex = re.compile(r'(\d\d\d\d)(\d\d\d\d\d\d)')
mo = phoneNumRegex.search('Nomerat mi e 0888888888')
print (mo.group(1))
print(mo.group(2))
