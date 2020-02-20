'''
En este archivo de Python tendremos todas las funciones que ejecuten CÁLCULOS y COMPROBACIONES.
Por ejemplo:
- Calcular la edad a partir de una fecha
- Comprobar si un email ha sido introducido correctamente
'''
import datetime
import dateutil.relativedelta as dr
import re
import os
import time

import playsound
import speech_recognition as sr
from gtts import gTTS

#----------------------------------------------------------------------------------------------------------------------#
# Devuelve Boolean -> Comprueba que ha introducido un número
def es_un_numero(valor):
    try:
        valor = int(valor)
        if valor is not None:
            return True
        else:
            return False
    except:
        return False
#----------------------------------------------------------------------------------------------------------------------#
# Devuelve Boolean -> Recibe una letra y comprueba si es una 's' o una 'n' (clásico para comprobar si ha introducido sí o no por consola)
def si_o_no(texto):
    if texto == "s" or texto == "n":
        return True
    else:
        return False
#----------------------------------------------------------------------------------------------------------------------#
# Devuelve Int (la edad) -> Calcula la edad en base a la fecha de nacimiento. Se basa en la fecha de nacimiento
# Recibe un String o un Date (o ¿datetime?)
def edad(fecha_nacimiento):
    fecha_nac = str(fecha_nacimiento)
    if fecha_nac != "Unknown":
        fecha_nac = datetime.datetime.strptime(fecha_nac, '%Y-%m-%d')
        hoy = datetime.datetime.today()
        try:
            cumpleanyos = fecha_nac.replace(year=hoy.year)
        except:
            cumpleanyos = fecha_nac.replace(year=hoy.year, month=fecha_nac.month + 1, day=1)
        if cumpleanyos > hoy:
            return hoy.year - fecha_nac.year - 1
        else:
            return hoy.year - fecha_nac.year
    else:
        return -1 # <- Tratar el -1 como un error
#----------------------------------------------------------------------------------------------------------------------#
# Comprueba que la fecha sea válida (patrones, comprobar edad > 16, comprobar años bisiestos y transformación a fecha)
# Falta añadir más posibles patrones
def pedir_fecha(pregunta):
    c = colores()
    correcto = False
    while not correcto:
        patron1_b = False
        patron2_b = False
        fecha_a_devolver = ""

        fecha = input(pregunta)
        if len(fecha) > 0:
            if (fecha.lower() == "today" or fecha.lower() == "hoy") and "nacimiento" not in pregunta:
                fecha_a_devolver = datetime.date.today()
                return fecha_a_devolver
            if "vencimiento" in pregunta:
                if fecha.lower() == "dia":
                    hoy = datetime.date.today()
                    fecha_a_devolver = hoy + datetime.timedelta(days=1)
                    return fecha_a_devolver
                elif fecha.lower() == "semana":
                    hoy = datetime.date.today()
                    fecha_a_devolver = hoy + datetime.timedelta(weeks=1)
                    return fecha_a_devolver
        fecha = fecha.replace(" ","-")

        # Día-Mes-Año
        patron1 = re.compile("[0-3][0-9]-[0-1][0-9]-[1-2]\d{3}")
        if patron1.match(fecha):
            correcto = True
            patron1_b = True

        #Año-Mes-Día
        patron2 = re.compile("[1-2]\d{3}-[0-1][0-9]-[0-3][0-9]")
        if patron2.match(fecha):
            correcto = True
            patron2_b = True

        if patron1_b:
            try:
                fecha_a_devolver = datetime.datetime.strftime(datetime.datetime.strptime(fecha, "%d-%m-%Y"), "%Y-%m-%d")
            except:
                correcto = False
                fecha_a_devolver = ""

        if patron2_b:
            try:
                fecha_a_devolver = datetime.datetime.strftime(datetime.datetime.strptime(fecha, "%Y-%m-%d"), "%Y-%m-%d")
            except:
                correcto = False
                fecha_a_devolver = ""

        if patron1_b or patron2_b:
            if str(fecha_a_devolver) != "":
                if "nacimiento" in pregunta:
                    fecha_nac = datetime.datetime.strptime(fecha_a_devolver, '%Y-%m-%d')
                    hoy = datetime.datetime.today()
                    try:
                        cumpleanyos = fecha_nac.replace(year=hoy.year)
                    except:
                        cumpleanyos = fecha_nac.replace(year=hoy.year, month=fecha_nac.month + 1, day=1)
                    if cumpleanyos > hoy:
                        edad =  hoy.year - fecha_nac.year - 1
                    else:
                        edad = hoy.year - fecha_nac.year
                    if edad < 16:
                        correcto = False
                        print("{0}¡Ups!{1} Edad mínima requerida: {2}16{3}\n".format(c["lr"], c["rst"], c["r"], c["rst"]))
                    else:
                        return fecha_a_devolver
                else:
                    return fecha_a_devolver
            else:
                correcto = False
                print("{0}Error.{1} No has introducido una fecha válida.\n".format(c["lr"], c["rst"]))
        else:
            correcto = False
            print("{0}Error.{1} No has introducido una fecha válida.\n".format(c["lr"], c["rst"]))
