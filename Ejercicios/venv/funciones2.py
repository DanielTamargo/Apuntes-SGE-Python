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

# Saca una lista con todos los números capicúas (separados por 2 guiones) hasta el número que le pases
# Recurre constantemente a la función capicua
def lista_capicuas(numero):
    lista_numeros = "1"
    for i in range(2, (numero + 1)):
        if capicua(i):
            lista_numeros = lista_numeros + "--" + str(i)
    print("Lista de capicúas desde 1 hasta",numero)
    print(lista_numeros)