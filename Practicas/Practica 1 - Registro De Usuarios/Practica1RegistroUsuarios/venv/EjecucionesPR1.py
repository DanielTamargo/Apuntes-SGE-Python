import FuncionesPR1
import time
import sys
import random
import colorama
import smtplib
import ssl

def textoNegro_fondoAmarillo(linea):
    # Este método recibe una cadena String y la muestra con el color del texto negro y el fondo azul claro
    # utiliza código ANSI, no hace falta instalar colorama, ni nada (aunque al final no uso este método)

    # print('\033[43m') # fondo amarillo
    # print('\033[90m') # texto negro claro
    if linea == "  TBPG  ":
        print('\033[43m' + '\033[90m' + linea.center(91, "="), end = "")
    else:
        print(linea, end = "")
    print('\033[49m' + '\033[39m')  # reset a los colores normales

def textoNegro_fondoAzulClaro(linea):
    # Este método recibe una cadena String y la muestra con el color del texto negro y el fondo azul claro
    # utiliza Colorama, una biblioteca descargada e importada

    # Cambiamos todo el estilo, añadimos color al texto y al fondo, y cambiamos el estilo a Bright
    print(colorama.Back.LIGHTBLUE_EX + colorama.Style.BRIGHT + colorama.Fore.LIGHTBLACK_EX, end = "")

    # Mostramos la línea
    print(linea, end = "")

    # Reseteamos todo para que no se mantengan los cambios en los demás textos
    print(colorama.Style.RESET_ALL)



def paripe_inicial():
    # Una tontería adicional para el proyecto, simula un progreso de carga y da una introducción 'chula' al programa
    texto = "  TBPG  "
    titulo = "The Best Password Generator"
    linea1 = "Bienvenido a "
    linea2 = "La mejor aplicación actual para generar contraseñas automáticamente"
    linea3 = "A continuación, se te pedirá que marques una serie de parámetros para diseñar tu contraseña"
    linea4 = "Si tienes dudas, quizás no sea tu mejor día, porque la aplicación es sencilla"
    linea4_1 = "Si tienes dudas, pregunta sin miedo :)"
    linea5 = "Gracias por utilizar "
    linea6 = "Tendrás que registrarte con un usuario único."

    textoNegro_fondoAzulClaro(texto.center(91, "="))

    print((linea1 + colorama.Fore.BLUE + titulo).center(91, " ") + colorama.Style.RESET_ALL)
    print(linea2.center(91, " "))
    time.sleep(2.5)
    print()

    for j in range(0, 3):
        print("\rCargando", end="")
        time.sleep(.5)
        for i in range(0, 3):
            print(".", end="")
            time.sleep(.5)
        # sys.stdout.write(CURSOR_UP_ONE)
        # sys.stdout.write(ERASE_LINE)
    print("\r¡Datos cargados con éxito!", end="")
    time.sleep(1.50)

    print("\r" + linea3)
    time.sleep(2.3)

    print(linea4, end="")
    time.sleep(2.9)
    print(
        "\r" + "EJEM, perdón, ha sonado demasiado " + colorama.Fore.RED + colorama.Style.BRIGHT + "hater" + colorama.Style.RESET_ALL + ", déjame volver a intentarlo.",
        end="")
    time.sleep(2.9)

    for j in range(0, 2):
        print("\rRecalibrando", end="")
        time.sleep(.5)
        for i in range(0, 3):
            print(".", end="")
            time.sleep(.5)
    print("\r" + linea4_1)
    time.sleep(1.5)
    print(linea5 + colorama.Fore.BLUE + titulo + colorama.Style.RESET_ALL)
    time.sleep(1.5)
    print(linea6)
    time.sleep(1.5)

    textoNegro_fondoAzulClaro("".center(91, "="))
    time.sleep(2)
    print()


