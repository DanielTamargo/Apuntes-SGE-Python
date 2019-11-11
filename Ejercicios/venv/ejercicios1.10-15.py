import funciones

# Ejercicio 11
print("Ejercicio 11")
print("¿Cuál es la capital de Francia?")
print("a) París\n"
      "b) Nimes\n"
      "c) Montpellier\n"
      "d) Lyon")
letra = input("Respuesta: ").lower()[0] # <- lower() = toLowerCase / [0] = charAt(0)
if letra == "a":
    print("¡Has acertado!")
else:
    print("Has fallado")
print()

# Ejercicio 12
print("Ejercicio 12 - Palíndromo")
funciones.esPalindromo(funciones.recogerPalabra())
print()

# Ejercicio 13
print("Ejercicio 13 - Fibonacci")
funciones.fibonacci(funciones.recogerNumero())
print()

# Ejercicio 14
print("Ejercicio 14 - Naciste en el año xxxx")
funciones.anyoNacimiento()
print()

# Ejercicio 15
print("Ejercicio 15 - Tirada de dados")
tirar = True
while tirar:
    funciones.tiradaDados()
    eleccion = input("¿Tirar los dados de nuevo? (S/N): ").lower()
    if eleccion == "n" or eleccion == "no":
        tirar = False