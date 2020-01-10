import datetime
import dateutil.relativedelta as dr

#from Archivos import Clases as Clases
#from Archivos import Funciones as Fun
#from Archivos import MiBot
import Clases
import Funciones as Fun
import MiBot

import colorama
import re
import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

#------------------------------------------------- Colores ------------------------------------------------------------#
def colores():
    diccionario_colores = {
        "lc": colorama.Fore.LIGHTCYAN_EX,
        "lr": colorama.Fore.LIGHTRED_EX,
        "lm": colorama.Fore.LIGHTMAGENTA_EX,
        "ly": colorama.Fore.LIGHTYELLOW_EX,
        "r": colorama.Fore.RED,
        "rst": colorama.Style.RESET_ALL,
        "*": colorama.Style.BRIGHT
    }
    return diccionario_colores

#--------------------------------------------------- Menús ------------------------------------------------------------#
def menu_principal():
    c = colores()
    print()
    print(c["lm"] + c["*"] + "Menú" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Empleados")
    print(c["lm"] + "2. " + c["lc"] + "Clientes")
    print(c["lm"] + "3. " + c["lc"] + "Actividades")
    print(c["lm"] + "4. " + c["lc"] + "Informes")
    print(c["lm"] + "5. " + c["lc"] + "Oportunidades.")
    print(c["lm"] + "6. " + c["lc"] + "Gráficas")
    print(c["lm"] + "7. " + c["lc"] + "Extras.")
    print(c["lm"] + "8. " + c["lc"] + "Salir." + c["rst"])
    return input("Opción: ")

def menu_empleados():
    c = colores()
    print(c["lm"] + c["*"] + "Menú empleados" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Nuevo empleado")
    print(c["lm"] + "2. " + c["lc"] + "Modificar empleado")
    print(c["lm"] + "3. " + c["lc"] + "Eliminar empleado" + c["rst"])
    return input("Opción: ")

def menu_clientes():
    c = colores()
    print(c["lm"] + c["*"] + "Menú clientes" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Nuevo cliente")
    print(c["lm"] + "2. " + c["lc"] + "Modificar cliente")
    print(c["lm"] + "3. " + c["lc"] + "Eliminar cliente" + c["rst"])
    return input("Opción: ")

def menu_actividades():
    c = colores()
    print(c["lm"] + c["*"] + "Menú actividades" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Nueva actividad")
    print(c["lm"] + "2. " + c["lc"] + "Modificar actividad")
    print(c["lm"] + "3. " + c["lc"] + "Eliminar actividad" + c["rst"])
    return input("Opción: ")

def menu_informes():
    c = colores()
    print(c["lm"] + c["*"] + "Menú informes" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Nuevo informe")
    print(c["lm"] + "2. " + c["lc"] + "Modificar informe")
    print(c["lm"] + "3. " + c["lc"] + "Eliminar informe" + c["rst"])
    return input("Opción: ")

def menu_oportunidades():
    c = colores()
    print(c["lm"] + c["*"] + "Menú oportunidades" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Nueva oportunidad")
    print(c["lm"] + "2. " + c["lc"] + "Modificar oportunidad")
    print(c["lm"] + "3. " + c["lc"] + "Eliminar oportunidad" + c["rst"])
    return input("Opción: ")

def menu_graficas():
    c = colores()
    print(c["lm"] + c["*"] + "Menú gráficas" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Número de clientes y empleados por informe")
    print(c["lm"] + "2. " + c["lc"] + "Actividades por meses")
    print(c["lm"] + "3. " + c["lc"] + "Dinero" + c["rst"])
    return input("Opción: ")

def menu_extras():
    c = colores()
    print(c["lm"] + c["*"] + "Menú extras" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Text-to-speech")
    print(c["lm"] + "2. " + c["lc"] + "Voice-to-text")
    print(c["lm"] + "3. " + c["lc"] + "Habla con el bot (W.I.P.)" + c["rst"])
    return input("Opción: ")

#------------------------------------------------- Útiles -------------------------------------------------------------#
def tts(texto):
    lenguaje = "da" # Lista: https://developers.google.com/admin-sdk/directory/v1/languages
    tts = gTTS(text=texto, lang=lenguaje)
    hoy = datetime.datetime.today()
    hoy = hoy.strftime("%d-%m-%Y_%H-%M-%S")
    nombre_archivo = "Audios/" + str(hoy) + "_" + str(lenguaje) + "_tts_voice.mp3"
    tts.save(nombre_archivo)
    playsound.playsound(nombre_archivo)

def pedir_numero():
    c = colores()
    while True:
        a = input("Elección: ")
        if len(str(a)) > 0:
            try:
                a = int(a)
                return a
            except:
                pass
            if str(a).lower() == "salir":
                return str(a).lower()
            else:
                print("{0}Error.{1} No has introducido un número válido.\n".format(c["lr"], c["rst"]))
        else:
            print("{0}Error.{1} No has introducido nada.\n".format(c["lr"], c["rst"]))

# Comprueba que la fecha sea válida (patrones, comprobar edad > 16, comprobar años bisiestos y transformación a fecha)
def pedir_fecha(pregunta):
    c = colores()
    correcto = False
    while not correcto:
        patron1_b = False
        patron2_b = False
        fecha_a_devolver = ""

        fecha = input(pregunta)
        if len(fecha) > 0:
            if (fecha.lower() == "today" or fecha.lower() == "hoy") and "nacimiento" not in pregunta:
                fecha_a_devolver = datetime.date.today()
                return fecha_a_devolver
            if "vencimiento" in pregunta:
                if fecha.lower() == "dia":
                    hoy = datetime.date.today()
                    fecha_a_devolver = hoy + datetime.timedelta(days=1)
                    return fecha_a_devolver
                elif fecha.lower() == "semana":
                    hoy = datetime.date.today()
                    fecha_a_devolver = hoy + datetime.timedelta(weeks=1)
                    return fecha_a_devolver
        fecha = fecha.replace(" ","-")

        # Día-Mes-Año
        patron1 = re.compile("[0-3][0-9]-[0-1][0-9]-[1-2]\d{3}")
        if patron1.match(fecha):
            correcto = True
            patron1_b = True

        #Año-Mes-Día
        patron2 = re.compile("[1-2]\d{3}-[0-1][0-9]-[0-3][0-9]")
        if patron2.match(fecha):
            correcto = True
            patron2_b = True

        if patron1_b:
            try:
                fecha_a_devolver = datetime.datetime.strftime(datetime.datetime.strptime(fecha, "%d-%m-%Y"), "%Y-%m-%d")
            except:
                correcto = False
                fecha_a_devolver = ""

        if patron2_b:
            try:
                fecha_a_devolver = datetime.datetime.strftime(datetime.datetime.strptime(fecha, "%Y-%m-%d"), "%Y-%m-%d")
            except:
                correcto = False
                fecha_a_devolver = ""

        if patron1_b or patron2_b:
            if str(fecha_a_devolver) != "":
                if "nacimiento" in pregunta:
                    fecha_nac = datetime.datetime.strptime(fecha_a_devolver, '%Y-%m-%d')
                    hoy = datetime.datetime.today()
                    try:
                        cumpleanyos = fecha_nac.replace(year=hoy.year)
                    except:
                        cumpleanyos = fecha_nac.replace(year=hoy.year, month=fecha_nac.month + 1, day=1)
                    if cumpleanyos > hoy:
                        edad =  hoy.year - fecha_nac.year - 1
                    else:
                        edad = hoy.year - fecha_nac.year
                    if edad < 16:
                        correcto = False
                        print("{0}¡Ups!{1} Edad mínima requerida: {2}16{3}\n".format(c["lr"], c["rst"], c["r"], c["rst"]))
                    else:
                        return fecha_a_devolver
                else:
                    return fecha_a_devolver
            else:
                correcto = False
                print("{0}Error.{1} No has introducido una fecha válida.\n".format(c["lr"], c["rst"]))
        else:
            correcto = False
            print("{0}Error.{1} No has introducido una fecha válida.\n".format(c["lr"], c["rst"]))

#-------------------------------------------------- Opciones ----------------------------------------------------------#
########### AÚN WIP
def wip(): # <- salta en algunos puntos que no he acabado
    c = colores()
    print(c["lm"] + c["*"] + "W.I.P." + c["rst"])
    print("Esta opción aún está en construcción.")

########### PASS
def pasar(): # <- asegura que no pueda romperse el diccionario sub_opciones del main
    pass

########### OPCIONES EMPLEADOS
def opcion_nuevo_empleado():
    c = colores()
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    dni = input("DNI: ")
    email = input("Email: ")
    fecha_nacimiento = pedir_fecha("Fecha de nacimiento (YYYY-MM-DD): ")
    #print(fecha_nacimiento)
    respuesta = ""
    departamentos = {"1":Clases.Departamento.Comercial, "2":Clases.Departamento.Administrativo,
                     "3":Clases.Departamento.Ventas, "4":Clases.Departamento.RRHH,"5":Clases.Departamento.Salud}
    while respuesta == "":
        print("Elige un departamento:")
        print("1. Comercial")
        print("2. Administrativo")
        print("3. Ventas")
        print("4. RRHH")
        print("5. Salud")
        respuesta = input("Departamento: ")
        if respuesta in departamentos:
            departamento = departamentos[respuesta]
        else:
            respuesta = ""
        if respuesta == "":
            print("{0}¡Ups!{1} No te he entendido :(.\n".format(c["lr"], c["rst"]))
    fecha_contratacion = pedir_fecha("Fecha de contratación (YYYY-MM-DD) (hoy/today): ")
    # Quito las comas porque fastidiarían el sistema de recogida de datos del fichero.
    empleado = Clases.Empleado(dni.replace(",",""), nombre.replace(",",""), apellidos.replace(",",""),
                               email.replace(",",""), str(fecha_nacimiento), departamento, str(fecha_contratacion))
    Fun.guardar_empleado(empleado)
    print(c["lc"] + "¡Empleado creado correctamente!" + c["rst"])

def opcion_modificar_empleado():
    c = colores()
    print(c["lc"] + "Selecciona el empleado a modificar (o introduce 'salir')")
    empleados = Fun.cargar_datos_empleados()
    x = 1
    for empleado in empleados:
        print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(empleado)))
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        print()
        eleccion = eleccion - 1
        if 0 <= eleccion < len(empleados):
            empleado = empleados[eleccion]
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            dni = input("DNI: ")
            email = input("Email: ")
            fecha_nacimiento = pedir_fecha("Fecha de nacimiento (YYYY-MM-DD): ")
            # print(fecha_nacimiento)
            respuesta = ""
            departamentos = {"1": Clases.Departamento.Comercial, "2": Clases.Departamento.Administrativo,
                             "3": Clases.Departamento.Ventas, "4": Clases.Departamento.RRHH,
                             "5": Clases.Departamento.Salud}
            while respuesta == "":
                print("Elige un departamento:")
                print("1. Comercial")
                print("2. Administrativo")
                print("3. Ventas")
                print("4. RRHH")
                print("5. Salud")
                respuesta = input("Departamento: ")
                if respuesta in departamentos:
                    departamento = departamentos[respuesta]
                else:
                    respuesta = ""
                if respuesta == "":
                    print("{0}¡Ups!{1} No te he entendido :(.\n".format(c["lr"], c["rst"]))
            fecha_contratacion = pedir_fecha("Fecha de contratación (YYYY-MM-DD) (hoy/today): ")

            print("{0}Estás a punto de guardar los cambios modificando a:{1} {2}{3}".format(c["lc"], c["ly"], str(empleado), c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Modificar? (s/n): ")
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        empleado.dni = dni
                        empleado.nombre = nombre
                        empleado.apellidos = apellidos
                        empleado.email = email
                        empleado.fecha_nacimiento = fecha_nacimiento
                        empleado.departamento = departamento
                        empleado.fecha_contratacion = fecha_contratacion

                        Fun.modificar_empleado(empleado)
                        print(c["lc"] + "¡Empleado modificado correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "El empleado no será modificado")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))

    else:
        print("Saliendo del menú...")

def opcion_borrar_empleado():
    c = colores()
    print(c["lc"] + "Selecciona el empleado a eliminar (o introduce 'salir')")
    empleados = Fun.cargar_datos_empleados()
    x = 1
    for empleado in empleados:
        print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(empleado)))
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        print()
        eleccion = eleccion - 1
        if 0 <= eleccion < len(empleados):
            empleado = empleados[eleccion]
            print("{0}Estás a punto de eliminar:{1} {2}{3}".format(c["lc"], c["ly"], str(empleado), c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Eliminar? (s/n): ")
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        Fun.borrar_empleado(empleado)
                        print(c["lc"] + "¡Empleado eliminado correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "El empleado no será eliminado")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")


########### OPCIONES CLIENTES
def opcion_nuevo_cliente():
    c = colores()
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    dni = input("DNI: ")
    email = input("Email: ")
    fecha_nacimiento = pedir_fecha("Fecha de nacimiento (YYYY-MM-DD): ")
    #print(fecha_nacimiento)
    respuesta = ""
    tipos_clientes = {"1":Clases.TipoCliente.Cliente, "2":Clases.TipoCliente.Sponsor,
                     "3":Clases.TipoCliente.Proveedor}
    while respuesta == "":
        print("Elige un tipo de cliente:")
        print("1. Cliente")
        print("2. Sponsor")
        print("3. Proveedor")
        respuesta = input("Tipo cliente: ")
        if respuesta in tipos_clientes:
            tipocliente = tipos_clientes[respuesta]
        else:
            respuesta = ""
        if respuesta == "":
            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    # Quito las comas porque fastidiarían el sistema de recogida de datos del fichero.
    cliente = Clases.Cliente(dni.replace(",",""), nombre.replace(",",""), apellidos.replace(",",""),
                               email.replace(",",""), str(fecha_nacimiento), tipocliente)
    Fun.guardar_cliente(cliente)
    print(c["lc"] + "¡Cliente creado correctamente!" + c["rst"])

def opcion_modificar_cliente():
    c = colores()
    print(c["lc"] + "Selecciona el cliente a modificar (o introduce 'salir')")
    clientes = Fun.cargar_datos_clientes()
    x = 1
    for cliente in clientes:
        print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(cliente)))
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        print()
        eleccion = eleccion - 1
        if 0 <= eleccion < len(clientes):
            cliente = clientes[eleccion]
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            dni = input("DNI: ")
            email = input("Email: ")
            fecha_nacimiento = pedir_fecha("Fecha de nacimiento (YYYY-MM-DD): ")
            # print(fecha_nacimiento)
            respuesta = ""
            tipos_clientes = {"1": Clases.TipoCliente.Cliente, "2": Clases.TipoCliente.Sponsor,
                              "3": Clases.TipoCliente.Proveedor}
            while respuesta == "":
                print("Elige un tipo de cliente:")
                print("1. Cliente")
                print("2. Sponsor")
                print("3. Proveedor")
                respuesta = input("Tipo cliente: ")
                if respuesta in tipos_clientes:
                    tipocliente = tipos_clientes[respuesta]
                else:
                    respuesta = ""
                if respuesta == "":
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))

            print("{0}Estás a punto de guardar los cambios modificando a:{1} {2}{3}".format(c["lc"], c["ly"], str(cliente), c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Modificar? (s/n): ")
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        cliente.dni = dni
                        cliente.nombre = nombre
                        cliente.apellidos = apellidos
                        cliente.email = email
                        cliente.fecha_nacimiento = fecha_nacimiento
                        cliente.tipocliente = tipocliente

                        Fun.modificar_cliente(cliente)
                        print(c["lc"] + "¡Cliente modificado correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "El cliente no será modificado")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))

    else:
        print("Saliendo del menú...")

def opcion_borrar_cliente():
    c = colores()
    print(c["lc"] + "Selecciona el cliente a eliminar (o introduce 'salir')")
    clientes = Fun.cargar_datos_clientes()
    x = 1
    for cliente in clientes:
        print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(cliente)))
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        print()
        eleccion = eleccion - 1
        if 0 <= eleccion < len(clientes):
            cliente = clientes[eleccion]
            print("{0}Estás a punto de eliminar:{1} {2}{3}".format(c["lc"], c["ly"], str(cliente), c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Eliminar? (s/n): ")
                print()
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        Fun.borrar_cliente(cliente)
                        print(c["lc"] + "¡Cliente eliminado correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "El cliente no será eliminado")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")


########### OPCIONES ACTIVIDADES
def opcion_nueva_actividad():
    c = colores()
    descripcion = input("Descripción: ")
    fecha_vencimiento = pedir_fecha("Fecha de vencimiento (YYYY-MM-DD) (dia/semana): ")
    fecha_planificacion = pedir_fecha("Fecha de planificación (YYYY-MM-DD) (hoy/today): ")
    respuesta = ""
    tipos_actividades = {"1":Clases.TipoActividad.Reunion, "2":Clases.TipoActividad.Llamada,
                     "3":Clases.TipoActividad.Promocion, "4":Clases.TipoActividad.Informe}
    tipoactividad = Clases.TipoActividad.Reunion
    while respuesta == "":
        print("Elige un tipo de actividad:")
        print("1. Reunión")
        print("2. Llamada")
        print("3. Promoción")
        print("4. Informe")
        respuesta = input("Tipo de actividad: ")
        if respuesta in tipos_actividades:
            tipoactividad = tipos_actividades[respuesta]
        else:
            respuesta = ""
        if respuesta == "":
            print("{0}¡Ups!{1} No te he entendido :(.\n".format(c["lr"], c["rst"]))

    # Quito las comas porque fastidiarían el sistema de recogida de datos del fichero.
    actividad = Clases.Actividad(descripcion.replace(",",""), str(fecha_vencimiento), str(fecha_planificacion),
                               tipoactividad)
    Fun.guardar_actividad(actividad)
    print(c["lc"] + "¡Actividad creada correctamente!" + c["rst"])

def opcion_modificar_actividad():
    c = colores()
    print(c["lc"] + "Selecciona la actividad a modificar (o introduce 'salir')")
    actividades = Fun.cargar_datos_actividades()
    x = 1
    for actividad in actividades:
        print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(actividad)))
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        eleccion = int(eleccion) - 1
        if eleccion >= 0 and eleccion < len(actividades):
            actividad = actividades[eleccion]
            descripcion = input("Descripción: ")
            fecha_vencimiento = pedir_fecha("Fecha de vencimiento (YYYY-MM-DD) (dia/semana): ")
            fecha_planificacion = pedir_fecha("Fecha de planificación (YYYY-MM-DD) (hoy/today): ")
            respuesta = ""
            tipos_actividades = {"1": Clases.TipoActividad.Reunion, "2": Clases.TipoActividad.Llamada,
                                 "3": Clases.TipoActividad.Promocion, "4": Clases.TipoActividad.Informe}
            tipoactividad = Clases.TipoActividad.Reunion
            while respuesta == "":
                print("Elige un tipo de actividad:")
                print("1. Reunión")
                print("2. Llamada")
                print("3. Promoción")
                print("4. Informe")
                respuesta = input("Tipo de actividad: ")
                if respuesta in tipos_actividades:
                    tipoactividad = tipos_actividades[respuesta]
                else:
                    respuesta = ""
                if respuesta == "":
                    print("{0}¡Ups!{1} No te he entendido :(.\n".format(c["lr"], c["rst"]))

            actividad.descripcion = descripcion
            actividad.fecha_vencimiento = fecha_vencimiento
            actividad.fecha_planificacion = fecha_planificacion
            actividad.tipoactividad = tipoactividad

            Fun.modificar_actividad(actividad)
            print(c["lc"] + "¡Actividad modificada correctamente!" + c["rst"])
        else:
            print("{0}¡Ups!{1} No te he entendido :(.\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")

def opcion_borrar_actividad():
    c = colores()
    print(c["lc"] + "Selecciona la actividad a eliminar (o introduce 'salir')")
    actividades = Fun.cargar_datos_actividades()
    x = 1
    for actividad in actividades:
        print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(actividad)))
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        print()
        eleccion = eleccion - 1
        if 0 <= eleccion < len(actividades):
            actividad = actividades[eleccion]
            print("{0}Estás a punto de eliminar:{1} {2}{3}".format(c["lc"], c["ly"], str(actividad), c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Eliminar? (s/n): ")
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        Fun.borrar_actividad(actividad)
                        print(c["lc"] + "¡Actividad eliminada correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "La actividad no será eliminada")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")
        
########### OPCIONES INFORMES
def opcion_nuevo_informe():
    c = colores()
    print(c["lc"] + "Selecciona una actividad sobre la que crear el informe (o introduce 'salir'):" + c["rst"])
    actividades = Fun.cargar_datos_actividades()
    informes_existentes = Fun.cargar_datos_informes()
    if len(informes_existentes) > 0:
        for informe_existente in informes_existentes:
            for actividad in actividades:
                if informe_existente.getActividad().id == actividad.id:
                    actividades.remove(actividad)
    if len(actividades) > 0:
        x = 1
        for actividad in actividades:
            print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(actividad)))
            x += 1
        eleccion = pedir_numero()
        if str(eleccion) != "salir":
            print()
            eleccion = eleccion - 1
            if 0 <= eleccion < len(actividades):
                actividad = actividades[eleccion]
                correcto = False

                empleados = Fun.cargar_datos_empleados()
                lista_empleados_informe = []
                while not correcto:
                    print(c["lc"] + "Selecciona un empleado que administre el informe (o introduce 'salir'):" + c["rst"])
                    if len(lista_empleados_informe) > 0:
                        for empleado_informe in lista_empleados_informe:
                            if empleado_informe in empleados:
                                empleados.remove(empleado_informe)
                    x = 1
                    if len(empleados) > 0:
                        for empleado in empleados:
                            print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(empleado)))
                            x += 1
                        eleccion = pedir_numero()
                    else:
                        print("{0}No{1} quedan empleados que no estén añadidos al informe\n".format(c["r"], c["rst"]))
                        eleccion = "salir"
                    if str(eleccion) != "salir":
                        eleccion = int(eleccion) - 1
                        print()
                        if 0 <= int(eleccion) < len(empleados):
                            lista_empleados_informe.append(empleados[eleccion])
                            print("Empleado añadido al informe.")
                            respuesta = ""
                            while respuesta == "":
                                respuesta = input("¿Quieres añadir más empleados al informe? (s/n): ")
                                if respuesta != "":
                                    if respuesta.lower()[0] == "s":
                                        pass
                                    elif respuesta.lower()[0] == "n":
                                        correcto = True
                                    else:
                                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                                        respuesta = ""
                                else:
                                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                        else:
                            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                    else:
                        correcto = True

                correcto = False

                clientes = Fun.cargar_datos_clientes()
                lista_clientes_informe = []
                while not correcto:
                    print(c["lc"] + "Selecciona un cliente para que aparezca en el informe (o introduce 'salir'):" + c["rst"])
                    if len(lista_clientes_informe) > 0:
                        for cliente_informe in lista_clientes_informe:
                            if cliente_informe in clientes:
                                clientes.remove(cliente_informe)
                    x = 1
                    if len(clientes) > 0:
                        for cliente in clientes:
                            print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(cliente)))
                            x += 1
                        eleccion = pedir_numero()
                    else:
                        print("{0}No{1} quedan empleados que no estén añadidos al informe\n".format(c["r"], c["rst"]))
                        eleccion = "salir"
                    if str(eleccion) != "salir":
                        eleccion = int(eleccion) - 1
                        print()
                        if 0 <= int(eleccion) < len(clientes):
                            lista_clientes_informe.append(clientes[eleccion])
                            print("Cliente añadido al informe.")
                            respuesta = ""
                            while respuesta == "":
                                respuesta = input("¿Quieres añadir más clientes al informe? (s/n): ")
                                print()
                                if respuesta != "":
                                    if respuesta.lower()[0] == "s":
                                        pass
                                    elif respuesta.lower()[0] == "n":
                                        correcto = True
                                    else:
                                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                                        respuesta = ""
                                else:
                                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                        else:
                            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                    else:
                        correcto = True
                informe = Clases.Informe(actividad, lista_clientes_informe, lista_empleados_informe)
                Fun.guardar_informe(informe)
                print(c["lc"] + "¡Informe creado correctamente!" + c["rst"])
            else:
                print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
        else:
            print("Saliendo del menú...")
    else:
        print("{0}¡Ups!{1} No quedan actividades para asignarlos a un informe. ¡Crea nuevas actividades primero!\n".format(c["lr"], c["rst"]))


