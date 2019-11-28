import funciones

# Ejercicio 1
print("Ejercicio 1 - Hola Mundo")
print("Hola Mundo")
print()

# Ejercicio 2
print("Ejercicio 2 - Nombre")
nombre = "Dani"
print("Hola",nombre)
print()

# Ejercicio 3
print("Ejercicio 3 - Pedir nombre")
''' Forma en dos pasos, guardar nombre y mostrarlo
nombre = funciones.recogerNombre()
print("Hola",nombre) <- al concatenar strings añade un espacio automaticamente?
'''
print("Hola",funciones.recogerNombre())
print()

# Ejercicio 4
print("Ejercicio 4 - Nombre + edad")
print("Hola",funciones.recogerNombre() + ", tienes",funciones.recogerEdad(),"años.")
print()

# Ejercicio 5
print("Ejercicio 5 - Mayor o menor")
funciones.cualEsMayor(funciones.recogerNumero(), funciones.recogerNumero())
