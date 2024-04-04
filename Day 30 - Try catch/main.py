try:
    file = open("a_file.txt")
except FileNotFoundError as error_message:
    print(f"An error was encountered: {error_message} . A new file will be created")
    file = open("a_file.txt", "w")
    file.write("Something")
else:
    content = file.read()
    print(content)
finally:
    file.close
    print("File was closed")
    
#This day focuses on raising exceptions and exception handling.
#Apart from a few try/except exercises, the main work was done on the Day 26 and Day 29 codes.