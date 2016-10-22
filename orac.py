from flask import Flask, render_template
from flask_ask import Ask, question, statement

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def launched():
    return question("Orac launched")

@ask.intent("GrovelIntent")
def grovel():
    import random
    grovelling = ["How wonderful to speak with you again, Sir!",
                  "It is an honour to serve you, sire!"]
    
    text = random.choice(grovelling)
    return statement(text).simple_card("Grovelling", text)

if __name__=="__main__":
    app.run(debug=True)
