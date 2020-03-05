import colorama
import Archivos.Funciones.CargarDatos as cd
import Archivos.Clases as Clases
import Archivos.Funciones.GuardarModificarDatos as gm
import Archivos.Funciones.Logs as Logs
import Archivos.Funciones.CrearPDF as pdf_t
import smtplib
import ssl


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

#----------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------         VARIOS          ---------------------------------------------- #
#----------------------------------------------------------------------------------------------------------------------#

def email():
    # Este método sirve para pedir un email, comprueba que es válido y lo devuelve
    # Compruebo muchas cosas pero no establezco restricciones de longitud ni mínimas ni máximas
    # Iba a comprobar que no tuviera caracteres especiales (simbolos) pero un blog dice que son validos: http://preguntascojoneras.blogspot.com/2015/01/caracteres-validos-en-un-email.html
    valido = False
    email = ""
    while valido == False:
        email = input("Introduce el email al que enviar la factura: ")
        if email is not None and email != "":
            if "@" in email:
                # dominio = str(email.lstrip("@")) # lstrip no funciona como yo pensaba, es bastante más particular
                # así que opto por otra forma de hacerlo, averiguo la posición, y examino el dominio
                # compruebo que solo existe un @ y que el email no comience dierctamente por el @
                if email.find("@") == email.rfind("@") and email.find("@") > 0:
                    dominio = email[(email.find("@") + 1):len(email)]
                    if "." in dominio:
                        # para ver si el dominio termina bien, busco el último punto, a veces hay más de un punto, por ejemplo:
                        # daniel.tamargo@ikasle.egibide.org
                        # también compruebo que el punto no esté situado al final, el dominio no puede acabar en punto
                        # también compruebo que tras la @ no haya un punto
                        if dominio.rfind(".") < len(dominio) - 1 and dominio.find(".") > 0:
                            fin_dominio = dominio[(dominio.rfind(".") + 1):len(dominio)]
                            lista_finales_dominios = ["es", "com", "org", "net", "edu", "us", "me", "biz", "tk", "eu"] # Podría ser una lista eterna
                            if fin_dominio in lista_finales_dominios:
                                valido = True
                            else:
                                respuesta = ""
                                while respuesta == "":
                                    respuesta = input(colorama.Fore.LIGHTMAGENTA_EX + "'" + fin_dominio + "'" + colorama.Fore.RESET
                                                      + " es una terminación de dominio que no tenemos registrada. ¿Quieres guardarlo así? (s/n): ")
                                    if respuesta is not None or respuesta != "":
                                        respuesta = respuesta.lower()
                                        if respuesta == "s":
                                            valido = True
                                        elif respuesta == "n":
                                            print("Vuelve a introducir tu email.")
                                        else:
                                            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                                                  + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
                                    else:
                                        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                                              + colorama.Style.RESET_ALL + " No has introducido un nada :(")
                        else:
                            if dominio.find(".") == 0:
                                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                                      + colorama.Style.RESET_ALL + " El dominio no puede comenzar por un punto.")
                            else:
                                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                                      + colorama.Style.RESET_ALL + " El dominio no puede acabar en un punto.")
                    else:
                        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                              + colorama.Style.RESET_ALL + " El dominio no es válido (falta el punto).")
                else:
                    if email.find("@") == 0:
                        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                              + colorama.Style.RESET_ALL + " No has introducido un email válido (no puede empezar por @).")
                    else:
                        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                              + colorama.Style.RESET_ALL + " No has introducido un email válido (existe más de un @).")
            else:
                print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                      + colorama.Style.RESET_ALL + " No has introducido un email válido (falta el @).")
        else:
            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                  + colorama.Style.RESET_ALL + " No has introducido un nada :(")
        print()

    return email

def enviar_email(linea, email):
    # Este método utiliza mi cuenta de correo del instituto para enviar un correo al email introducido con todos sus datos
    print("Intentando mandar el correo...", end="")
    # https://realpython.com/python-send-email/
    port = 465
    password = "JxGEWWue"
    gmail = "daniel.tamargo@ikasle.egibide.org"

    # Está así para que aparezca bien quien lo envía, cual es el asunto y el cuerpo del email
    mensaje = """\
    From: Artic Gaming\nSubject: Factura de tu pedido\n\n   Vea el archivo PDF adjunto al correo.:

    Muchas gracias por su compra. Esperamos volver a verle de nuevo."""

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(gmail, password)

        server.sendmail(gmail, email, mensaje)

    print(colorama.Fore.LIGHTGREEN_EX + "\r¡Correo enviado!" + colorama.Fore.RESET)