def cargar_lista_usuarios():
    # Este método carga los datos del fichero datos.txt y genera dos diccionarios, uno tiene los datos del usuario y el otro
    # es la lista de usuarios, este último diccionario es el que es devuelto por este método

    # f = open("datos.txt", "r") -> lineas = f.readLines() me daba problemas, saltaba el error '_io.TextIOWrapper' object has no attribute 'readLines'
    # https://stackoverflow.com/questions/17569679/python-attributeerror-io-textiowrapper-object-has-no-attribute-split
    usuario = ""
    contrasenya = ""
    email = ""
    diccionario_usuarios = {}
    with open('datos.txt') as f:
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            usuario = datos[0]
            contrasenya = datos[1]
            email = datos[2]
            diccionario_user = dict(contrasenya=contrasenya, email=email)
            diccionario_usuarios[usuario] = diccionario_user

    # Datos que había creado de base
    diccionario2_dani = dict(contrasenya="_6Zq=*3'Rsk", email="dani.tamargo@ikasle.egibide.org")
    diccionario2_elena = dict(contrasenya="_4fas--'Rsk", email="elena.zamora@ikasle.egibide.org")
    diccionario2_kiana = dict(contrasenya="+58!¡asd-'Rsk", email="monicakiana@gmail.com")
    diccionario1_usuarios = dict(zip(["dani", "elena", "kiana"], [diccionario2_dani, diccionario2_elena, diccionario2_kiana]))
    # return diccionarios1_usuarios <- antes usaba estos datos fijos, después investigué un poco sobre ficheros
    return diccionario_usuarios


def lista_usuarios():
    # Este método muestra la lista completa de todos los usuarios con sus datos
    diccionario1_usuarios = cargar_lista_usuarios()

    n = 1
    print("Lista de usuarios:")
    for usuario in diccionario1_usuarios:
        print(colorama.Fore.LIGHTMAGENTA_EX + colorama.Style.BRIGHT, end="")
        print(str(n) + ". " + str(usuario).ljust(17, "-") + "->[", end="")
        print(colorama.Style.RESET_ALL, end="")
        x = 0
        for atributo in diccionario1_usuarios[str(usuario)]:
            if x == 0:
                print(colorama.Fore.LIGHTBLUE_EX + str(atributo) + ": " + colorama.Fore.RESET + str(diccionario1_usuarios[str(usuario)][atributo]), end="")
            else:
                # Esta comprobación de nombre y apellidos sólo se usará si implemento el pedir nombre y apellidos para guardarlo en los datos
                if str(atributo) == "nombre" or str(atributo) == "apellidos":
                    print(", " + colorama.Fore.LIGHTBLUE_EX + str(atributo) + ": " + colorama.Fore.RESET + str(diccionario1_usuarios[str(usuario)][atributo]).title(), end="")
                else:
                    print(", " + colorama.Fore.LIGHTBLUE_EX + str(atributo) + ": " + colorama.Fore.RESET + str(diccionario1_usuarios[str(usuario)][atributo]), end="")
            x += 1
        n += 1
        print(colorama.Fore.LIGHTMAGENTA_EX + "]." + colorama.Fore.RESET)
    print()


def usuario():
    # Este método sirve para crear un usuario, comprueba que no exista ya en los datos y cuando es único, devuelve usuario (el string)
    diccionario1_usuarios = cargar_lista_usuarios()

    existe = True
    usuario = ""
    # No hago restricciones de mínimo o máximo de longitud de usuario
    while existe:
        usuario = input("Introduce tu nombre de usuario (debe ser único): ")
        if usuario is not None and usuario != "":
            usuario = usuario.lower().strip()
            if usuario in diccionario1_usuarios.keys():
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                      + colorama.Style.RESET_ALL + " Ese nombre de usuario ya existe :(")
            else:
                print("Perfecto, el usuario " + colorama.Fore.LIGHTBLUE_EX + usuario + colorama.Fore.RESET + " está disponible.")
                existe = False
        else:
            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                  + colorama.Style.RESET_ALL + " No has introducido nada.")
        print()
    return usuario


