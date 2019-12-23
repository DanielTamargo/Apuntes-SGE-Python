import datetime
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
#from google.cloud import speech_v1
#from google.cloud.speech_v1 import enums

#text-to-speech
def tts(texto):
    lenguaje = "es-ES" # Lista: https://developers.google.com/admin-sdk/directory/v1/languages
    tts = gTTS(text=texto, lang=lenguaje)
    hoy = datetime.datetime.today()
    hoy = hoy.strftime("%d-%m-%Y_%H-%M-%S")
    nombre_archivo = "Audios/" + str(hoy) + "_" + str(lenguaje) + "_tts_voice.mp3"
    tts.save(nombre_archivo)
    playsound.playsound(nombre_archivo)

def tts_japones(texto):
    lenguaje = "ja" # Lista: https://developers.google.com/admin-sdk/directory/v1/languages
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
            said = r.recognize_google(audio, language='es-ES')
            #print(said)
        except Exception as e:
            pass
            #print("Ruidos")
            #tts("No te he entendido.")
            #print("Exception: " + str(e))
    return said

# speech_recognition está enfocado al idioma inglés

def evitar_tildes(cadena):
    # Este método sustituye los caracteres que darían problemas al enviar el email: ñ ¡ ¿

    dic_correciones = {
                       "á": "a",
                       "à": "a",
                       "é": "e",
                       "è": "e",
                       "í": "i",
                       "ì": "i",
                       "ó": "o",
                       "ò": "o",
                       "ú": "u",
                       "ù": "u",
                       "Á": "A",
                       "À": "A",
                       "É": "E",
                       "È": "E",
                       "Í": "I",
                       "Ì": "I",
                       "Ó": "O",
                       "Ò": "O",
                       "Ú": "U",
                       "Ù": "U"
                       }
    cadena = str(cadena)
    #print(cadena)
    for i in range(len(cadena)):
        if cadena[i] in dic_correciones:
            cadena = cadena.replace(cadena[i], dic_correciones[cadena[i]])
    #print(cadena)
    return cadena

def conversacion():
    print("Notas:")
    print("- Graba cada vez que suene el 'blup'")
    print("- Graba cada vez que capta sonido hasta que deja de captarlo (frase a frase, o sonidos random)")
    print("- Si tras decir una frase suena el 'blup' de nuevo, es que está grabando y esa frase no tiene respuesta")
    print("- Di 'Adiós' para salir.")
    print("- Está totalmente W.I.P.")
    print("Está grabando:")

    blop = "ImportanteNoBorrar/blop-inicio-grabacion.mp3"
    nombre = ""

    while True:
        playsound.playsound(blop)
        frase = str(vtt())
        print("\r" + frase, end="")
        #tts(frase)
        frase = evitar_tildes(frase)

        if "Adios" == frase.capitalize():
            return True

        if "hola" in frase:
            tts("hola a ti")

        if ("como te llamas" or "cual es tu nombre" or "cuales tu nombre" or "dime tu nombre") in frase:
            if nombre == "":
                tts("No sé, ¿Cómo quieres que me llame?")
                frase = str(vtt())
                print("\r" + frase, end="")
                tts("¿Quieres que me llame: " + frase + "?")
                posible_nombre = frase
                frase = str(vtt())
                print("\r" + frase, end="")
                if ("sí" or "si" or "claro" or "por qué no" or "porque no") in frase:
                    nombre = posible_nombre
            else:
                tts("Mi nombre es: " + str(nombre))
        # Rellenar con alternativas y opciones
        if ("dime" and "japones") in frase:
            tts_japones("Kanben shite kure! Yamero! Shinpai suru na! Nani yatte n no yo?! Ittekimasu! Irasshaimase!")





