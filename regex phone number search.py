import re
message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())
print(phoneNumRegex.findall(message))
message2 = 'Molya, svurzhete se s men na 0888888888 ili na stacionaren nomer 02/9212100'
BGPhonemobileregex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
BGPhonestationaryphoneregex = re.compile(r'\d\d/\d\d\d\d\d\d\d')
mo = BGPhonemobileregex.search(message2)
print(mo.group())
mo = BGPhonestationaryphoneregex. search(message2)
print(mo.group())
