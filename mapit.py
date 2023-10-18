import webbrowser, sys, pyperclip

#Check if command line args were passed 

sys.argv 

if len(sys.argv) > 1: 
    #combine args in a single string
    address = ' '.join(sys.argv[1:]) #go from index 1 until the end of the string
else: 
    address = pyperclip.paste()
    
webbrowser.open('https://google.com/maps/place/' + str(address))
