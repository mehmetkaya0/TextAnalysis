from flask import Flask, render_template, request
import re

app = Flask(__name__)

def count_text(text):
    sentences = re.split(r'[.!?]+', text)
    num_sentences = len(sentences) - 1  # subtract 1 to exclude extra sentence at the end

    words = re.findall(r'\w+', text)
    num_words = len(words)

    num_chars = len(text) - text.count(' ')  # exclude spaces from character count

    return {'sentences': num_sentences, 'words': num_words, 'characters': num_chars}



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        result = count_text(text)
        return render_template('index.html', result=result, text=text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
