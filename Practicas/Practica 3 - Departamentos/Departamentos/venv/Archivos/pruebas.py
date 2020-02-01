#import tkinter as tk
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

import primertest_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    primertest_support.set_Tk_var()
    top = Toplevel1 (root)
    primertest_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    primertest_support.set_Tk_var()
    top = Toplevel1 (w)
    primertest_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("396x224+795+276")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Inicio de Sesión")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.025, rely=0.045, relheight=0.915
                , relwidth=0.947)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.button_Iniciar_Sesion = tk.Button(self.Frame1)
        self.button_Iniciar_Sesion.place(relx=0.64, rely=0.732, height=38
                , width=122)
        self.button_Iniciar_Sesion.configure(activebackground="#ececec")
        self.button_Iniciar_Sesion.configure(activeforeground="#622000")
        self.button_Iniciar_Sesion.configure(background="#d9d9d9")
        self.button_Iniciar_Sesion.configure(disabledforeground="#a3a3a3")
        self.button_Iniciar_Sesion.configure(font="-family {Arial Black} -size 9 -weight bold")
        self.button_Iniciar_Sesion.configure(foreground="#ff5f11")
        self.button_Iniciar_Sesion.configure(highlightbackground="#d9d9d9")
        self.button_Iniciar_Sesion.configure(highlightcolor="black")
        self.button_Iniciar_Sesion.configure(pady="0")
        self.button_Iniciar_Sesion.configure(text='''Iniciar Sesión''')

        self.cb_mantener_sesion_iniciada = tk.Checkbutton(self.Frame1)
        self.cb_mantener_sesion_iniciada.place(relx=0.053, rely=0.78
                , relheight=0.122, relwidth=0.456)
        self.cb_mantener_sesion_iniciada.configure(activebackground="#ececec")
        self.cb_mantener_sesion_iniciada.configure(activeforeground="#000000")
        self.cb_mantener_sesion_iniciada.configure(background="#d9d9d9")
        self.cb_mantener_sesion_iniciada.configure(disabledforeground="#a3a3a3")
        self.cb_mantener_sesion_iniciada.configure(foreground="#000000")
        self.cb_mantener_sesion_iniciada.configure(highlightbackground="#d9d9d9")
        self.cb_mantener_sesion_iniciada.configure(highlightcolor="black")
        self.cb_mantener_sesion_iniciada.configure(justify='left')
        self.cb_mantener_sesion_iniciada.configure(text='''Mantener sesión iniciada''')
        self.cb_mantener_sesion_iniciada.configure(variable=primertest_support.che44)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.072, rely=0.229, height=21, width=74)
        self.Label1.configure(anchor='e')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Usuario''')

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.072, rely=0.424, height=21, width=74)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(anchor='e')
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Contraseña''')

        self.entry_usuario = tk.Entry(self.Frame1)
        self.entry_usuario.place(relx=0.288, rely=0.234, height=20
                , relwidth=0.597)
        self.entry_usuario.configure(background="white")
        self.entry_usuario.configure(cursor="fleur")
        self.entry_usuario.configure(disabledforeground="#a3a3a3")
        self.entry_usuario.configure(font="TkFixedFont")
        self.entry_usuario.configure(foreground="#000000")
        self.entry_usuario.configure(insertbackground="black")

        self.entry_contrasenya = tk.Entry(self.Frame1)
        self.entry_contrasenya.place(relx=0.288, rely=0.434, height=20
                , relwidth=0.597)
        self.entry_contrasenya.configure(background="white")
        self.entry_contrasenya.configure(disabledforeground="#a3a3a3")
        self.entry_contrasenya.configure(font="TkFixedFont")
        self.entry_contrasenya.configure(foreground="#000000")
        self.entry_contrasenya.configure(highlightbackground="#d9d9d9")
        self.entry_contrasenya.configure(highlightcolor="black")
        self.entry_contrasenya.configure(insertbackground="black")
        self.entry_contrasenya.configure(selectbackground="#c4c4c4")
        self.entry_contrasenya.configure(selectforeground="black")
        self.entry_contrasenya.configure(show="*")

if __name__ == '__main__':
    vp_start_gui()




from tkinter import *

window = Tk()
window.title("Inicio de sesión")
window.geometry('350x200')

frame1 = Frame(window, bg="#ffa561").place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

label_nombre = Label(frame1, text="Nombre: ").grid(column=0, row=0)

txt_nombre = Entry(frame1,width=10).grid(column=1, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()

'''
from tkinter import *

ventana = Tk()

canvas = Canvas(ventana, height=400, width=400, bg="#ffa561").pack()

frame1 = Frame(ventana, bg="white").place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)


#label_prueba = Label(canvas, text="Prueba", fg="red").pack()

ventana.mainloop()
'''