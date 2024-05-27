from flask import Flask, render_template
import requests 

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()
keys = list(data)
temp = keys[0]
print (type(temp))
print (temp)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=data, keys=keys)

@app.route('/post/<num>')
def get_blog(num):
    item = keys[int(num)]
    print (item)
    return render_template("post.html", title=item["title"], subtitle=item["subtitle"], body=item["body"])    

if __name__ == "__main__":
    app.run(debug=True)
