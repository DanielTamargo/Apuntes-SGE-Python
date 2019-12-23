import datetime
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

#text-to-speech
def tts(texto):
    lenguaje = "es-us" # Lista: https://developers.google.com/admin-sdk/directory/v1/languages
    tts = gTTS(text=texto, lang=lenguaje)
    hoy = datetime.datetime.today()
    hoy = hoy.strftime("%d-%m-%Y_%H-%M-%S")
    nombre_archivo = "Audios/" + str(hoy) + "_" + str(lenguaje) + "_tts_voice.mp3"
    tts.save(nombre_archivo)
    playsound.playsound(nombre_archivo)

#voice-to-text
def vtt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Probablemente te estás riendo...")
            #tts("No te he entendido.")
            #print("Exception: " + str(e))
    return said

# speech_recognition está enfocado al idioma inglés


while True:
    frase = str(vtt())
    #tts(frase)

    if "hola" in frase:
        tts("hola a ti")


