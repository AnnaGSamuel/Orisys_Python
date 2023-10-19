from flask import Flask
import random

app = Flask(__name__)

rand_num = random.randint(0,9)

@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1> \
            <img src="https://media.giphy.com/media/kWJs200Ffsob6/giphy.gif" alt="some gif">'

@app.route("/number/<int:num>") 
def guess_num(num):
    if(num==rand_num):
        return '<p>You guessed right!</p> \
            <img src="https://media.giphy.com/media/hdLWaVK5geNt4pwyh9/giphy.gif" alt="happy gif">'
    elif(num>rand_num):
        return '<p>You guessed too high!</p> \
            <img src="https://media.giphy.com/media/kWJs200Ffsob6/giphy.gif" alt="some gif">'
    else:
        return '<p>You guessed too low!</p> \
            <img src="https://media.giphy.com/media/kWJs200Ffsob6/giphy.gif" alt="some gif">'

if __name__ == "__main__":
    app.run(debug=True)
