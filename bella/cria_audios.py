import os
from gtts import gTTS
from playsound import playsound


def cria_audio(audio):
    tts = gTTS('oi, eu sou a bella', lang='pt-br')

    if not os.path.exists('audio'):
        os.makedirs('audio')

    tts.save('audio/hello.mp3')
    playsound('audio/hello.mp3')
    

