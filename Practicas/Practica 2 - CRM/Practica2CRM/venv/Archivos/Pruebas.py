import datetime
import Clases
import Funciones as Fun
import time
import Archivos.MainEjecuciones as ME

a = "hola"
b = "quetal"
c = "adios"
lista1 = [a, b, c]
print(lista1)
lista2 = [c]
lista3 = [a, b]
for elemento in lista2:
    lista1.remove(elemento)
print(lista1)

if c in lista3:
    lista3.remove(c)
if a in lista3:
    lista3.remove(a)
print(lista3)
print()
