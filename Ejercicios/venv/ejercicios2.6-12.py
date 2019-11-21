import funciones2
import funciones

# Ejercicio 6
print("Ejercicio 6 - Capicúa, par/impar, primo")
n = int(input("Introduce un número: "))
if funciones2.capicua(n):
    print("- Es capicúa")
else:
    print("- No es capicúa")
if funciones2.es_par(n):
    print("- Es par")
else:
    print("- Es impar")
if funciones2.es_primo(n):
    print("- Es primo")
else:
    print("- No es primo")
print()

# Ejercicio 7
print("Ejercicio 7 - Pirámide completa (¿o quizás árbol?)")
n = int(input("Introduce un número: "))
funciones2.piramide_entera(n)
print()

# Ejercicio 8
print("Ejercicio 8 - Crear lista, añadir 100 números mostrando solo pares")
funciones2.lista_100_numeros_muestra_pares()
print()

# Ejercicio 9
print("Ejercicio 9 - Crear lista, añadir 100 números, dividir en dos listas (pares e impares), mostrar ambas listas")
funciones2.dividir100endoslistas()
print()

# Ejercicio 10
print("Ejercicio 10 - Palíndromo (¿repetido?)")
funciones.esPalindromo(funciones.recogerPalabra())
print()

# Ejercicio 11
print("Ejercicio 11 - Lista asignaturas")
funciones2.lista_asignaturas_dam()
print()

# Ejercicio 12
print("Ejercicio 12 - Lista con numeros desordenados, mostrar de menor a mayor")
n = int(input("Introduce cuantos números quieres que tenga la lista: "))
funciones2.lista_desordenada_demenoramayor(n)