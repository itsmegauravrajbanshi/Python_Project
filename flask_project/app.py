from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Dice Roller! <a href='/roll'>Roll the dice</a>"