def contrasenya():
    # Este método genera una contraseña aleatoria en base a los parámetros definidos, una vez confirmada, la devuelve

    # Mostramos el menú y pedimos que determine los parámetros a definir para crear la contraseña
    # Está en bucle puesto que al terminar de determinar dichos parámetros, se ofrece la opción de volver a determinarlos
    repetir = ""
    while repetir == "":
        print()
        print("Parámetros a definir:\n"
              "1. Longitud\n"
              "2. Minúsculas\n"
              "3. Mayúsculas\n"
              "4. Símbolos\n"
              "5. Números\n"
              "Empecemos.")
        print()

        # Define longitud. Será una variable de tipo int y utilizamos una función para comprobar que ha introducido un número
        longitud = ""
        print("1. Define la longitud de la contraseña.")
        while longitud == "":
            longitud = input("Longitud (mínimo 5): ")
            if FuncionesPR1.es_un_numero(longitud) == False:
                longitud = ""
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido un número.")
            else:
                if int(longitud) < 5:
                    longitud = ""
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Número demasiado pequeño!"
                          + colorama.Style.RESET_ALL + " Introduce un número más grande, ¡mínimo 5!.")
            print()

        # Define minúsculas. Será una variable tipo string o char donde guardaremos 's' o 'n'
        minusculas = ""
        print("2. Define si la contraseña tendrá minúsculas.")
        while minusculas == "":
            try:
                minusculas = input("¿Minúsculas? (s/n): ").lower()[0]
                if FuncionesPR1.si_o_no(minusculas) == False:
                    minusculas = ""
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                          + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
            except:
                minusculas = ""
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido ninguna respuesta. Debes introducir S o N para marcar Sí o No.")
            print()

        # Define mayúsculas. Será una variable tipo string o char donde guardaremos 's' o 'n'
        mayusculas = ""
        print("3. Define si la contraseña tendrá mayúsculas.")
        while mayusculas == "":
            try:
                mayusculas = input("¿Mayúsculas? (s/n): ").lower()[0]
                if FuncionesPR1.si_o_no(mayusculas) == False:
                    mayusculas = ""
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                          + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
            except:
                mayusculas = ""
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido ninguna respuesta. Debes introducir S o N para marcar Sí o No.")
            print()

        # Define símbolos. Será una variable tipo string o char donde guardaremos 's' o 'n'
        simbolos = ""
        print("4. Define si la contraseña tendrá símbolos.")
        while simbolos == "":
            try:
                simbolos = input("¿Símbolos? (s/n): ").lower()[0]
                if FuncionesPR1.si_o_no(simbolos) == False:
                    simbolos = ""
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                          + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
            except:
                simbolos = ""
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido ninguna respuesta. Debes introducir S o N para marcar Sí o No.")
            print()

        # Define números. Será una variable tipo string o char donde guardaremos 's' o 'n'
        numeros = ""
        print("5. Define si la contraseña tendrá números.")
        while numeros == "":
            try:
                numeros = input("¿Números? (s/n): ").lower()[0]
                if FuncionesPR1.si_o_no(numeros) == False:
                    numeros = ""
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                          + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
            except:
                numeros = ""
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido ninguna respuesta. Debes introducir S o N para marcar Sí o No.")
            print()

        # Resumen con los parámetros puestos
        textoNegro_fondoAzulClaro("  Resumen  ".center(45, "="))
        print(colorama.Fore.LIGHTBLUE_EX)
        print("Longitud: ".rjust(20, " ") + str(longitud))
        print("Minúsculas: ".rjust(20, " ") + ("Sí" if minusculas == "s" else "No"))
        print("Mayúsculas: ".rjust(20, " ") + ("Sí" if mayusculas == "s" else "No"))
        print("Símbolos: ".rjust(20, " ") + ("Sí" if simbolos == "s" else "No"))
        print("Números: ".rjust(20, " ") + ("Sí" if numeros == "s" else "No"))
        print(colorama.Style.RESET_ALL)
        textoNegro_fondoAzulClaro("".center(45, "="))
        print()

        if minusculas == "n" and mayusculas == "n" and simbolos == "n" and numeros == "n":
            print(
                "Lo sentimos, pero hemos detectado que has señalado que la contraseña no contendrá ningún tipo de caracter.")
            print("Eso es imposible, así que, por favor, rellena el menú de nuevo.")
        else:
            repetir = ""
            while repetir == "":
                repetir = input("¿Seguir adelante o repetir? (s/r): ")
                if repetir is not None and repetir != "":
                    repetir = repetir.lower()[0]
                    if repetir != "s" and repetir != "r":
                        print("Perdona, no te he entendido. Introduce 's' para seguir o 'r' para repetir.")
                        repetir = ""
                else:
                    repetir = ""
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                          + colorama.Style.RESET_ALL + " No has introducido ninguna respuesta. Debes introducir S o R para marcar Sí o Repetir.")
                print()
            if repetir == "r":
                repetir = ""



    #### He creado dos métodos para generar contraseñas, ambos son iguales pero uno de ellos tiene una particularidad
    #### El primero, simplemente genera una contraseña aleatoria donde sólo pueden aparecer los parámetros que haya definido
    # como sí, aunque no tienen porqué aparecer
    #### El segundo, genera una contraseña aleatoria igual que el primero, pero la genera una y otra vez hasta obtener una
    # en la que aparezcan (al menos una vez) sí o sí todos y cada uno de los parámetros definidos como sí
    #### Le damos la opción al usuario a escoger cual de los dos métodos utilizar
    #### Pero también, si el usuario ha seleccionado utilizar solo uno de los parámetros, omitimos el elegir entre ambas opciones
    # pues si solo puede utilizar, por ejemplo, minúsculas, dará igual que utilice el método que fuerza su aparición o no

    forzar = False
    parametros_usados = 0
    if minusculas == "s": parametros_usados += 1
    if mayusculas == "s": parametros_usados += 1
    if simbolos == "s": parametros_usados += 1
    if numeros == "s": parametros_usados += 1

    if parametros_usados > 1:
        respuesta = ""
        while respuesta == "":
            print("¿Qué método quieres usar para crear la contraseña?")
            print("a) Básico. No forzar la aparición de todos los parámetros marcados como 'sí'.")
            print("b) Recomendado. Forzar que aparezcan al menos una vez los parámetros marcados como 'sí'.")
            respuesta = input("Elige (a/b): ")
            if respuesta is not None:
                respuesta = respuesta.lower()[0]
                if respuesta == "a":
                    forzar = False
                elif respuesta == "b":
                    forzar = True
                else:
                    respuesta = ""
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                          + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
            else:
                respuesta = ""
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido ninguna respuesta. Debes introducir S o N para marcar Sí o No.")
            print()
    else:
        forzar = False

    # Generar contraseña
    repetir = True
    contrasenya = ""
    while repetir:
        print("Contraseña generada: ")
        if forzar:
            contrasenya = FuncionesPR1.generar_contrasenya_forzada(longitud, minusculas, mayusculas, simbolos, numeros)
        else:
            contrasenya = FuncionesPR1.generar_contrasenya(longitud, minusculas, mayusculas, simbolos, numeros)
        print(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + contrasenya + colorama.Style.RESET_ALL)
        print()
        print("Nivel de seguridad de la contraseña: ")
        seguridad_contrasenya = 0
        seguridad_contrasenya = int(FuncionesPR1.nivel_seguridad_contrasenya(contrasenya))
        if seguridad_contrasenya <= 7:
            print("Notas para mejorar la robustez:")
            if int(longitud) < 7:
                print("- Si la longitud es inferior a 7, la contraseña es propensa a ser débil.")
            if simbolos == "n":
                print("- El uso de símbolos aporta mucha robustez a la contraseña.")
            if simbolos == "n" and numeros == "n":
                print(
                    "- Utilizar solo caracteres alfabéticos hace que tu contraseña sea insegura. Además, seguramente no sea aceptada en muchas páginas.")
            if mayusculas == "n" or minusculas == "n":
                print("- No utilizas " + (
                    "minúsculas" if minusculas == "n" else "mayúsculas") + ". Intercalar minúsculas y mayúsculas es más seguro que no hacerlo.")
        print()
        respuesta = ""
        while respuesta == "":
            print("¿Generar de nuevo?")
            respuesta = input("Respuesta (s/n): ")
            if respuesta is not None and respuesta != "":
                respuesta = respuesta.lower()[0]
                if respuesta == "s" or respuesta == "n":
                    if respuesta == "n":
                        repetir = False
                else:
                    respuesta = ""
                    repetir = True
                    print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Ups!"
                          + colorama.Style.RESET_ALL + "No entiendo tu respuesta.")
            else:
                respuesta == ""
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido ninguna respuesta. Debes introducir S o N para marcar Sí o No.")
            print()

    return contrasenya