def preguntar_mandar_email(venta, email):
    # Este método existe para dar la opción de enviar o no enviar el email, por ejemplo si has puesto una direccion
    # falsa o no existente, seleccionas no enviarlo y no habrá problemas
    mandarlo = False
    respuesta = input("¿Enviar un email al correo que has indicado con los datos de la venta? (s/n): ")
    if respuesta != "" and respuesta is not None:
        respuesta = respuesta.lower()[0]
        if respuesta == "s" or respuesta == "n":
            if respuesta == "s":
                # Creamos el PDF y enviamos el correo
                pdf_t.crearPDF(venta)
                enviar_email(usuario, contrasenya, email)
            else:
                print("Perfecto, entonces no mandaremos el email.")
        else:
            print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
                  + colorama.Style.RESET_ALL + " Debes introducir S o N para marcar Sí o No.")
    else:
        print(colorama.Fore.LIGHTRED_EX + colorama.Style.BRIGHT + "¡Error!"
              + colorama.Style.RESET_ALL + " No has introducido un nada :(")

#----------------------------------------------------------------------------------------------------------------------#
# ------------------------------------------- MENÚ Y OPCIONES PROVEEDORES -------------------------------------------- #
#----------------------------------------------------------------------------------------------------------------------#
def opcion_nuevo_proveedor():


def menu_productos(boolean_logout):
    c = colores()
    while True:
        print(c["lm"] + c["*"] + "Menú Proveedores" + c["rst"])
        print("1. Registrar nuevo proveedor.")
        print("2. Modificar proveedor (W.I.P.).")
        if boolean_logout:
            print("3. Cerrar sesión.")
        else:
            print("3. Salir del menú de ventas.")
        eleccion = input("Opción: ")
        try:
            eleccion = int(eleccion)
        except:
            print("{0}Error.{1} Debes introducir el número de la opción.\n".format(c["lr"], c["rst"]))
            eleccion = -12131415
        if eleccion != -12131415:
            if eleccion > 0 and eleccion < 4:
                print("submenússss")




            else:
                print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
        print()



#----------------------------------------------------------------------------------------------------------------------#
# -------------------------------------------- MENÚ Y OPCIONES PRODUCTOS --------------------------------------------- #
#----------------------------------------------------------------------------------------------------------------------#

def menu_productos(usuario_loggeado, boolean_logout):
    c = colores()
    while True:
        print(c["lm"] + c["*"] + "Menú Productos" + c["rst"])
        print("1. Registrar nuevo producto.")
        print("2. Descatalogar producto.")
        print("3. Eliminar producto.")
        if boolean_logout:
            print("4. Cerrar sesión.")
        else:
            print("4. Salir del menú de ventas.")
        eleccion = input("Opción: ")
        try:
            eleccion = int(eleccion)
        except:
            print("{0}Error.{1} Debes introducir el número de la opción.\n".format(c["lr"], c["rst"]))
            eleccion = -12131415
        if eleccion != -12131415:
            if eleccion > 0 and eleccion < 5:
                print("submenússss")




            else:
                print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
        print()


#----------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------- MENÚ Y OPCIONES VENTAS  ---------------------------------------------- #
#----------------------------------------------------------------------------------------------------------------------#
def mostrar_lista_ventas(usuario_loggeado, ventas):
    print("Lista de ventas:")
    indice = 1
    for venta in ventas:
        print("{0}. {1}".format(str(indice), str(venta)))
        indice += 1

def seleccionar_venta_de_lista(ventas):
    eleccion = - 1
    while eleccion < 0 or eleccion >= len(ventas):
        eleccion = input("Selecciona una venta: ")
        try:
            eleccion = int(eleccion) - 1
        except:
            eleccion = -1
        if eleccion < 0 or eleccion >= len(ventas):
            print("{0}Error.{1} Tienes que seleccionar una venta de la lista.".format(c["lr"], c["rst"]))
        print()
    return eleccion

def opcion_consultar_ventas():
    c = colores()
    # Seleccionar una venta de la lista y mostrar los productos
    ventas = cd.cargar_datos_ventas()
    bucle = True
    while bucle:
        print("Selecciona una venta para ver la lista de productos vendidos que le corresponde.")
        mostrar_lista_ventas(ventas)
        eleccion = seleccionar_venta_de_lista()

        venta = ventas[eleccion]
        productos = venta.productos
        print("Lista de productos de la venta:")
        indice = 0
        for producto in productos:
            print("{0}. {1}".format(str(indice), str(producto)))
        print()

        respuesta = ""
        while respuesta != "s" or respuesta != "n":
            print("¿Quieres consultar otra venta?")
            respuesta = input("Respuesta (s/n): ")
            try:
                respuesta = respuesta[0:1].lower()
            except:
                respuesta = ""
            if respuesta != "s" or respuesta != "n":
                print("¡Tienes que introducir {0}sí{1} o {2}no{3}!".format(c["lc"], c["rst"], c["lc"], c["rst"]))
            print()
        if respuesta == "n":
            bucle = False


