import random
import colorama

def es_un_numero(valor):
    try:
        valor = int(valor)
        if valor is not None:
            return True
        else:
            return False
    except:
        return False


def si_o_no(texto):
    if texto == "s" or texto == "n":
        return True
    else:
        return False


def generar_contrasenya(longitud, minusculas, mayusculas, simbolos, numeros):
    # Este método genera una contraseña cumpliendo con los parámetros definidos
    # longitud es tipo int y determina la longitud de la contraseña
    # minusculas, mayusculas, simbolos y numeros son tipo string o char y determinan si se usan o no ('s' o 'n')

    abc = "abcdefghijklmnñopqrstuvwxyz" # Cuidado con la ñ si utilizas codificación tipo ascii, un método la convierte si es necesario
    nums = "1234567890"
    simbs = "!¡?¿=_-+*^'"  # Se podrían añadir más, ¡ y ¿ dan problemas por ascii, pero un metodo los convierte cuando es necesario

    contrasenya = ""

    while len(contrasenya) < int(longitud):
        x = random.randint(1, 4)
        if x == 1 and minusculas == "s":
            x = random.randint(0, (len(abc) - 1))
            contrasenya += abc[x]
        elif x == 2 and mayusculas == "s":
            x = random.randint(0, (len(abc) - 1))
            contrasenya += abc.upper()[x]
        elif x == 3 and simbolos == "s":
            x = random.randint(0, (len(simbs) - 1))
            contrasenya += simbs[x]
        elif x == 4 and numeros == "s":
            x = random.randint(0, (len(nums) - 1))
            contrasenya += nums[x]


    return contrasenya


def generar_contrasenya_forzada(longitud, minusculas, mayusculas, simbolos, numeros):
    # Este método es igual que generar_contrasenya pero en este caso,
    # fuerza el insertar al menos una vez los parámetros definidos como sí

    abc = "abcdefghijklmnñopqrstuvwxyz" # Cuidado con la ñ si utilizas codificación tipo ascii, un método la convierte si es necesario
    nums = "1234567890"
    simbs = "!?=_-+*^'¡¿"  # Se podrían añadir más, ¡ y ¿ dan problemas por ascii, pero un metodo los convierte cuando es necesario

    # Utilizo estas variables boolean para determinar si ya han aparecido, así, realizaré un bucle que genera una
    # contraseña tras otra hasta crear una que utilice todos los elementos
    min = False
    may = False
    sim = False
    num = False

    # El bucle se repetirá mientras alguno sea falso, los parámetros definidos como 'no' serán verdaderos, y los parámetros
    # que aparezcan serán verdadero también
    contrasenya = ""
    while min == False or may == False or sim == False or num == False:
        # Reseteamos por si el bucle reinicia
        min = False
        may = False
        sim = False
        num = False

        # Marco como True los parámetros que no van a aparecer, puesto que si no, el bucle sería infinito, ya que el bucle
        # se realiza hasta que todas son True (True quiere decir que ya aparecen, pero como estos parámetros están definidos
        # como 'no', no pueden aparecer, entonces en este caso True quiere decir que no los tenga en cuenta)
        if minusculas == "n":
            min = True
        if mayusculas == "n":
            may = True
        if simbolos == "n":
            sim = True
        if numeros == "n":
            num = True

        contrasenya = ""

        while len(contrasenya) < int(longitud):
            x = random.randint(1, 4)
            if x == 1 and minusculas == "s":
                x = random.randint(0, (len(abc) - 1))
                contrasenya += abc[x]
                min = True
            elif x == 2 and mayusculas == "s":
                x = random.randint(0, (len(abc) - 1))
                contrasenya += abc.upper()[x]
                may = True
            elif x == 3 and simbolos == "s":
                x = random.randint(0, (len(simbs) - 1))
                contrasenya += simbs[x]
                sim = True
            elif x == 4 and numeros == "s":
                x = random.randint(0, (len(nums) - 1))
                contrasenya += nums[x]
                num = True


    return contrasenya


