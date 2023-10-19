from flask import Flask

app = Flask(__name__)

@app.route("/number/<num>") 
def print_num(num):
    return f"The number is : {num}" 

if __name__ == "__main__":
    app.run(debug=True)