#----------------------------------------------------------------------------------------------------------------------#
# Devuelve String (el email) -> Este método sirve para pedir un email, comprueba que es válido y lo devuelve
# Recibe un String (texto), que será la pregunta a mostrar cuando se pida el email -> Ejemplo: "Email: "
def email(texto):
    # Compruebo muchas cosas pero no establezco restricciones de longitud ni mínimas ni máximas
    # Iba a comprobar que no tuviera caracteres especiales (simbolos) pero un blog dice que son validos: http://preguntascojoneras.blogspot.com/2015/01/caracteres-validos-en-un-email.html
    valido = False
    email = ""
    while valido == False:
        email = input(texto)
        if email is not None and email != "":
            if "@" in email:
                # dominio = str(email.lstrip("@")) # lstrip no funciona como yo pensaba, es bastante más particular
                # así que opto por otra forma de hacerlo, averiguo la posición, y examino el dominio
                # compruebo que solo existe un @ y que el email no comience dierctamente por el @
                if email.find("@") == email.rfind("@") and email.find("@") > 0:
                    dominio = email[(email.find("@") + 1):len(email)]
                    if "." in dominio:
                        # para ver si el dominio termina bien, busco el último punto, a veces hay más de un punto, por ejemplo:
                        # daniel.tamargo@ikasle.egibide.org
                        # también compruebo que el punto no esté situado al final, el dominio no puede acabar en punto
                        # también compruebo que tras la @ no haya un punto
                        if dominio.rfind(".") < len(dominio) - 1 and dominio.find(".") > 0:
                            fin_dominio = dominio[(dominio.rfind(".") + 1):len(dominio)]
                            lista_finales_dominios = ["es", "com", "org", "net", "edu", "us", "me", "biz", "tk", "eu"] # Podría ser una lista eterna
                            if fin_dominio in lista_finales_dominios:
                                valido = True
                            else:
                                respuesta = ""
                                while respuesta == "":
                                    respuesta = input(colorama.Fore.LIGHTMAGENTA_EX + "'" + fin_dominio + "'" + colorama.Fore.RESET
                                                      + " es una terminación de dominio que no tenemos registrada. ¿Quieres guardarlo así? (s/n): ")
                                    if respuesta is not None or respuesta != "":
                                        respuesta = respuesta.lower()
                                        if respuesta == "s":
                                            valido = True
                                        elif respuesta == "n":
                                            print("Vuelve a introducir tu email.")
                                        else:
                                            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                                                  + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
                                    else:
                                        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                                              + colorama.Style.RESET_ALL + " No has introducido un nada :(")
                        else:
                            if dominio.find(".") == 0:
                                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                                      + colorama.Style.RESET_ALL + " El dominio no puede comenzar por un punto.")
                            else:
                                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                                      + colorama.Style.RESET_ALL + " El dominio no puede acabar en un punto.")
                    else:
                        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                              + colorama.Style.RESET_ALL + " El dominio no es válido (falta el punto).")
                else:
                    if email.find("@") == 0:
                        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                              + colorama.Style.RESET_ALL + " No has introducido un email válido (no puede empezar por @).")
                    else:
                        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                              + colorama.Style.RESET_ALL + " No has introducido un email válido (existe más de un @).")
            else:
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido un email válido (falta el @).")
        else:
            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                  + colorama.Style.RESET_ALL + " No has introducido un nada :(")
        print()

    return email
