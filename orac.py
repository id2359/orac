from flask import Flask, render_template
from flask_ask import Ask, question, statement

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def launched():
    return question("Orac launched")


if __name__=="__main__":
    app.run(debug=True)
