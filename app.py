from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def root():
    pre = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>flask spin</title>
        <style>
        html,
        body {
            width: 100%;
            height: 100%;
            margin: 0;
            overflow: hidden;
            background: #111;
            color: #cf0;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        }
        </style>
    </head>
    <body>
    """
    load = f"Your random number is {randint(1000, 9999)}."
    post = """
    </body>
    </html>
    """
    return pre + load + post