from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0,9)
print(random_number)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/EE185t7OeMbTy/giphy.gif' width=200>"

def make_bold(function):
    def wrapper_bold():
        return "<b>" + function() + "</b>"
    return wrapper_bold

def make_emphasis(function):
    def wrapper_emphasis():
        return "<em>" + function() + "</em>"
    return wrapper_emphasis

def make_underline(function):
    def wrapper_underline():
        return "<u>" + function() + "</u>"
    return wrapper_underline

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_underline
@make_emphasis
def say_bye():
    return "bye"

# Creating Variable paths and converting the path to a specified data type

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return  f"Hello there {name}, you are {number} years old"

@app.route("/<int:number>")
def high_low(number):
    if number == random_number:
        return "<h1 style='color:green;'>You Guessed the right number!</h1>" \
               "<img src='https://media.giphy.com/media/bt8FwKXiNKRkQ/giphy.gif'>"
    elif number > random_number:
        return "<h1 style='color:purple;'>Too High, Try again!</h1>" \
               "<img src='https://media.giphy.com/media/CM1rHbKDMH2BW/giphy.gif'>"
    elif number < random_number:
        return "<h1 style='color:red;'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3OhXBaoR1tVPW/giphy.gif'>"




if __name__ == "__main__":
    app.run(debug=True)
