import os
from datetime import date
from datetime import datetime
import Archivos.Funciones.CargarDatos as cd
import Archivos.Clases as Clases

estatus = Clases.EstatusProducto.Activo

print(type(estatus))
print(type(estatus.name))
print(estatus.name)

precio = 8.8
print(precio)
f = open("Datos/test.txt", "w+")
f.write(str(precio))
f.close()


