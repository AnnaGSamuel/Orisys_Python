from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route("/")
def hello():
    return render_template("index1.html", blogs = response)

if(__name__ == "__main__"):
    app.run(debug=True)