import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import speech_recognition as speechRec
from gtts import gTTS
from io import BytesIO
import pygame
import time
import webbrowser
def PlaySound(text, language='en'):
    byteSound = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(byteSound)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(byteSound, 'mp3')
    pygame.mixer.music.play()
myRec = speechRec.Recognizer()
while True:
    with speechRec.Microphone() as source:
        print("Waiting for your talk...")
        try:
            sound = myRec.listen(source, timeout=3, phrase_time_limit=5)
            text=myRec.recognize_google(sound, language='en-en')
            PlaySound("Google search results for "+text+" are listed.")
            url = "https://www.google.com/search?q="+text
            webbrowser.open(url)
        except speechRec.RequestError:
            print("Internet Connection Error")
        except speechRec.WaitTimeoutError:
            print("Time Out Error")
        except speechRec.UnknownValueError:
            print("Unidentified Speech")
