import funciones
import datetime
import random

numero = 1919191
numero = str(numero)
print(numero)
print(len(numero))
x = len(numero) - 1
print(x)
print(numero[0],numero[1],numero[2])
es_capicua = True
for i in range(0, (len(numero) - 1)):
    if numero[i] != numero[x]:
        es_capicua = False
        i = len(numero)
    x -= 1
print(es_capicua)

# a = "hola"
# print(len(a)) #sacar longitud string
# print(a[1]) #sacar letra en concreto
# print(a[1] == "o") # True