import csv
from datetime import datetime

# Función para crear los logs
def generarLog(usuario):
    print("Generando log")
    ahora = datetime.now()
    datos = [str(usuario), str(ahora)]
    with open('Datos/user_logs.csv', 'a+', newline='') as f:
        # campos = ['Usuario', 'Fecha']
        writer = csv.writer(f)
        writer.writerow(datos)
        print("Log generado")
    print()

# Función para guardar una línea con los datos del usuario que haya iniciado sesión
def usuarioLoggeado(usuario, contrasenya, mantener_sesion):
    # Datos login (si la casilla está marcada, se ejecutará el login automáticamente la próxima vez)
    f = open("Datos/user_logged_in.txt", "w+")
    f.write("{0},{1},{2}".format(str(usuario), str(contrasenya), str(mantener_sesion)))
    f.close()

# Función para cargar el usuario loggeado
def cargarUsuarioLoggeado():
    f = open("Datos/user_logged_in.txt", "r+")
    datos = f.read()
    if len(datos) > 2:
        datos = datos.split(",")
        return str(datos[0])

# Función que comprueba si existen datos de un usuario que marcase la casilla de Mantener Sesión Iniciada
def comprobar_inicio_sesion_automatico():

    with open("Datos/user_logged_in.txt", "r+") as f:
        datos = f.read()
        if len(datos) > 2:
            datos = datos.split(",")
            if datos[2] == "1":
                return True
            else:
                return False
        else:
            return False
    return False

# Función que elimina la línea del usuario loggeado si este no marcó la casilla Mantener Sesión Iniciada
def borrarUsuarioLoggeado():
    if not comprobar_inicio_sesion_automatico():
        f = open("Datos/user_logged_in.txt", "w+")
        f.write("")
        f.close()