def nivel_seguridad_contrasenya(contrasenya):
    #### Este método determinará el nivel de seguridad de una contraseña
    #### Mostrará a través de unos prints las evaluaciones por cada parámetro y finalmente devolverá
    # el nivel (será un int) de la contraseña
    #### El sistema seguido está en el archivo notas.txt (lo encontrarás en la misma ruta que este archivo)

    # Para dar una ayuda visual, la robustez de la contraseña se señalará también por colores
    print("Sistema por colores: "
          + colorama.Fore.RED + "muy débil" + colorama.Fore.RESET + " - "
          + colorama.Fore.LIGHTRED_EX + "débil" + colorama.Fore.RESET + " - "
          + colorama.Fore.YELLOW + "moderada" + colorama.Fore.RESET + " - "
          + colorama.Fore.LIGHTBLUE_EX + "fuerte" + colorama.Fore.RESET + " - "
          + colorama.Fore.GREEN + "muy fuerte" + colorama.Fore.RESET)
    print()

    contrasenya = str(contrasenya)
    puntuacion_seguridad = 0

    puntuacion_longitud = 0
    # Longitud (débil, moderado, fuerte o muy fuerte)
    if len(contrasenya) < 7:
        puntuacion_longitud = 1
    elif len(contrasenya) < 9:
        puntuacion_longitud = 2
    elif len(contrasenya) < 13:
        puntuacion_longitud = 3
    else:
        puntuacion_longitud = 4

    print("Seguridad longitud: ", end="")
    if puntuacion_longitud == 1:
        print(colorama.Fore.LIGHTRED_EX + "débil")
    elif puntuacion_longitud == 2:
        print(colorama.Fore.YELLOW + "moderada")
    elif puntuacion_longitud == 3:
        print(colorama.Fore.LIGHTBLUE_EX + "fuerte")
    elif puntuacion_longitud == 4:
        print(colorama.Fore.GREEN + "muy fuerte")
    print(colorama.Fore.RESET, end="")

    puntuacion_seguridad += puntuacion_longitud

    # Capitalización (muy débil, débil o fuerte):
    numero_de_minusculas = 0
    numero_de_mayusculas = 0
    abc = "abcdefghijklmnñopqrstuvwxyz"

    for i in range(len(contrasenya)):
        if contrasenya[i] in abc:
            numero_de_minusculas += 1
        elif contrasenya[i] in abc.upper():
            numero_de_mayusculas += 1

    puntuacion_capitalizacion = 0
    if numero_de_minusculas >= 3 and numero_de_mayusculas == 1:
        puntuacion_capitalizacion = 1
    elif numero_de_minusculas >= 3 and numero_de_mayusculas > 1:
        puntuacion_capitalizacion = 2
    elif numero_de_mayusculas >= 3 and numero_de_minusculas == 1:
        puntuacion_capitalizacion = 1
    elif numero_de_mayusculas >= 3 and numero_de_minusculas > 1:
        puntuacion_capitalizacion = 2

    print("Seguridad capitalización: ", end="")
    if puntuacion_capitalizacion == 0:
        print(colorama.Fore.RED + "muy débil" + (
            " (sólo has usado minúsculas)" if numero_de_minusculas == 0 else "") + (" (sólo has usado minúsculas)" if numero_de_mayusculas == 0 else ""))
    elif puntuacion_capitalizacion == 1:
        print(colorama.Fore.LIGHTRED_EX + "débil")
    elif puntuacion_capitalizacion == 2:
        print(colorama.Fore.LIGHTBLUE_EX + "fuerte")
    print(colorama.Fore.RESET, end="")

    puntuacion_seguridad += puntuacion_capitalizacion

    # Símbolos (débil, moderado, fuerte o muy fuerte)
    simbs = "!?=_-+*^'¡¿"
    numero_de_simbolos = 0

    for i in range(len(contrasenya)):
        if contrasenya[i] in simbs:
            numero_de_simbolos += 1

    puntuacion_simbolos = 0
    if numero_de_simbolos > 0:
        if numero_de_simbolos == 1:
            puntuacion_simbolos = 2
        elif numero_de_simbolos == 2:
            puntuacion_simbolos = 3
        else:
            puntuacion_simbolos = 4

    print("Seguridad símbolos: ", end="")
    if puntuacion_simbolos == 0:
        print(colorama.Fore.LIGHTRED_EX + "débil")
    elif puntuacion_simbolos == 2:
        print(colorama.Fore.YELLOW + "moderado")
    elif puntuacion_simbolos == 3:
        print(colorama.Fore.LIGHTBLUE_EX + "fuerte")
    elif puntuacion_simbolos == 4:
        print(colorama.Fore.GREEN + "muy fuerte")
    print(colorama.Fore.RESET, end="")

    puntuacion_seguridad += puntuacion_simbolos

    # Números (débil, moderado, fuerte o muy fuerte)
    nums = "1234567890"
    numero_de_numeros = 0

    for i in range(len(contrasenya)):
        if contrasenya[i] in nums:
            numero_de_numeros += 1

    puntuacion_numeros = 0

    if numero_de_numeros == 1:
        puntuacion_numeros = 1
    elif numero_de_numeros == 2:
        puntuacion_numeros = 2
    elif numero_de_numeros > 2:
        puntuacion_numeros = 3

    print("Seguridad números: ", end="")
    if puntuacion_numeros == 0:
        print(colorama.Fore.LIGHTRED_EX + "débil")
    elif puntuacion_numeros == 1:
        print(colorama.Fore.YELLOW + "moderado")
    elif puntuacion_numeros == 2:
        print(colorama.Fore.LIGHTBLUE_EX + "fuerte")
    elif puntuacion_numeros == 3:
        print(colorama.Fore.GREEN + "muy fuerte")
    print(colorama.Fore.RESET, end="")

    print()
    puntuacion_seguridad += puntuacion_numeros

    # Puntuación final
    print(colorama.Fore.LIGHTBLUE_EX + "Seguridad de la contraseña: ", end="")
    if puntuacion_seguridad == 0:  # <- nunca se va a dar mientras la longitud mínima de la contraseña sea 5
        print(colorama.Fore.LIGHTMAGENTA_EX + "insegura, obligatorio mejorarla")
    elif 1 <= puntuacion_seguridad <= 3:
        print(colorama.Fore.RED + "muy débil")
    elif 4 <= puntuacion_seguridad <= 6:
        print(colorama.Fore.LIGHTRED_EX + "débil")
    elif puntuacion_seguridad == 7:
        print(colorama.Fore.YELLOW + "moderada")
    elif puntuacion_seguridad == 8 and puntuacion_seguridad == 9:
        print(colorama.Fore.LIGHTBLUE_EX + "fuerte")
    else:
        print(colorama.Fore.GREEN + "muy fuerte")
    print(colorama.Fore.RESET, end="")

    return puntuacion_seguridad



# Este último método es un intento de borrar líneas que ya se hubiesen mostrado en pantalla, pero no funciona
#print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
def intentando_borrar_lineas():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    # Varios intentos de borrar líneas atrás, pero no funciona, solo borra la última
    # Finalmente utilizo \r para reescribir la línea (es necesario utilizar end = "" para que no haya salto de línea y así poder sobreescribirla)
    for i in range(10):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
        # print("\r\r", end = "")