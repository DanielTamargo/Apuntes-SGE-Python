import funciones
import datetime
import random

print("Ejercicio 15 - Tirada de dados")
tirar = True
while tirar:
    funciones.tiradaDados()
    eleccion = input("¿Tirar los dados de nuevo? (S/N): ").lower()
    if eleccion == "n" or eleccion == "no":
        tirar = False
print()


# a = "hola"
# print(len(a)) #sacar longitud string
# print(a[1]) #sacar letra en concreto
# print(a[1] == "o") # True