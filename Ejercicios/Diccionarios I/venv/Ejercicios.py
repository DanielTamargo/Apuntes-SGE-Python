# Quitar Tildes utilizando un Diccionario
tildes = {'á' : 'a', 'à' : 'a'}
palabra = 'hálà'
print("Antes de quitar:", palabra)
for i in range(0, len(palabra)):
    if palabra[i] in tildes.keys():
        palabra = palabra.replace(palabra[i], tildes[palabra[i]])
print("Después de quitar:", palabra)

import funciones

# Funciones en un Diccionario
diccionario_funciones = {'a' : funciones.es_par, 'b' : funciones.es_primo}

eleccion = input("Introduce 'a' o 'b': ").lower()

numero = 11

if diccionario_funciones[eleccion](numero):
    if eleccion == "a":
        print("Es par")
    else:
        print("Es primo")
else:
    if eleccion == "a":
        print("Es impar")
    else:
        print("No es primo")
