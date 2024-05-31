from flask import Flask
import random

random_num = random.randint(0, 9)
print(random_num)

app = Flask(__name__)

@app.route("/")
def guess_number():

    return '<h1>Guess The Number Between 0 and 9<h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:number>")
def random_number(number):

    if number == random_num:
        return '<h1 style="color:green">You Found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number < random_num:
        return '<h1 style="color:red">Too low! Try again</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > random_num:
        return '<h1 style="color:blue">Too high! Try again</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color:red">Wrong Input</h1>'


if __name__ == "__main__":
    app.run(debug=True)