import os 

filename = "highscore.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

def get_highscore():
        with open (file_path, "r") as file:
            content = file.read()
        return content

var = get_highscore()

if len(var) > 0:
    print (var)
else:
    print ("File is empty")