def email():
    # Este método sirve para pedir un email, comprueba que es válido y lo devuelve
    # Compruebo muchas cosas pero no establezco restricciones de longitud ni mínimas ni máximas
    # Iba a comprobar que no tuviera caracteres especiales (simbolos) pero un blog dice que son validos: http://preguntascojoneras.blogspot.com/2015/01/caracteres-validos-en-un-email.html
    valido = False
    email = ""
    while valido == False:
        email = input("Introduce tu email: ")
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

def guardar_usuario(usuario, contrasenya, email):
    # Este metodo muestra los datos que se van a guardar, y guarda el nuevo usuario en el fichero
    # Si hubiera que añadirlos al diccionario, sería así
    diccionario_datos_usuario = dict(contrasenya=contrasenya, email=email)
    diccionario_usuarios = cargar_lista_usuarios()
    diccionario_usuarios[usuario] = diccionario_datos_usuario

    print("Datos que se van a guardar:")
    print("Usuario: {0}".format(usuario))
    print("Contraseña: {0}".format(contrasenya))
    print("Email: {0}".format(email))
    print()

    # Pero yo lo añado al fichero
    # https://www.guru99.com/reading-and-writing-files-in-python.html
    linea = usuario + "," + contrasenya + "," + email

    f = open("datos.txt", "a+") #<- a significa que es para añadir (append) líneas al final, sin necesidad de sobreescribir
    f.write(linea + "\n")
    f.close()


