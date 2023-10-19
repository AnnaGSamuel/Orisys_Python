from flask import Flask

app = Flask(__name__)

@app.route("/") #home route
def hello_world():
    return "<h1>Hello world</h1>" 

@app.route("/bye") 
def bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True) 
