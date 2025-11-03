from flask import Flask, render_template, request
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    
    # If user didn't enter anything
    if not text.strip():
        return "Please enter some text!"

    # Create a speech file using Google TTS (supports Hindi + English)
    tts = gTTS(text=text, lang='hi', tld='co.in')  # 'hi' for Hindi voice
    file_path = os.path.join('static', 'output.mp3')
    tts.save(file_path)
    
    return render_template('index.html', audio_file=file_path)

if __name__ == '__main__':
    app.run(debug=True)
