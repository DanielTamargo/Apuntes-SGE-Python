import datetime
import random

def recogerNombre():
    return input("Escribe tu nombre: ")

def recogerEdad():
    return input("Escribe tu edad: ")

def recogerNumero():
    return int(input("Introduce un número: "))

def cualEsMayor(a, b):
    if a> b:
        print(a,"es mayor que",b)
    elif b > a:
        print(b,"es mayor que",a)
    else:
        print(a,"es igual a",b)

def estaEntre0y10(a):
    if a >= 0 and a <= 10:
        print("Sí,",a,"está entre 0 y 10.")
    else:
        print("No,",a,"no está entre 0 y 10.")

def esPrimo(a):
    esPrimo = True
    for i in range(2,a):
        if esPrimo:
            if a % i == 0:
                esPrimo = False
    if esPrimo:
        print(a,"es un número primo.")
    else:
        print(a,"no es un número primo.")

def parImpar(a):
    x = "impar"
    if a % 2 == 0:
        x = "par"
    print(a,"es",x + ".")

def numerosImparesDel1al200():
    # Ejercicio 9, con While
    n = 2
    lista_numeros = "1"
    while n <= 200:
        if n % 2 != 0:
            lista_numeros += ", " + str(n)
        n+=1
    print("Lista de números impares del 1 al 100 (con While):")
    print(lista_numeros)

    # Ejercicio 10, con For
    lista_numeros = "1"
    for i in range(2,201):
        if i % 2 != 0:
            lista_numeros += ", " + str(i)
    print("Lista de números impares del 1 al 100 (con For):")
    print(lista_numeros)

def recogerPalabra():
    return input("Escribe una palabra: ")

def esPalindromo(a):
    longitud_texto = len(a)
    x = longitud_texto - 1
    palindromo = True
    for i in range(0,longitud_texto):
        if palindromo:
            if a[i] != a[x]:
                palindromo = False
            x -= 1
    if palindromo:
        print(a,"es palíndromo")
    else:
        print(a,"no es palíndromo")

def fibonacci(n):
    a = 0
    b = 1
    lista_numeros = "0, 1"
    while b < n:
        if (a + b) < n:
            lista_numeros += ", " + str(a + b)
        b += a
        a = b - a
    print("Lista de números fibonacci desde 0 hasta",n)
    print(lista_numeros)

def anyoNacimiento():
    nombre = input("Escribe tu nombre: ")
    edad = int(input("Escribe tu edad: ")) #falta aprender a comprobar excepciones, ejemplo, si no introduce un numero

    if edad < 1:
        print("Ja, ja, ja, me parto contigo")
    else:
        mes = int(input("Escribe el número del mes en el que naciste (ejemplo: 9): "))
        dia = int(input("Escribe el día en el que naciste (ejemplo: 23): "))
        anyo = datetime.datetime.now().year
        month = datetime.datetime.now().month
        anyo -= edad
        cumple = False
        if mes > month:
            anyo -= 1
        elif mes == month:
            day = datetime.datetime.now().day
            if dia > day:
                anyo -= 1
            elif dia == day:
                cumple = True

        print("Hola",nombre + ", naciste en el año",anyo)
        if cumple:
            print("Enhorabuena, ¡hoy es tu cumple!")

def tiradaDados():
    print("Dado 1:",random.randint(1,6))
    print("Dado 2:", random.randint(1, 6))