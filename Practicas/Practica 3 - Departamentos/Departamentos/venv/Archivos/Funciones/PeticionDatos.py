#
def comprobar_inicio_sesion_automatico():
    f = open("Datos/user_logged_in.txt", "r")
    datos = f.read().split(",")
    if datos[2] == "1":
        return True
    else:
        return False