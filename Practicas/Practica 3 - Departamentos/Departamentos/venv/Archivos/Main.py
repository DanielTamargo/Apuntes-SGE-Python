from Archivos.Ventanas import InicioSesion as inicio

# Si marcó la opción mantener sesión iniciada, omitimos el inicio de sesión

# Inicio de sesión
inicio.crearVentana()




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

