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
print("Ejercicio 12")
funciones.esPalindromo(funciones.recogerPalabra())
print()

# Ejercicio 13
print("Ejercicio 13")
funciones.fibonacci(funciones.recogerNumero())
print()

# Ejercicio 14
print("Ejercicio 14")

print()