def opcion_modificar_informe():
    c = colores()
    print(c["lc"] + "Elige el informe a modificar (o introduce 'salir')" + c["rst"])
    print()
    informes = Fun.cargar_datos_informes()
    x = 1
    for informe in informes:
        print("{0}{1}.{2}".format(c["lc"], x, c["rst"]))
        informe.mostrar_informe()
        x += 1
    print()
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        print()
        eleccion = int(eleccion) - 1
        if 0 <= eleccion < len(informes):
            informe = informes[eleccion]
            print(c["lc"] + "Elige cómo modificar el informe (o introduce 'salir')" + c["rst"])
            print("1. Añadir emlpeados")
            print("2. Añadir clientes")
            print("3. Eliminar un empleado")
            print("4. Eliminar un cliente")
            eleccion = pedir_numero()
            if str(eleccion) != "salir":
                print()
                eleccion = int(eleccion)
                if 0 <= eleccion <= 4:
                    if eleccion == 1:
                        correcto = False
                        lista_empleados_informe = informe.getEmpleados()
                        empleados = Fun.cargar_datos_empleados()
                        while not correcto:
                            print(c["lc"] + "Selecciona un empleado que administre el informe (o introduce 'salir'):" + c["rst"])
                            if len(lista_empleados_informe) > 0:
                                for empleado_informe in lista_empleados_informe:
                                    for empleado in empleados:
                                        if empleado_informe.id == empleado.id:
                                            empleados.remove(empleado)
                            x = 1
                            if len(empleados) > 0:
                                for empleado in empleados:
                                    print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(empleado)))
                                    x += 1
                                eleccion = pedir_numero()
                            else:
                                print("{0}No{1} quedan empleados que no estén añadidos al informe\n".format(c["r"],
                                                                                                            c["rst"]))
                                eleccion = "salir"
                            if str(eleccion) != "salir":
                                eleccion = int(eleccion) - 1
                                print()
                                if 0 <= int(eleccion) < len(empleados):
                                    informe.addEmpleado(empleados[eleccion])
                                    #lista_empleados_informe.append(empleados[eleccion])
                                    print("Empleado añadido al informe.")
                                    print()
                                    respuesta = ""
                                    while respuesta == "":
                                        respuesta = input("¿Quieres añadir más empleados al informe? (s/n): ")
                                        if respuesta != "":
                                            if respuesta.lower()[0] == "s":
                                                pass
                                            elif respuesta.lower()[0] == "n":
                                                correcto = True
                                                Fun.modificar_informe(informe)
                                                print(c["lc"] + "¡Informe modificado correctamente!" + c["rst"])
                                            else:
                                                print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                                                respuesta = ""
                                        else:
                                            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                            else:
                                correcto = True
                    elif eleccion == 2:
                        correcto = False
                        lista_clientes_informe = informe.getClientes()
                        clientes = Fun.cargar_datos_clientes()
                        while not correcto:
                            print(c["lc"] + "Selecciona un cliente para que aparezca en el informe (o introduce 'salir'):" + c["rst"])
                            if len(lista_clientes_informe) > 0:
                                for cliente_informe in lista_clientes_informe:
                                    for cliente in clientes:
                                        if cliente_informe.id == cliente.id:
                                            clientes.remove(cliente)
                            x = 1
                            if len(clientes) > 0:
                                for cliente in clientes:
                                    print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(cliente)))
                                    x += 1
                                eleccion = pedir_numero()
                            else:
                                print("{0}No{1} quedan clientes que no estén añadidos al informe\n".format(c["r"],
                                                                                                            c["rst"]))
                                eleccion = "salir"
                            if str(eleccion) != "salir":
                                print()
                                eleccion = int(eleccion) - 1
                                if 0 <= int(eleccion) < len(clientes):
                                    informe.addCliente(clientes[eleccion])
                                    #lista_clientes_informe.append(clientes[eleccion])
                                    print("Cliente añadido al informe.")
                                    print()
                                    respuesta = ""
                                    while respuesta == "":
                                        respuesta = input("¿Quieres añadir más clientes al informe? (s/n): ")
                                        if respuesta != "":
                                            if respuesta.lower()[0] == "s":
                                                pass
                                            elif respuesta.lower()[0] == "n":
                                                correcto = True
                                                Fun.modificar_informe(informe)
                                                print(c["lc"] + "¡Informe modificado correctamente!" + c["rst"])
                                            else:
                                                print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                                        else:
                                            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                                            respuesta = ""
                            else:
                                correcto = True
                    elif eleccion == 3:
                        empleados = informe.getEmpleados()
                        if len(empleados) > 0:
                            print(
                                c["lc"] + "Selecciona un empleado para eliminarlo del informe (o introduce 'salir'):" + c[
                                    "rst"])
                            x = 1
                            for empleado in empleados:
                                print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(empleado)))
                                x += 1
                            eleccion = pedir_numero()
                            if str(eleccion) != "salir":
                                print()
                                eleccion = int(eleccion) - 1
                                if 0 <= eleccion < len(empleados):
                                    empleado = empleados[eleccion]
                                    informe.getEmpleados().remove(empleado)
                                    Fun.modificar_informe(informe)
                                    print("Empleado eliminado del informe.")
                                    print()
                                else:
                                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                            else:
                                print("Saliendo del menú...")
                        else:
                            print("{0}No{1} existen empleados que estén añadidos al informe\n".format(c["r"], c["rst"]))
                    elif eleccion == 4:
                        clientes = informe.getClientes()
                        if len(clientes) > 0:
                            print(
                                c["lc"] + "Selecciona un cliente para eliminarlo del informe (o introduce 'salir'):" + c[
                                    "rst"])
                            x = 1
                            for cliente in clientes:
                                print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(cliente)))
                                x += 1
                            eleccion = pedir_numero()
                            if str(eleccion) != "salir":
                                print()
                                eleccion = int(eleccion) - 1
                                if 0 <= eleccion < len(clientes):
                                    cliente = clientes[eleccion]
                                    informe.getClientes().remove(cliente)
                                    Fun.modificar_informe(informe)
                                    print("Cliente eliminado del informe.")
                                    print()
                                else:
                                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                            else:
                                print("Saliendo del menú...")
                        else:
                            print("{0}No{1} existen clientes que estén añadidos al informe\n".format(c["r"], c["rst"]))
                    else:
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
            else:
                print("Saliendo del menú...")
        else:
            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")

