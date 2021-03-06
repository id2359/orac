from flask import Flask, render_template
from flask_ask import Ask, question, statement

app = Flask(__name__)
ask = Ask(app, "/")

def get_briefing():
    # get via some other means
    return "This is a dummy briefing"


@ask.launch
def launched():
    return question("Orac launched")

@ask.intent("GrovelIntent")
def grovel():
    import random
    grovelling = ["How wonderful to speak with you again, Sir!",
                  "It is an honour to serve you, sire!",
                  "Greetings, Oh great one!"]
    
    text = random.choice(grovelling)
    return statement(text).simple_card("Grovelling", text)


@ask.intent("BriefingIntent")
def briefing():
    text = get_briefing()
    return statement(text).simple_card("Briefing", text)
    

if __name__=="__main__":
    app.run(debug=True)