def enviar_email(usuario, contrasenya, email):
    # Este método utiliza mi cuenta de correo del instituto para enviar un correo al email introducido con todos sus datos
    print("Intentando mandar el correo...", end="")
    # https://realpython.com/python-send-email/
    port = 465
    password = "JxGEWWue"
    gmail = "daniel.tamargo@ikasle.egibide.org"

    # Está así para que aparezca bien quien lo envía, cual es el asunto y el cuerpo del email
    mensaje ="""\
    From: The Best Password Generator\nSubject: Nuevo usuario creado\n\n   Este correo confirma que se han guardado los siguientes datos:
    - Usuario: {0}
    - Contrasenya: {1}
    - Email: {2}
    Se han guardado en nuestra base de datos, si quieres cambiar cualquier dato, contacta con nosotros.
    
    Este correo ha sido enviado por The Best Password Generator.""".format(usuario, contrasenya, email)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(gmail, password)

        server.sendmail(gmail, email, mensaje)

    print(colorama.Fore.LIGHTGREEN_EX + "\r¡Correo enviado!" + colorama.Fore.RESET)


def preguntar_mandar_email(usuario, contrasenya, email):
    # Este método existe para dar la opción de enviar o no enviar el email, por ejemplo si has puesto una direccion
    # falsa o no existente, seleccionas no enviarlo y no habrá problemas
    mandarlo = False
    respuesta = input("¿Enviar un email al correo que has indicado con los datos guardados? (s/n): ")
    if respuesta != "" and respuesta is not None:
        respuesta = respuesta.lower()[0]
        if respuesta == "s" or respuesta == "n":
            if respuesta == "s":
                enviar_email(usuario, contrasenya, email)
            else:
                print(
                    "Perfecto, entonces no mandaremos el email.")
        else:
            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                  + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
    else:
        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
              + colorama.Style.RESET_ALL + " No has introducido un nada :(")


def evitar_caracteres_no_soportados_por_ascii(cadena):
    # Este método sustituye los caracteres que darían problemas al enviar el email: ñ ¡ ¿

    dic_correciones = {"ñ": "n", 
                       "¡": "!", 
                       "¿": "?",
                       "´": "`",
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
