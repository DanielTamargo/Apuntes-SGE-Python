import funciones2

# Ejercicio 1
print("Ejercicio 1 - Lista de capicúas")
n = int(input("Introduce un número positivo para sacar una lista de capicúas: "))
funciones2.lista_capicuas(n)
print()
# Comparar lista con lista invertida: lista==lista[::-1]

# Ejercicio 2
print("Ejercicio 2 - Préstamos")
prestamo = float(input("Cantidad préstamo: "))
plazos = int(input("Plazos: "))
funciones2.prestamo_en_plazos(prestamo, plazos)
print()

# Ejercicio 3
print("Ejercicio 3 - Escalera asteriscos")
n = int(input("Introduce número de filas: "))
funciones2.escalera_asteriscos(n)
print()

# Ejercicio 4
print("Ejercicio 4 - Escalera pares")
n = int(input("Introduce número de filas: "))
funciones2.escalera_pares(n)
print()

# Ejercicio 5
print("Ejercicio 5 - Tabla de multiplicar")
n = -1
while n < 1 | n > 10:
    n = int(input("Introduce un número del 1 al 10"))
funciones2.tabla_multiplicar(n)
