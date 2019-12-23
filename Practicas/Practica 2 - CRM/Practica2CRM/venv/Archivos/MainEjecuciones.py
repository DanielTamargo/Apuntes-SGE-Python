import datetime
import Clases as Clases
import Funciones as Fun
import MiBot

import colorama
import re

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import os
import time
import playsound
#import speech_recognition as sr
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
    print(c["lm"] + c["*"] + "Menú" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Empleados")
    print(c["lm"] + "2. " + c["lc"] + "Clientes")
    print(c["lm"] + "3. " + c["lc"] + "Actividades")
    print(c["lm"] + "4. " + c["lc"] + "Informes (y gráficos).")
    print(c["lm"] + "5. " + c["lc"] + "Extras.")
    print(c["lm"] + "6. " + c["lc"] + "Salir." + c["rst"])
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
    print(c["lm"] + "3. " + c["lc"] + "Eliminar informe")
    print(c["lm"] + "4. " + c["lc"] + "Mostrar informe (gráficas)" + c["rst"])
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
    # Por defecto, se crea la actividad en la etapa "nueva"

    # Quito las comas porque fastidiarían el sistema de recogida de datos del fichero.
    actividad = Clases.Actividad(descripcion.replace(",",""), str(fecha_vencimiento), str(fecha_planificacion),
                               tipoactividad)
    Fun.guardar_actividad(actividad)
    print(c["lc"] + "¡Actividad creada correctamente!" + c["rst"])

def opcion_modificar_actividad():
    c = colores()
    print(c["lc"] + "Selecciona el actividad a modificar (o introduce 'salir')")
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
            tipos_etapas = {"1": Clases.TipoEtapa.Nueva, "2": Clases.TipoEtapa.Propuesta,
                            "3": Clases.TipoEtapa.Calificada, "4": Clases.TipoEtapa.Ganada,
                            "5": Clases.TipoEtapa.Suspendida}
            respuesta = ""
            while respuesta == "":
                print("Elige la etapa en la que se encuentra la actividad:")
                print("1. Nueva")
                print("2. Propuesta")
                print("3. Calificada")
                print("4. Ganada")
                print("5. Suspendida")
                respuesta = input("Tipo de etapa: ")
                if respuesta in tipos_etapas:
                    tipoetapa = tipos_etapas[respuesta]
                    if tipoetapa == actividad.tipoetapa:
                        respuesta = ""
                else:
                    respuesta = ""
                if respuesta == "":
                    if tipoetapa == actividad.tipoetapa:
                        print("{0}¡Ey!{1} Estás volviendo a poner la etapa en la que ya estaba la actividad\n".format(c["lr"], c["rst"]))
                    else:
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
            print()
            print("{0}Estás a punto de guardar los cambios modificando a:{1} {2}{3}".format(c["lc"], c["ly"], str(actividad), c["rst"]))
            respuesta = ""
            while respuesta == "":
                respuesta = input("¿Modificar? (s/n): ")
                if respuesta != "":
                    respuesta = respuesta.lower()[0]
                    if respuesta == "s":
                        actividad.tipoetapa = tipoetapa
                        Fun.modificar_actividad(actividad)
                        print(c["lc"] + "¡Actividad modificada correctamente!" + c["rst"])
                    elif respuesta == "n":
                        print(c["lc"] + "Okay. " + c["rst"] + "La actividad no será modificada")
                    else:
                        respuesta = ""
                        print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                else:
                    print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
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
            lista_empleados_informe = []

            empleados = Fun.cargar_datos_empleados()
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
                    correcto = True

            correcto = False
            lista_clientes_informe = []
            while not correcto:
                print(c["lc"] + "Selecciona un cliente para que aparezca en el informe (o introduce 'salir'):" + c["rst"])
                clientes = Fun.cargar_datos_clientes()
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
                    correcto = True
            informe = Clases.Informe(actividad, lista_clientes_informe, lista_empleados_informe)
            Fun.guardar_informe(informe)
            print(c["lc"] + "¡Informe creado correctamente!" + c["rst"])
        else:
            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")


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
                        while not correcto:
                            print(c["lc"] + "Selecciona un empleado que administre el informe (o introduce 'salir'):" + c["rst"])
                            empleados = Fun.cargar_datos_empleados()
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
                        while not correcto:
                            print(c["lc"] + "Selecciona un cliente para que aparezca en el informe (o introduce 'salir'):" + c["rst"])
                            clientes = Fun.cargar_datos_clientes()
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

def opcion_eliminar_informe():
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


def grafico_empleadosyclientes():
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


def opcion_mostrar_graficos():
    c = colores()
    print(c["lc"] + "Elige el tipo de gráfico (o introduce 'salir')" + c["rst"])
    print(c["lm"] + "1. " + c["lc"] + "Clientes y empleados por informe")
    print(c["lm"] + "2. " + c["lc"] + "Actividades en los últimos 4 meses" + c["rst"])
    eleccion = pedir_numero()
    if str(eleccion) != "salir":
        if int(eleccion) == 1:
            grafico_empleadosyclientes()
        elif int(eleccion) == 2:
            wip()
        else:
            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
    else:
        print("Saliendo del menú...")

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