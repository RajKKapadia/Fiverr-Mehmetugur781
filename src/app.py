import time

from flask import Flask, request
from dotenv import load_dotenv, find_dotenv

from helper.openai_api import chat_complition, turkish_to_english, english_to_turkish
from helper.twilio_api import send_message

load_dotenv(find_dotenv())


app = Flask(__name__)


@app.route('/')
def home():
    return 'All is well...'


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        query = request.form['Body']
        sender_id = request.form['From']
        print(f'{sender_id} -> {query}')
        to_english = turkish_to_english(query)
        print(to_english)
        time.sleep(0.5)
        response = chat_complition(to_english)
        print(response)
        time.sleep(0.5)
        to_turkish = english_to_turkish(response)
        time.sleep(0.5)
        send_message(sender_id, to_turkish)
        print(to_turkish)
    except:
        send_message(sender_id, 'We are facing a technical issue at this time.')
    return 'OK', 200
