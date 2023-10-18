#global variables example

def spam():
    global eggs
    eggs = ' Hello'
    print(eggs)
    
eggs=42
spam()
print(eggs)

#local variables example

def spam():
    eggs = ' Hello'
    print(eggs)
    
eggs=42
spam()
print(eggs)