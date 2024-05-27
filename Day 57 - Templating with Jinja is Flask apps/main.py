from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.now().year
    random_number = random.randint(1,10)
    return render_template("index.html", num=random_number, year=year)

@app.route(f'/guess/<name>')
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    data = response.json()

    name = data["name"]
    gender = data["gender"]

    response = requests.get(f"https://api.agify.io?name={name}")
    data = response.json()

    age = data["age"]
    return render_template("index2.html", gender=gender, age=age, name=str(name).title())

if __name__ == "__main__":
    app.run(debug=True)