from pyrogram import Client, filters
from gtts import gTTS
from NAYRA_X_ROBOT import app


@app.on_message(filters.command('tts'))
def text_to_speech(client, message):
    if len(message.text.split(' ', 1)) > 1:
     text = message.text.split(' ', 1)[1]
    tts = gTTS(text=text, lang='hi')
    tts.save('speech.mp3')
    client.send_audio(message.chat.id, 'speech.mp3')
