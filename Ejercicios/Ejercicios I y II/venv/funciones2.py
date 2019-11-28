import random
import sys

# Devuelve un boolean True or False en base a si el número que le pasas es capicúa o no
# Número capicúa = True, número no capicúa = False
def capicua(numero):
    numero = str(numero)
    x = len(numero) - 1
    es_capicua = True
    for i in range(0, (len(numero) - 1)):
        if numero[i] != numero[x]:
            es_capicua = False
            i = len(numero)
        x -= 1
    return es_capicua

# Devuelve un boolean, True si el número es par y False si es impar
def es_par(numero):
    b_es_par = False
    if numero % 2 == 0:
        b_es_par = True
    return b_es_par

# Devuelve un boolean, True si el número es primo y False si no lo es
def es_primo(numero):
    b_es_primo = True
    for i in range(2, (numero - 1)):
        if numero % i == 0:
            b_es_primo = False
    return b_es_primo

# Saca una lista con todos los números capicúas (separados por 2 guiones) hasta el número que le pases
# Recurre constantemente a la función capicua
def lista_capicuas(numero):
    lista_numeros = "1"
    for i in range(2, (numero + 1)):
        if capicua(i):
            lista_numeros = lista_numeros + "--" + str(i)
    print("Lista de capicúas desde 1 hasta",numero)
    print(lista_numeros)

# Recibe un prétamo y unos plazos en los que repartir dicho préstamo
# prestamo es float, plazos es int
def prestamo_en_plazos(prestamo, plazos):
    x = prestamo / plazos
    for i in range(1,plazos+1):
        prestamo = prestamo - x
        print("Plazo",str(i) +", falta por pagar:", prestamo)

# Recibe un número y saca una lista de asteriscos en forma de escalera
def escalera_asteriscos(numero):
    x = ""
    for i in range(0, numero):
        x += "*"
        print(x)

# Recibe un número y saca una lista de numeros pares en forma de escalera
def escalera_pares(numero):
    for i in range(1, numero + 1):
        texto = ""
        x = i * 2
        while (x > 0):
            texto += " " + str(x)
            x -= 2
        print(texto)

# Recibe un número y saca su tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print("{0} * {1} = {2}".format(numero, i, (i * numero)))

# Recibe un número y saca una pirámide entera de asteriscos
def piramide_entera(numero):

    n_caracteres_por_lado = 1 + (2 ** (numero - 1))
    n_espacios_tronco = -5
    for i in range (0, (numero)):
        # Bastaría con esta linea: print(' '*(numero-i-1) + '*'*(2*i+1)
        if i == 0:
            n_asteriscos = 1
        else:
            n_asteriscos = 1 + (2 ** i)
        linea = ""
        for j in range(0, ((n_caracteres_por_lado - n_asteriscos) // 2)):
            if i == 1 and n_espacios_tronco == -5:
                n_espacios_tronco = (n_caracteres_por_lado - n_asteriscos) // 2
            linea += " "
        for j in range(0, n_asteriscos):
            linea += "*"
        for j in range(0, ((n_caracteres_por_lado - n_asteriscos) // 2)):
            linea += " "
        print(linea)
    for i in range(0, 2):
        linea = ""
        for j in range(0, n_espacios_tronco):
            linea += " "
        linea += "*"
        linea += " "
        linea += "*"
        if i == 0:
            linea += "  y si en vez de ser una pirámide, es un árbol(?)"
        if i == 1:
            linea += "  <--- esto es el tronco (má o meno)"
        print(linea)
    linea = ""
    for i in range(0, n_espacios_tronco):
        linea += " "
    linea += "***"
    print(linea)

# Crea una lista de 100 números y muestra solo los pares
def lista_100_numeros_muestra_pares():
    v_lista = []
    for i in range(1, 101):
        v_lista.append(i)

    str_lista = "Lista de números pares: "
    primero = True
    for numero in v_lista:
        if numero % 2 == 0:
            if not primero:
                str_lista += ", " + str(numero)
            else:
                str_lista += str(numero)
                primero = False
    print(str_lista)

# Crea una lista de 100 números, y luego crea otras dos listas guardando en cada una los impares y los pares
def dividir100endoslistas():
    v_lista = []
    for i in range(1, 101):
        v_lista.append(i)
    v_lista_pares = []
    v_lista_impares = []

    for numero in v_lista:
        if numero % 2 == 0:
            v_lista_pares.append(numero)
        else:
            v_lista_impares.append(numero)

    primero = True
    str_lista = ""
    print("Lista de pares: ")
    for numero in v_lista_pares:
        if not primero:
            str_lista += ", " + str(numero)
        else:
            str_lista += str(numero)
            primero = False
    print(str_lista)

    primero = True
    str_lista = ""
    print("Lista de impares: ")
    for numero in v_lista_impares:
        if not primero:
            str_lista += ", " + str(numero)
        else:
            str_lista += str(numero)
            primero = False
    print(str_lista)

# Crea una lista con las asignaturas del 2º Curso de DAM y la muestra
def lista_asignaturas_dam():
    v_lista = ["Lenguaje de Marcas", "Sistemas de Gestión Empresarial", "Sistemas Informáticos", "Desarrollo de Interfaces",
               "Ingles Técnico", "Programación Multimedia y Dispositivos Móviles"]
    linea = "El curso 2º de DAM tiene las siguientes asignaturas: "
    primero = True
    for asignatura in v_lista:
        if not primero:
            linea += ", " + asignatura
        else:
            linea += asignatura
            primero = False
    linea += "."
    print(linea)

# Crea una lista con números aleatorios, de forma desordenada, va mostrando los números de menor a mayor
def lista_desordenada_demenoramayor(n):
    v_lista = []

    for i in range(0, n):
        v_lista.append(random.randint(1,99))

    print("Lista de números generada: ")
    linea = ""
    primero = True
    for numero in v_lista:
        if not primero:
            linea += ", " + str(numero)
        else:
            linea += str(numero)
            primero = False
    print(linea)

    print("Lista de números reordenada de menor a mayor: ")
    linea = ""
    primero = True
    minimo = 101
    ultimo = -1
  # FALTA POR ACABAR ESTA PARTE
    for i in range(0, n):
        minimo = 101
        for numero in v_lista:
            if minimo > numero > ultimo:
                minimo = numero

        if not primero:
            linea += ", " + str(minimo)
        else:
            linea += str(minimo)
            primero = False
        ultimo = minimo
    print(linea)