def opcion_enviar_factura():
    ventas = cd.cargar_datos_ventas()
    print("Selecciona una venta para enviar la factura correspondiente por e-mail")
    mostrar_lista_ventas(ventas)
    eleccion = seleccionar_venta_de_lista(ventas)
    venta = ventas[eleccion]
    respuesta = ""
    while respuesta != "s" or respuesta != "n":
        print("¿Quieres enviar la venta seleccionada por correo?")
        respuesta = input("Respuesta (s/n): ")
        try:
            respuesta = respuesta[0:1].lower()
        except:
            respuesta = ""
        if respuesta != "s" or respuesta != "n":
            print("¡Tienes que introducir {0}sí{1} o {2}no{3}!".format(c["lc"], c["rst"], c["lc"], c["rst"]))
        print()
    if respuesta == "s":
        email = email()




    else:
        print("Cancelando el envío del email...")
    print()

def opcion_nueva_venta(usuario_loggeado):
    c = colores()
    productos = cd.cargar_datos_productos()
    productos_en_venta = []
    productos_seleccionados = []

    for producto in productos:
        if producto.estatus_producto.name == "Activo":
            productos_en_venta.append(producto)

    if len(productos_en_venta) > 0:
        anyadir_mas_productos = True
        while anyadir_mas_productos:


            eleccion = -1
            while eleccion < 0 or eleccion >= len(productos_en_venta):
                print("Elige el producto que se va a vender:")
                indice = 1
                for producto in productos_en_venta:
                    print("{0}. {1}".format(str(indice), str(producto)))
                    indice += 1
                eleccion = input("Elección: ")
                try:
                    eleccion = int(eleccion) - 1
                except:
                    eleccion = -12131415
                    print("{0}Error.{1} Tienes que seleccionar un producto de la lista.\n".format(c["lr"], c["rst"]))
                if eleccion != -12131415:
                    if eleccion >= 0 and eleccion < len(productos_en_venta):
                        productos_seleccionados.append(productos_en_venta[eleccion]) # <- se añade el producto producto!
                        print("¡Producto añadido!")
                print()
                if len(productos_seleccionados) > 0:
                    respuesta = ""
                    while respuesta != "s" or respuesta != "n":
                        print("¿Quieres añadir más productos a la venta?")
                        respuesta = input("Opción (s/n): ")
                        try:
                            respuesta = respuesta[0]
                        except:
                            respuesta = ""
                        if respuesta != "s" or respuesta != "n":
                            print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
                        print()
                    if respuesta == "n":
                        anyadir_mas_productos = False

        clientes = cd.cargar_datos_clientes()
        eleccion = -1
        while eleccion < 0 or eleccion >= len(clientes):
            print("Elige el cliente al que se le realiza la venta:")
            indice = 1
            for cliente in clientes:
                print("{0}. {1}".format(str(indice), str(cliente)))
                indice += 1
            eleccion = input("Elección: ")
            try:
                eleccion = int(eleccion) - 1
            except:
                eleccion = -12131415
                print("{0}Error.{1} Tienes que seleccionar un cliente de la lista.\n".format(c["lr"], c["rst"]))
            if eleccion != -12131415:
                if eleccion >= 0 and eleccion < len(clientes):
                    cliente_seleccionado = clientes[eleccion]

        nueva_venta = Clases.Venta(productos_seleccionados, cliente_seleccionado, usuario_loggeado.empleado, None, None)
        gm.guardar_venta(nueva_venta)
        print(c["lc"] + "¡Venta creada correctamente!" + c["rst"])
    else:
        print("{0}¡Hey!{1} No existen productos o están todos descatalogados.\n".format(c["lr"], c["rst"]))

def menu_ventas(usuario_loggeado, boolean_logout):
    c = colores()
    menu = True
    while menu:
        print(c["lm"] + c["*"] + "Menú Ventas" + c["rst"])
        print("1. Realizar una nueva venta.")
        print("2. Consultar productos de una venta.")
        print("3. Enviar factura por e-mail al cliente.")
        if boolean_logout:
            print("4. Cerrar sesión.")
        else:
            print("4. Salir del menú de ventas.")
        eleccion = input("Opción: ")
        try:
            eleccion = int(eleccion)
        except:
            print("{0}Error.{1} Debes introducir el número de la opción.\n".format(c["lr"], c["rst"]))
            eleccion = -12131415
        if eleccion != -12131415:
            if eleccion > 0 and eleccion < 5:
                if eleccion == 1:
                    opcion_nueva_venta(usuario_loggeado)
                elif eleccion == 2:
                    opcion_consultar_ventas()
                elif eleccion == 3:
                    opcion_enviar_factura()
                else:
                    menu = False
                    if boolean_logout is True:
                        print("Cerrando sesión...")
                    else:
                        print("Volviendo atrás en el menú")
                    print()
            else:
                print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
        print()
    