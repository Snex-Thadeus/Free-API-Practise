import os

from dotenv import load_dotenv
from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)
from twilio.rest import Client

load_dotenv()
app = Flask(__name__)
app.secret_key = "ssssh don't tell anyone"

TWILIO_PHONE_NUMBER = +19514762521

client = Client(
    "ACa58cc88cde3cedb825651ae997d0c34b",
    "dbe29be7097e1cb4f0ff9a56c5625b23"
)

def get_sent_messages():
    # TODO: Make this return a collection of messages that were sent from the number
    messages = []
    return messages

def send_message(to, body):
    # TODO: Send the text message
   client.messages.create(
    to=to,
    body=body,
    from_=+19514762521 
    )

@app.route("/", methods=["GET"])
def index():
    messages = get_sent_messages()
    return render_template("index.html", messages=messages)

@app.route("/add-compliment", methods=["POST"])
def add_compliment():
    sender = request.values.get('sender', 'Someone')
    receiver = request.values.get('receiver', 'Someone')
    compliment = request.values.get('compliment', 'wonderful')
    to = request.values.get('to')
    body = f'{sender} says: {receiver} is {compliment}. See more compliments at {request.url_root}'
    send_message(to, body)
    flash('Your message was successfully sent')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()