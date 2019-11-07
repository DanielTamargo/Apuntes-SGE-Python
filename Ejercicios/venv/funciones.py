import datetime

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

def numerosImparseDel1al200():
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
    c = 1
    lista_numeros = "0, 1"
    while b < n:
        if (a + b) < n:
            lista_numeros += ", " + str(a + b)
        c = a
        a = b
        b += c
    print("Lista de números fibonacci desde 0 hasta",n)
    print(lista_numeros)