def opcion_borrar_informe():
    c = colores()
    print(c["lc"] + "Elige el informe a eliminar (o introduce 'salir')" + c["rst"])
    informes = Fun.cargar_datos_informes()
    x = 1
    for informe in informes:
        print("{0}{1}.{2}".format(c["lc"], x, c["rst"]))
        informe.mostrar_informe()
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        print()
        eleccion = int(eleccion) - 1
        if 0 <= eleccion < len(informes):
            informe = informes[eleccion]
            print("{0}Estás a punto de eliminar el informe:{1} {2}{3}".format(c["lc"], c["ly"], str(informe.getId()), c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Eliminar? (s/n): ")
                print()
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        Fun.borrar_informe(informe)
                        print(c["lc"] + "¡Informe eliminado correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "El informe no será eliminado")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
        else:
            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")

def introducir_dinero():
    c = colores()
    dinero = ""
    while dinero == "":
        dinero = input("Dinero estimado: ")
        try:
            dinero = float(dinero)
        except:
            dinero = ""
            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    return float(dinero)

def opcion_nueva_oportunidad():
    c = colores()
    nombre = input("Nombre oportunidad: ")
    dinero_estimado = introducir_dinero()
    oportunidad = Clases.Oportunidad(nombre, None, dinero_estimado)

    Fun.guardar_oportunidad(oportunidad)
    print(c["lc"] + "¡Oportunidad creada correctamente!" + c["rst"])

def opcion_modificar_etapa_oportunidad():
    c = colores()
    print(c["lc"] + "Vas a modificar la etapa de una oportunidad")
    print(c["lc"] + "Selecciona la oportunidad a modificar (o introduce 'salir')")
    oportunidades = Fun.cargar_datos_oportunidades()
    x = 1
    for oportunidad in oportunidades:
        print("{0}{1}.{2}".format(c["lc"], x, c["rst"]))
        oportunidad.mostrar_oportunidad()
        print()
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        print()
        eleccion = eleccion - 1
        if 0 <= eleccion < len(oportunidades):
            oportunidad = oportunidades[eleccion]
            tipos_etapas = {"1": Clases.TipoEtapa.Nueva, "2": Clases.TipoEtapa.Propuesta,
                            "3": Clases.TipoEtapa.Calificada, "4": Clases.TipoEtapa.Ganada,
                            "5": Clases.TipoEtapa.Suspendida}
            respuesta = ""
            while respuesta == "":
                print("Elige la etapa en la que se encuentra la oportunidad:")
                print("1. Nueva")
                print("2. Propuesta")
                print("3. Calificada")
                print("4. Ganada")
                print("5. Suspendida")
                respuesta = input("Tipo de etapa: ")
                if respuesta in tipos_etapas:
                    tipoetapa = tipos_etapas[respuesta]
                    if tipoetapa == oportunidad.tipoetapa:
                        respuesta = ""
                else:
                    respuesta = ""
                if respuesta == "":
                    if tipoetapa == oportunidad.tipoetapa:
                        print("{0}¡Ey!{1} Estás volviendo a poner la etapa en la que ya estaba la oportunidad\n".format(
                            c["lr"], c["rst"]))
                    else:
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
            print()
            print("{0}Estás a punto de guardar los cambios modificando a:{1} {2}{3}".format(c["lc"], c["ly"],
                                                                                            str(oportunidad), c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Modificar? (s/n): ")
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        oportunidad.tipoetapa = tipoetapa
                        Fun.modificar_oportunidad(oportunidad)
                        print(c["lc"] + "¡Oportunidad modificada correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "La oportunidad no será modificada")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")

def opcion_modificar_oportunidad_anyadir_informes():
    c = colores()
    oportunidades = Fun.cargar_datos_oportunidades()
    if len(oportunidades) > 0:
        informes = Fun.cargar_datos_informes()
        for oportunidad in oportunidades:
            if len(oportunidad.informes) > 0:
                for informe_oportunidad in oportunidad.informes:
                    for informe in informes:
                        if informe.getId() == informe_oportunidad.getId():
                            informes.remove(informe)
        if len(informes) > 0:
            print(c["lc"] + "Vas a añadir informes a una oportunidad")
            print(c["lc"] + "Selecciona la oportunidad a modificar (o introduce 'salir')")
            oportunidades = Fun.cargar_datos_oportunidades()
            x = 1
            for oportunidad in oportunidades:
                print("{0}{1}.{2}".format(c["lc"], x, c["rst"]))
                oportunidad.mostrar_oportunidad()
                print()
                x += 1
            eleccion = pedir_numero()
            if str(eleccion) != "salir":
                eleccion = int(eleccion) - 1
                if 0 <= eleccion < len(oportunidades):
                    oportunidad = oportunidades[eleccion]
                    print(c["lc"] + "Selecciona un informe para añadirlo a la oportunidad (o introduce 'salir')")
                    x = 1
                    for informe in informes:
                        print("{0}{1}.{2}".format(c["lc"], x, c["rst"]))
                        informe.mostrar_informe()
                        print()
                        x += 1
                    eleccion = pedir_numero()
                    if str(eleccion) != "salir":
                        eleccion = int(eleccion) - 1
                        if 0 <= eleccion < len(informes):
                            informe = informes[eleccion]
                            oportunidad.addInforme(informe)
                            Fun.modificar_oportunidad(oportunidad)
                            print(c["lc"] + "¡Informe añadido correctamente!" + c["rst"])
                        else:
                            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                    else:
                        print("Saliendo del menú...")
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
            else:
                print("Saliendo del menú...")
        else:
            print(
                "{0}¡Ups!{1} No quedan informes para asignarlos a una oportunidad. ¡Crea nuevos informes primero!\n".format(
                    c["lr"], c["rst"]))
    else:
        print(
            "{0}¡Ups!{1} No existen oportunidades. ¡Crea nuevos oportunidades primero!\n".format(
                c["lr"], c["rst"]))

def opcion_modificar_oportunidad_eliminar_informes():
    c = colores()
    oportunidades = Fun.cargar_datos_oportunidades()
    if len(oportunidades) > 0:
        x = 1
        for oportunidad in oportunidades:
            print("{0}{1}.{2}".format(c["lc"], x, c["rst"]))
            oportunidad.mostrar_oportunidad()
            print()
            x += 1
        eleccion = pedir_numero()
        if str(eleccion) != "salir":
            eleccion = int(eleccion) - 1
            if 0 <= eleccion < len(oportunidades):
                oportunidad = oportunidades[eleccion]
                informes_oportunidad = oportunidad.informes
                if len(informes_oportunidad) > 0:
                    print(c["lc"] + "Selecciona un informe para eliminarlo de la oportunidad (o introduce 'salir')")
                    x = 1
                    for informe in informes_oportunidad:
                        print("{0}{1}.{2}".format(c["lc"], x, c["rst"]))
                        informe.mostrar_informe()
                        print()
                        x += 1
                    eleccion = pedir_numero()
                    if str(eleccion) != "salir":
                        eleccion = int(eleccion) - 1
                        if 0 <= eleccion < len(informes_oportunidad):
                            #informe = informes_oportunidad[eleccion]
                            #oportunidad.deleteInforme(informe)
                            informes_oportunidad.remove(informes_oportunidad[eleccion])
                            Fun.modificar_oportunidad(oportunidad)
                            print(c["lc"] + "¡Informe eliminado correctamente!" + c["rst"])
                        else:
                            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                    else:
                        print("Saliendo del menú...")
                else:
                    print(
                        "{0}¡Ups!{1} Esta oportunidad no tiene informes. ¡Añádeles nuevos informes primero!\n".format(
                            c["lr"], c["rst"]))
            else:
                print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
        else:
            print("Saliendo del menú...")
    else:
        print(
            "{0}¡Ups!{1} No existen oportunidades. ¡Crea nuevos oportunidades primero!\n".format(
                c["lr"], c["rst"]))

def opcion_modificar_oportunidad():
    c = colores()
    # Mostrar un menu con 3 opciones que de a elegir entre modificar etapa, añadir actividad (informe y eliminar actividad (informe)
    print(c["lm"] + c["*"] + "Menú modificar oportunidades" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Modificar etapa oportunidad")
    print(c["lm"] + "2. " + c["lc"] + "Añadir informes")
    print(c["lm"] + "3. " + c["lc"] + "Eliminar informes" + c["rst"])
    print(c["lm"] + "4. " + c["lc"] + "Salir" + c["rst"])
    eleccion = pedir_numero()
    print()
    if str(eleccion) == "1":
        opcion_modificar_etapa_oportunidad()
    elif str(eleccion) == "2":
        opcion_modificar_oportunidad_anyadir_informes()
    elif str(eleccion) == "3":
        opcion_modificar_oportunidad_eliminar_informes()
    elif str(eleccion) == "4":
        print("Saliendo del menú...")
    else:
        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))

def opcion_borrar_oportunidad():
    c = colores()
    print(c["lc"] + "Selecciona la oportunidad a eliminar (o introduce 'salir')")
    oportunidades = Fun.cargar_datos_oportunidades()
    x = 1
    for oportunidad in oportunidades:
        print("{0}{1}.{2} {3}".format(c["lc"], x, c["rst"], str(oportunidad)))
        x += 1
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        eleccion = int(eleccion) - 1
        if eleccion >= 0 and eleccion < len(oportunidades):
            oportunidad = oportunidades[eleccion]
            print("{0}Estás a punto de eliminar la oportunidad:{1} {2}{3}".format(c["lc"], c["ly"], str(oportunidad),
                                                                              c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Eliminar? (s/n): ")
                print()
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        Fun.borrar_oportunidad(oportunidad)
                        print(c["lc"] + "¡Oportunidad eliminada correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "La oportunidad no será eliminada")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
        else:
            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")

def opcion_grafica_empleadosyclientes():
    informes = Fun.cargar_datos_informes()
    if len(informes) > 0:
        labels = []
        empleados_means = []
        clientes_means = []
        for informe in informes:
            labels.append(informe.getId())
            empleados_means.append(len(informe.getEmpleados()))
            clientes_means.append(len(informe.getClientes()))

        x = np.arange(len(labels)) # ubicación de los labels
        width = 0.30 # anchura de las barras

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, empleados_means, width, label='Empleados')
        rects2 = ax.bar(x + width/2, clientes_means, width, label='Clientes')

        # Personalizamos la gráfica un poco más
        ax.set_ylabel('Número de')
        ax.set_title('Número de empleados y clientes por informe')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        for rect in rects1:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

        for rect in rects2:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

        fig.tight_layout()

        hoy = datetime.datetime.today()
        hoy = hoy.strftime("%d-%m-%Y_%H-%M-%S")
        nombre_archivo = "Imagenes/" + str(hoy) + "_Empleados-Clientes"
        plt.savefig(nombre_archivo)

        plt.show()
    else:
        print("{0}¡Ups!{1} No existen informes actualmente :(\n".format(c["lr"], c["rst"]))

def grafico_por_meses():
    # Primero, coger la fecha de hoy y ver cuales seran los 4 meses pasados y el mes siguiente
    oportunidades = Fun.cargar_datos_oportunidades()

    hoy = datetime.date.today()

    etiqueta_primermes = ""
    etiqueta_ultmes = ""

    rango = range(1, 6)
    reuniones = []
    llamadas = []
    promociones = []
    informes = []

    for i in range(-1, 4):
        fecha = hoy - dr.relativedelta(months=i)

        if i == -1:
            if fecha.month < 10:
                etiqueta_ultmes = "01-0" + str(fecha.month) + "-" + str(fecha.year)
            else:
                etiqueta_ultmes = "01-" + str(fecha.month) + "-" + str(fecha.year)
        elif i == 3:
            if fecha.month < 10:
                etiqueta_primermes = "01-0" + str(fecha.month) + "-" + str(fecha.year)
            else:
                etiqueta_primermes = "01-" + str(fecha.month) + "-" + str(fecha.year)

        num_reuniones = 0
        num_llamadas = 0
        num_promociones = 0
        num_informes = 0

        if len(oportunidades) > 0:
            for oportunidad in oportunidades:
                informes_oportunidad = oportunidad.informes
                if informes_oportunidad is not None and len(informes_oportunidad) > 0:
                    for informe in informes_oportunidad:
                        actividad = informe.getActividad()
                        fecha_vencimiento = actividad.fecha_vencimiento
                        fecha_vencimiento = datetime.datetime.strptime(fecha_vencimiento, '%Y-%m-%d').date()
                        if fecha_vencimiento.month == fecha.month and fecha_vencimiento.year == fecha.year:
                            if actividad.tipoactividad == Clases.TipoActividad.Informe:
                                num_informes += 1
                            elif actividad.tipoactividad == Clases.TipoActividad.Promocion:
                                num_promociones += 1
                            elif actividad.tipoactividad == Clases.TipoActividad.Llamada:
                                num_llamadas += 1
                            else:
                                num_reuniones += 1

        reuniones.append(num_reuniones)
        llamadas.append(num_llamadas)
        promociones.append(num_promociones)
        informes.append(num_informes)

    reuniones.reverse()
    llamadas.reverse()
    promociones.reverse()
    informes.reverse()

    titulo = "Actividades desde " + str(etiqueta_primermes) + " hasta " + str(etiqueta_ultmes)
    labels = ["Reuniones", "Llamadas", "Promociones", "Informes"]

    plt.title(titulo)
    plt.stackplot(rango, reuniones, llamadas, promociones, informes, labels=["Reuniones", "Llamadas", "Promociones", "Informes"])
    plt.legend(loc='upper left')

    hoy = datetime.datetime.today()
    hoy = hoy.strftime("%d-%m-%Y_%H-%M-%S")
    nombre_archivo = "Imagenes/" + str(hoy) + "_TiposActividadesPorMeses"
    #plt.savefig(nombre_archivo)

    plt.show()

def opcion_extra_tts():
    c = colores()
    print(c["lc"] + "Introduce una cadena de texto que será leída por voz:" + c["rst"])
    cadena = input("Cadena: ")
    MiBot.tts(cadena)

def opcion_extra_vtt():
    c = colores()
    print(c["lc"] + "Habla:" + c["rst"])
    cadena = ""
    while cadena == "":
        cadena = MiBot.vtt()
        if cadena != "":
            print(cadena)

def opcion_extra_mibot():
    if MiBot.conversacion():
        print("\nConversación finalizada")


def evitar_tildes(cadena):
    dic_correciones = {
                       "á": "a",
                       "à": "a",
                       "é": "e",
                       "è": "e",
                       "í": "i",
                       "ì": "i",
                       "ó": "o",
                       "ò": "o",
                       "ú": "u",
                       "ù": "u",
                       "Á": "A",
                       "À": "A",
                       "É": "E",
                       "È": "E",
                       "Í": "I",
                       "Ì": "I",
                       "Ó": "O",
                       "Ò": "O",
                       "Ú": "U",
                       "Ù": "U"
                       }
    cadena = str(cadena)
    for i in range(len(cadena)):
        if cadena[i] in dic_correciones:
            cadena = cadena.replace(cadena[i], dic_correciones[cadena[i]])
    return cadena

def generar_oportunidades_automatico():
    c = colores()
    print("Introduce cuantas oportunidades quieres generar (o introduce 'salir')")
    cantidad = pedir_numero()
    if str(cantidad) != "salir":
        if cantidad > 0:
            oportunidades = Fun.cargar_datos_oportunidades()
            informes = Fun.cargar_datos_informes()
            informes_existentes = []
            for informe in informes:
                for oportunidad in oportunidades:
                    for informe_oportunidad in oportunidad.informes:
                        if informe.getId() == informe_oportunidad.getId():
                            informes_existentes.append(informe)
            if len(informes_existentes) > 0:
                for informe in informes_existentes:
                    informes.remove(informe)
            if cantidad > len(informes):
                cantidad_antes = cantidad
                cantidad = len(informes)
                print("No se pueden crear {0} oportunidades (no existen suficientes informes), se utilizarán los {1} informes restantes".format(str(cantidad_antes), str(cantidad)))
            if cantidad > 0:
                nombres = ["Captación de clientes", "Proyecto VBKAD", "Desarrollo VIVDP", "Proyecto Egibide",
                           "Expansión VPNET"]
                dineros_estimados = [1200, 900, 500, 2800, 340]
                tipos_etapas = [Clases.TipoEtapa.Nueva, Clases.TipoEtapa.Suspendida, Clases.TipoEtapa.Ganada,
                               Clases.TipoEtapa.Ganada, Clases.TipoEtapa.Calificada, Clases.TipoEtapa.Propuesta]
                x = 0
                while x < cantidad:
                    informes_oportunidad = []
                    num_random = random.randint(1,7)
                    i = 0
                    while i < num_random:
                        num_random2 = random.randint(0,(len(informes) - 1))
                        anyadir = True
                        informe_oportunidad = informes[num_random2]

                        if len(informes_oportunidad) > 0:
                            if informe_oportunidad in informes_oportunidad:
                                anyadir = False

                        if anyadir:
                            informes_oportunidad.append(informe_oportunidad)
                            x += 1
                            i += 1

                    num_random = random.randint(0, len(nombres) - 1)
                    nombre = nombres[num_random]
                    num_random = random.randint(0, len(dineros_estimados) - 1)
                    dinero_estimado = dineros_estimados[num_random]
                    dinero_estimado = str(dinero_estimado)
                    num_random = random.randint(0, len(tipos_etapas) - 1)
                    tipo_etapa = tipos_etapas[num_random]

                    oportunidad = Clases.Oportunidad(nombre, informes_oportunidad, dinero_estimado, tipo_etapa)
                    Fun.guardar_oportunidad(oportunidad)
                    print("¡Oportunidad '{0}' guardada! Nombre: {1}".format(oportunidad.id, oportunidad.nombre))
            else:
                print("No quedan informes para generar oportunidades. Crea más informes.")
        else:
            print("Introduce un número mayor que 0")
    else:
        print("Saliendo del menú...")

def generar_informes_automatico():
    c = colores()
    print("Introduce cuantos informes quieres generar (o introduce 'salir')")
    cantidad = pedir_numero()
    if str(cantidad) != "salir":
        informes = Fun.cargar_datos_informes()
        actividades = Fun.cargar_datos_actividades()
        actividades_existentes = []
        for actividad in actividades:
            id = actividad.id
            for informe in informes:
                if informe.getActividad().id == id:
                    actividades_existentes.append(actividad)
        for actividad in actividades_existentes:
            actividades.remove(actividad)

        cantidad_antes = -4
        #cada informe tiene una actividad asi que miramos poder crear tantos informes como pide
        if cantidad > len(actividades):
            cantidad_antes = cantidad
            cantidad = len(actividades)
            if cantidad > 0:
                print("No se pueden crear {0} informes (no existen suficientes actividades), se generarán {1}".format(str(cantidad_antes), str(cantidad)))
        if cantidad > 0:
            clientes = Fun.cargar_datos_clientes()
            empleados = Fun.cargar_datos_empleados()
            x = 0
            while x < cantidad:
                for actividad in actividades:
                    if x < cantidad:
                        clientes_informe = []
                        empleados_informe = []

                        num_random = random.randint(1, 5)
                        i = 0
                        while i < num_random:
                            num_random2 = random.randint(0, (len(clientes) - 1))
                            anyadir = True
                            if len(clientes_informe) > 0:
                                for cliente in clientes_informe:
                                    if cliente.id == clientes[num_random2].id:
                                        anyadir = False
                            if anyadir:
                                clientes_informe.append(clientes[num_random2])
                                i += 1

                        num_random = random.randint(1, 5)
                        i = 0
                        while i < num_random:
                            num_random2 = random.randint(0, (len(empleados) - 1))
                            anyadir = True
                            if len(empleados_informe) > 0:
                                for empleado in empleados_informe:
                                    if empleado.id == empleados[num_random2].id:
                                        anyadir = False
                            if anyadir:
                                empleados_informe.append(empleados[num_random2])
                                i += 1

                        informe = Clases.Informe(actividad, clientes_informe, empleados_informe)
                        Fun.guardar_informe(informe)
                        print("¡Informe '{0}' guardado!".format(informe.getId()))

                    x += 1

        else:
            if cantidad_antes == -4:
                print("Introduce un número mayor que 0.")
            else:
                print("No quedan actividades para generar informes. Crea más actividades.")
    else:
        print("Saliendo del menú...")

def generar_actividades_automatico():
    c = colores()
    print("Introduce cuantas actividades quieres generar (o introduce 'salir')")
    cantidad = pedir_numero()
    if str(cantidad) != "salir":
        descripciones = ["Reunirse con el cliente para tratar determinados problemas",
                         "Asegurar que el progreso del proyecto es el adecuado",
                         "Afianzar el trato con el cliente",
                         "Buscar un enfoque nuevo para el proyecto",
                         "Contactar con el cliente para posibles nuevas sugerencias",
                         "Seguimiento del proyecto",
                         "Mostrar u ofrecer una versión beta",
                         "Comentar errores que posiblemente se mostrarán presentes"]
        fechas_planificacion = ["2019-07-10", "2019-08-10", "2019-09-10", "2019-10-10", "2019-11-10", "2019-12-10", "2020-01-10", "2020-02-10",
                                "2019-07-20", "2019-08-20", "2019-09-20", "2019-10-20", "2019-11-20", "2019-12-20", "2020-01-20", "2020-02-20",
                                "2019-07-30", "2019-08-30", "2019-09-30", "2019-10-30", "2019-11-30", "2019-12-30", "2020-01-30", "2020-02-25"]
        tiposactividad = [Clases.TipoActividad.Llamada, Clases.TipoActividad.Promocion, Clases.TipoActividad.Informe,
                          Clases.TipoActividad.Reunion]

        for i in range(0, cantidad):
            x = random.randint(0, (len(descripciones) - 1))
            descripcion = descripciones[x]

            x = random.randint(0, (len(fechas_planificacion) - 1))
            fecha_plan = fechas_planificacion[x]

            fecha_ven = datetime.datetime.strptime(fecha_plan, '%Y-%m-%d').date()
            fecha_ven = fecha_ven + dr.relativedelta(months=1)
            fecha_ven = str(fecha_ven)


            x = random.randint(0, (len(tiposactividad) - 1))
            tipoactividad = tiposactividad[x]

            actividad = Clases.Actividad(str(descripcion), str(fecha_ven), str(fecha_plan), tipoactividad)
            Fun.guardar_actividad(actividad)
            print("¡Actividad 'Plan: {0} - Ven: {1}' guardada! Desc: {2}".format(fecha_plan, fecha_ven, descripcion))
    else:
        print("Saliendo del menú...")

def generar_clientes_automatico():
    c = colores()
    print("Introduce cuantos clientes quieres generar (o introduce 'salir')")
    cantidad = pedir_numero()
    if str(cantidad) != "salir":
        dnis = ["72831820C", "39916219H", "60650728G", "00952975Q", "17740687M", "91256957H", "93855984E", "09518886Z"]
        nombres = ["Dani", "Lorena", "Kiana", "Elena", "Ekaitz", "Daniela", "Ander", "Sveta", "Mikel", "Santiago",
                   "Guillermo", "Gorka", "Alexsandro", "Irune", "Asier", "Gustavo"]
        apellidos = ["Tamargo", "Saiz", "Zamora", "Blanco", "Inverna", "Camargo", "Martínez",
                     "López", "Fernández", "Sanz", "Redondo", "Humilde", "Clásico", "Auto",
                     "Meliodas"]

        fechas_nac = ["1996-10-10", "1998-02-23", "1994-04-15", "1993-10-23", "1992-11-23", "1989-09-23", "1995-09-23"]

        tiposcliente = [Clases.TipoCliente.Proveedor, Clases.TipoCliente.Sponsor, Clases.TipoCliente.Cliente]

        for i in range(0, cantidad):
            x = random.randint(0, (len(dnis) - 1))
            dni = dnis[x]
            x = random.randint(0, (len(nombres) - 1))
            nombre = nombres[x]
            apellido = ""
            x = random.randint(0, (len(apellidos) - 1))
            apellido += apellidos[x]
            x = random.randint(0, (len(apellidos) - 1))
            apellido += " " + apellidos[x]
            email = str(nombre) + str(apellido) + "@gmail.com"
            email = email.replace(" ","")
            email = evitar_tildes(email)
            x = random.randint(0, (len(fechas_nac) - 1))
            fecha_nac = fechas_nac[x]
            x = random.randint(0, (len(tiposcliente) - 1))
            tipocliente = tiposcliente[x]

            cliente = Clases.Cliente(dni, nombre, apellido, email, fecha_nac, tipocliente)
            Fun.guardar_cliente(cliente)
            print("¡Cliente '{0} {1}' guardado!".format(nombre, apellido))
    else:
        print("Saliendo del menú...")


def generar_empleados_automatico():
    c = colores()
    print("Introduce cuantos empleados quieres generar (o introduce 'salir')")
    cantidad = pedir_numero()
    if str(cantidad) != "salir":
        dnis = ["72831820C", "39916219H", "60650728G", "00952975Q", "17740687M", "91256957H", "93855984E", "09518886Z"]
        nombres = ["Dani", "Lorena", "Kiana", "Elena", "Ekaitz", "Daniela", "Ander", "Sveta", "Mikel", "Santiago",
                   "Guillermo", "Gorka", "Alexsandro", "Irune", "Asier", "Gustavo"]
        apellidos = ["Tamargo", "Saiz", "Zamora", "Blanco", "Inverna", "Camargo", "Martínez",
                     "López", "Fernández", "Sanz", "Redondo", "Humilde", "Clásico", "Auto",
                     "Meliodas"]

        fechas_nac = ["1996-10-10", "1998-02-23", "1994-04-15", "1993-10-23", "1992-11-23", "1989-09-23", "1995-09-23"]
        fechas_contr = ["2018-09-10", "2019-09-10", "2019-10-10", "2019-12-10", "2019-04-20", "2019-11-23", "2019-02-04"]
        departamentos = [Clases.Departamento.Comercial, Clases.Departamento.Salud, Clases.Departamento.RRHH,
                         Clases.Departamento.Ventas, Clases.Departamento.Administrativo]

        for i in range(0, cantidad):
            x = random.randint(0, (len(dnis) - 1))
            dni = dnis[x]
            x = random.randint(0, (len(nombres) - 1))
            nombre = nombres[x]
            apellido = ""
            x = random.randint(0, (len(apellidos) - 1))
            apellido += apellidos[x]
            x = random.randint(0, (len(apellidos) - 1))
            apellido += " " + apellidos[x]
            email = str(nombre) + str(apellido[0:10]) + "@gmail.com"
            email = email.replace(" ","")
            email = evitar_tildes(email)
            x = random.randint(0, (len(fechas_nac) - 1))
            fecha_nac = fechas_nac[x]
            x = random.randint(0, (len(fechas_contr) - 1))
            fecha_contr = fechas_contr[x]
            x = random.randint(0, (len(departamentos) - 1))
            departamento = departamentos[x]

            empleado = Clases.Empleado(dni, nombre, apellido, email, fecha_nac, departamento, fecha_contr)
            Fun.guardar_empleado(empleado)
            print("¡Empleado '{0} {1}' guardado!".format(nombre, apellido))
    else:
        print("Saliendo del menú...")