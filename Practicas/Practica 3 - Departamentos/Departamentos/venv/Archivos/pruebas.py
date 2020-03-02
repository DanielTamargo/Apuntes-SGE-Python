import os
from datetime import date
from datetime import datetime
import Archivos.Funciones.CargarDatos as cd

usuarios = cd.cargar_usuarios()
print(usuarios["dani"])
while True:
    num = input("Número: ")
    print("isdigit   -> " + str(num.isdigit()))
    print("isnumeric -> " + str(num.isnumeric()))
    print("isdecimal -> " + str(num.isdecimal()))
    print("isalnum   -> " + str(num.isalnum()))
    print()

