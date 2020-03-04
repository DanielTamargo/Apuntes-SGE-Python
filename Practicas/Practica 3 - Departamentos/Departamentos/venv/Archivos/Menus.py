import colorama
import Archivos.Funciones.CargarDatos as cd
import Archivos.Clases as Clases
import Archivos.Funciones.GuardarModificarDatos as gm

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





def menu_productos(boolean_logout):
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
def opcion_consultar_ventas():
    print("mostrar todas las ventas y a tomar por culo")

def opcion_enviar_factura():
    print("Seleccionar una venta de la lista y enviarla como factura al cliente, real o ficticio, depende del tiempo")

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

        nueva_venta = Clases.Venta(productos_seleccionados, cliente_seleccionado, usuario_loggeado.empleado)
        gm.guardar_venta(nueva_venta)
        print(c["lc"] + "¡Venta creada correctamente!" + c["rst"])
    else:
        print("{0}¡Hey!{1} No existen productos o están todos descatalogados.\n".format(c["lr"], c["rst"]))

def menu_ventas(usuario_loggeado, boolean_logout):
    c = colores()
    while True:
        print(c["lm"] + c["*"] + "Menú Ventas" + c["rst"])
        print("1. Realizar una nueva venta.")
        print("2. Consultar ventas realizadas.")
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
                print("submenússss")
                
                
                
                
            else:
                print("{0}¡Ups!{1} No te he entendido :(\n".format(c["lr"], c["rst"]))
        print()
    