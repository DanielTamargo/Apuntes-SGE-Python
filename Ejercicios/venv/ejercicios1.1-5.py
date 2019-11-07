import funciones

# Ejercicio 1
print("Ejercicio 1")
print("Hola Mundo")
print()

# Ejercicio 2
print("Ejercicio 2")
nombre = "Dani"
print("Hola",nombre)
print()

# Ejercicio 3
print("Ejercicio 3")
''' Forma en dos pasos, guardar nombre y mostrarlo
nombre = funciones.recogerNombre()
print("Hola",nombre) <- al concatenar strings añade un espacio automaticamente?
'''
print("Hola",funciones.recogerNombre())
print()

# Ejercicio 4
print("Ejercicio 4")
print("Hola",funciones.recogerNombre() + ", tienes",funciones.recogerEdad(),"años.")
print()

# Ejercicio 5
print("Ejercicio 5")
funciones.cualEsMayor(funciones.recogerNumero(), funciones.recogerNumero())
print()
