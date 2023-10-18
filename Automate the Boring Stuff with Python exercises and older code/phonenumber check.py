def isPhoneNumber (text): #BG phone number format
    if len(text) !=10:
        if len(text) !=13:
            return False #not BG format size
        if text[0] != "+":
            return False #not +359 format
    for i in range (0,10):
        if not text[i].isdecimal():
            return False #not all 10 characters are numbers
    return True 

print(isPhoneNumber('+359888888888'))
print(isPhoneNumber('0888888888'))

def isPhoneNumberUS (text): 
    if len(text) !=12:
        return False # not phone number sized
    for i in range (0,3):
        if not text[i].isdecimal ():
            return False 
    if text[3] != '-': 
        return False 
    for i in range (4,7):
        if not text[i].isdecimal ():
            return False
    if text[7] != '-':
        return False
    for i in range (8,12 ):
        if not text[i].isdecimal ():
            return False 
    return True 

message = 'Call me 415-555-101 tomorrow, or at 415-555-999 for my office line.'
foundNumber = False 
for i in range (len(message)):
    chunk = message[i:i+12]
    if isPhoneNumberUS(chunk):
        print('Phone number found: '+chunk)
        foundNumber=True
if not foundNumber:
    print('Could not find any phone numbers.')