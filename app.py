from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def root():
    return f"""Your random number is {randint(1000, 9999)}."""