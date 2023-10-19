from flask import Flask

app = Flask(__name__)

@app.route("/") #home route
def hello_world():
    return '<h1>Hello world</h1> \
            <img src="https://media.giphy.com/media/kWJs200Ffsob6/giphy.gif" alt="some gif">'

if __name__ == "__main__":
    app.run(debug=True)
