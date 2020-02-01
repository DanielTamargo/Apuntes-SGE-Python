import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

root = tk.Tk()

def crearVentana():

    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'

    root.geometry("396x224+795+276")
    root.minsize(120, 1)
    root.maxsize(1924, 1061)
    root.resizable(1, 1)
    root.title("Inicio de Sesión")
    root.configure(background="#d9d9d9")

    Frame1 = tk.Frame(root)
    Frame1.place(relx=0.025, rely=0.045, relheight=0.915
            , relwidth=0.947)
    Frame1.configure(relief='groove')
    Frame1.configure(borderwidth="2")
    Frame1.configure(relief="groove")
    Frame1.configure(background="#d9d9d9")

    Label1 = tk.Label(Frame1)
    Label1.place(relx=0.072, rely=0.229, height=21, width=74)
    Label1.configure(anchor='e')
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''Usuario''')

    Label1_1 = tk.Label(Frame1)
    Label1_1.place(relx=0.072, rely=0.424, height=21, width=74)
    Label1_1.configure(activebackground="#f9f9f9")
    Label1_1.configure(activeforeground="black")
    Label1_1.configure(anchor='e')
    Label1_1.configure(background="#d9d9d9")
    Label1_1.configure(disabledforeground="#a3a3a3")
    Label1_1.configure(foreground="#000000")
    Label1_1.configure(highlightbackground="#d9d9d9")
    Label1_1.configure(highlightcolor="black")
    Label1_1.configure(text='''Contraseña''')

    entry_usuario = tk.Entry(Frame1)
    entry_usuario.place(relx=0.288, rely=0.234, height=20
            , relwidth=0.597)
    entry_usuario.configure(background="white")
    #entry_usuario.configure(cursor="fleur")
    entry_usuario.configure(disabledforeground="#a3a3a3")
    entry_usuario.configure(font="TkFixedFont")
    entry_usuario.configure(foreground="#000000")
    entry_usuario.configure(insertbackground="black")

    entry_contrasenya = tk.Entry(Frame1)
    entry_contrasenya.place(relx=0.288, rely=0.434, height=20
            , relwidth=0.597)
    entry_contrasenya.configure(background="white")
    entry_contrasenya.configure(disabledforeground="#a3a3a3")
    entry_contrasenya.configure(font="TkFixedFont")
    entry_contrasenya.configure(foreground="#000000")
    entry_contrasenya.configure(highlightbackground="#d9d9d9")
    entry_contrasenya.configure(highlightcolor="black")
    entry_contrasenya.configure(insertbackground="black")
    entry_contrasenya.configure(selectbackground="#c4c4c4")
    entry_contrasenya.configure(selectforeground="black")
    entry_contrasenya.configure(show="*")

    marcado = tk.IntVar()

    cb_mantener_sesion_iniciada = tk.Checkbutton(Frame1, var=marcado)
    cb_mantener_sesion_iniciada.place(relx=0.053, rely=0.78
            , relheight=0.122, relwidth=0.456)
    cb_mantener_sesion_iniciada.configure(activebackground="#ececec")
    cb_mantener_sesion_iniciada.configure(activeforeground="#000000")
    cb_mantener_sesion_iniciada.configure(background="#d9d9d9")
    cb_mantener_sesion_iniciada.configure(disabledforeground="#a3a3a3")
    cb_mantener_sesion_iniciada.configure(foreground="#000000")
    cb_mantener_sesion_iniciada.configure(highlightbackground="#d9d9d9")
    cb_mantener_sesion_iniciada.configure(highlightcolor="black")
    cb_mantener_sesion_iniciada.configure(justify='left')
    cb_mantener_sesion_iniciada.configure(text='''Mantener sesión iniciada''')
    #cb_mantener_sesion_iniciada.configure(variable=InicioSesion_support.che44)

    def iniciarSesion():
        nombre = entry_usuario.get()
        contrasenya = entry_contrasenya.get()
        #marcado = cb_mantener_sesion_iniciada.getboolean()
        print(marcado.get()) #0 = false, 1 = true
        print(nombre)
        print(contrasenya)
        print("hola")

        f = open("user_logged_in.txt", "w")

        # ¿buscar el id de empleado relacionado y guardar el id encriptado en el archivo y desencriptar a la hora de recoger los datos cuando lo necesitemos?


        f.write("{0},{1},{2}".format(nombre, contrasenya, marcado.get()))

        f.close()

        # Cargar lista de usuarios y contraseñas y cotejar datos
        if nombre == "dani" and contrasenya == "dani":
            datos = (nombre, contrasenya)
            root.destroy()

        # Falta por añadir comprobar que sean válidos y luego arreglar el poder devolverlos
        # Propongo usar una función de funciones para cargar el fichero usuarios y contraseñas y contrastar datos
        # También propongo que si los datos son correctos se use un fichero temporal para pasar los datos a otro lado


    button_Iniciar_Sesion = tk.Button(Frame1)
    button_Iniciar_Sesion.place(relx=0.64, rely=0.732, height=38
            , width=122)
    button_Iniciar_Sesion.configure(activebackground="#ececec")
    button_Iniciar_Sesion.configure(activeforeground="#622000")
    button_Iniciar_Sesion.configure(background="#d9d9d9")
    button_Iniciar_Sesion.configure(disabledforeground="#a3a3a3")
    button_Iniciar_Sesion.configure(font="-family {Arial Black} -size 9 -weight bold")
    button_Iniciar_Sesion.configure(foreground="#ff5f11")
    button_Iniciar_Sesion.configure(highlightbackground="#d9d9d9")
    button_Iniciar_Sesion.configure(highlightcolor="black")
    button_Iniciar_Sesion.configure(pady="0")
    button_Iniciar_Sesion.configure(text='''Iniciar Sesión''')
    datos = button_Iniciar_Sesion.configure(command=iniciarSesion)

    root.mainloop()

#crearVentana()

