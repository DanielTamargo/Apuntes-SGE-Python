import funciones

# Ejercicio 6
print("Ejercicio 6 - Entre 0 y 10")
funciones.estaEntre0y10(funciones.recogerNumero())
print()

# Ejercicio 7
print("Ejercicio 7 - Es primo")
funciones.esPrimo(funciones.recogerNumero())
print()

# Ejercicio 8
print("Ejercicio 8 - Par o impar + primo")
a = funciones.recogerNumero()
funciones.parImpar(a)
funciones.esPrimo(a)
print()

# Ejercicio 9 y 10 (9 con While, 10 con For, ambos pasos en la función
print("Ejercicio 10 - Impares Del 1 al 200")
funciones.numerosImparesDel1al200()