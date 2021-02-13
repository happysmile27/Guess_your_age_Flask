from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f"https://api.genderize.io/?name[]={name}")
    gender = response.json()[0]["gender"]
    response1 = requests.get(url=f"https://api.agify.io?name[]={name}")
    age= response1.json()[0]["age"]
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)
