from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route("/")
def hello():
    return render_template("index.html", blogs = response)

@app.route("/post/<int:id>")
def show_post(id):
    for blog in response:
        if(blog["id"] == id):
          requested_blog = blog
    
    return render_template("post.html", blog = requested_blog )

if(__name__ == "__main__"):
    app.run(debug=True)