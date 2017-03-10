from bs4 import BeautifulSoup
import requests
import random

from flask import Flask
from flask import render_template

app = Flask(__name__)


def word():
    """Generate a list of words and shuffle them"""
    words = list()

    req = requests.get('https://en.wikipedia.org/wiki/List_of_plain_English_words_and_phrases')
    html_source = req.text
    soup = BeautifulSoup(html_source, "html.parser")

    for source in soup.find_all('a', { "class" : "extiw" }):
        word = source.find(text = True)
        try:
            word = str(word)
            words.append(word)
        except:
            pass

    random.shuffle(words)
    return words


def instruction(words):
    """Build an instruction from the word lists"""
    instruction_struct = [
        'I', words[0], words[8], 'the',
        words[2], words[5], 'with',
        words[4], words[7]
    ]

    instruction = ' '.join(instruction_struct)
    print instruction

words = word()
instruction(words)

@app.route('/')
def index():
    instruction = word()
    return render_template('index.html', fluxus=instruction)

if __name__ == '__main__':
    app.run()
