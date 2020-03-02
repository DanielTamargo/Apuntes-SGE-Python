from Archivos.Ventanas import InicioSesion as inicio
from Archivos.Funciones import PeticionDatos as pd
from Archivos.Funciones import Logs

# from tkinter import Tk

# Si marcó la opción mantener sesión iniciada, omitimos el inicio de sesión
inicio_sesion_automatico = Logs.comprobar_inicio_sesion_automatico()
if inicio_sesion_automatico is False:
    inicio = inicio.crearVentana()
else:
    inicio = True

if inicio is True:
    print("Hacer log, mostrar menú, etc")
    # Recogemos usuario
    usuario = Logs.cargarUsuarioLoggeado()
    # Log
    Logs.generarLog(usuario)

    # Borramos los datos de user_logged_in si no marcó la casilla de mantener sesión iniciada
    Logs.borrarUsuarioLoggeado()




else:
    print("Fin del programa")




'''python
# Creamos la ventana
ventana = tkinter.Tk()
ventana.title("Inicio de sesión")

# Dividimos la ventana en frames
# Frame para los text-fields
top_frame = tkinter.Frame(ventana).pack()
# Frame para los botones de abajo
bottom_frame = tkinter.Frame(ventana).pack(side="bottom")

# Botones
btn_cerrar_ventana = tkinter.Button(bottom_frame, text="Iniciar sesión",fg="purple").pack(side="left")
btn_cancelar = tkinter.Button(bottom_frame, text="Cancelar",fg="purple").pack(side="left")

# Ejecutamos la ventana en bucle hasta que la cerremos
ventana.mainloop()
'''

