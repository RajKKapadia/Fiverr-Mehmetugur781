import os

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


def turkish_to_english(query: str) -> dict:
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': f'Please translate the {query} into English language, if the {query} is in English just return the query.'}
            ]
        )
        return completion['choices'][0]['message']['content']
    except:
        return 'We are facing a technical issue at this time.'
    

def english_to_turkish(query: str) -> dict:
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': f'Please translate the {query} into Turkish language.'}
            ]
        )
        return completion['choices'][0]['message']['content']
    except:
        return 'We are facing a technical issue at this time.'
    

def chat_complition(query: str) -> dict:
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': query}
            ]
        )
        return completion['choices'][0]['message']['content']
    except:
        return 'We are facing a technical issue at this time.'
