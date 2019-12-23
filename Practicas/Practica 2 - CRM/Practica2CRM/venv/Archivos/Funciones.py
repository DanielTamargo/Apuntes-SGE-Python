import Archivos.Clases as Clases
import datetime
import random

# Carga la lista de clientes del fichero (o los datos base creados para pruebas)
def cargar_datos_clientes():
    clientes = []
    with open('Datos/Clientes.txt') as f:
        lineas = [line.rstrip('\n') for line in f]
        for linea in lineas:
            datos = linea.split(",")
            if datos[6] == "Sponsor":
                tipocliente = Clases.TipoCliente.Sponsor
            elif datos[6] == "Proveedor":
                tipocliente = Clases.TipoCliente.Proveedor
            else:
                tipocliente = Clases.TipoCliente.Cliente
            cliente = Clases.Cliente(datos[1],datos[2],datos[3],
                                     datos[4],datos[5],tipocliente,datos[0])
            clientes.append(cliente)

    return clientes

def cargar_datos_empleados():
    empleados = []
    with open('Datos/Empleados.txt') as f:
        lineas = [line.rstrip('\n') for line in f]
        for linea in lineas:
            datos = linea.split(",")
            if datos[6] == "Administrativo":
                departamento = Clases.Departamento.Administrativo
            elif datos[6] == "Ventas":
                departamento = Clases.Departamento.Ventas
            elif datos[6] == "RRHH":
                departamento = Clases.Departamento.RRHH
            elif datos[6] == "Salud":
                departamento = Clases.Departamento.Salud
            else:
                departamento = Clases.Departamento.Comercial
            empleado = Clases.Empleado(datos[1], datos[2], datos[3], datos[4], datos[5], departamento,
                                       datos[7], datos[0])
            empleados.append(empleado)

    return empleados

def cargar_datos_actividades():
    actividades = []
    with open('Datos/Actividades.txt') as f:
        lineas = [line.rstrip('\n') for line in f]
        for linea in lineas:
            datos = linea.split(",")
            if datos[4] == "Llamada":
                tipoactividad = Clases.TipoActividad.Llamada
            elif datos[4] == "Promocion":
                tipoactividad = Clases.TipoActividad.Promocion
            elif datos[4] == "Informe":
                tipoactividad = Clases.TipoActividad.Informe
            else:
                tipoactividad = Clases.TipoActividad.Reunion

            if datos[5] == "Propuesta":
                tipoetapa = Clases.TipoEtapa.Propuesta
            elif datos[5] == "Calificado":
                tipoetapa = Clases.TipoEtapa.Calificado
            elif datos[5] == "Ganada":
                tipoetapa = Clases.TipoEtapa.Ganada
            elif datos[5] == "Suspendida":
                tipoetapa = Clases.TipoEtapa.Suspendida
            else:
                tipoetapa = Clases.TipoEtapa.Nueva
            
            actividad = Clases.Actividad(datos[1], datos[2], datos[3], tipoactividad, tipoetapa, datos[0])
            actividades.append(actividad)

    return actividades

def cargar_datos_informes():

    clientes = cargar_datos_clientes()
    empleados = cargar_datos_empleados()
    actividades = cargar_datos_actividades()

    informes = []
    with open('Datos/Informes.txt') as f:
        lineas = [line.rstrip('\n') for line in f]
        for linea in lineas:
            id_informe = linea[0:linea.find(",")]
            id_actividad = linea[(linea.find(",") + 1):(linea.find("(") - 1)]
            ids_clientes_informe = linea[(linea.find("(") + 1):linea.find(")")].split(",")
            ids_empleados_informe = linea[(linea.rfind("(") + 1):linea.rfind(")")].split(",")
            informe = Clases.Informe(None, None, None, id_informe)

            actividad = ""
            for act in actividades:
                if id_actividad == act.id:
                    actividad = act
            informe.setActividad(actividad)

            empleados_informe = []
            for id_emp_informe in ids_empleados_informe:
                for emple in empleados:
                    if id_emp_informe == emple.id:
                        empleados_informe.append(emple)
            informe.setEmpleados(empleados_informe)

            clientes_informe = []
            for id_clien_informe in ids_clientes_informe:
                for clien in clientes:
                    if id_clien_informe == clien.id:
                        clientes_informe.append(clien)
            informe.setClientes(clientes_informe)

            #informe = Clases.Informe(actividad, clientes, empleados, id_informe)
            informes.append(informe)

    return informes

def guardar_cliente(cliente):
    linea = "{0},{1},{2},{3},{4},{5},{6}".format(str(cliente.id),str(cliente.dni),str(cliente.nombre),
                                                 str(cliente.apellidos),str(cliente.email),
                                                 str(cliente.fecha_nacimiento),str(cliente.tipocliente.name))
    f = open("Datos/Clientes.txt", "a+") # <- a significa que es para añadir (append) líneas al final, no sobreescribe
    f.write("\n" + linea)
    f.close()

def guardar_empleado(empleado):
    linea = "{0},{1},{2},{3},{4},{5},{6},{7}".format(str(empleado.id),str(empleado.dni),str(empleado.nombre),
                                                 str(empleado.apellidos),str(empleado.email),
                                                 str(empleado.fecha_nacimiento),str(empleado.departamento.name),
                                                 str(empleado.fecha_contratacion))
    f = open("Datos/Empleados.txt", "a+") # <- a significa que es para añadir (append) líneas al final, no sobreescribe
    f.write("\n" + linea)
    f.close()

def guardar_actividad(actividad):
    linea = "{0},{1},{2},{3},{4},{5}".format(str(actividad.id),str(actividad.descripcion),str(actividad.fecha_vencimiento),
                                                 str(actividad.fecha_planificacion),str(actividad.tipoactividad.name),
                                                 str(actividad.tipoetapa.name))
    f = open("Datos/Actividades.txt", "a+") # <- a significa que es para añadir (append) líneas al final, no sobreescribe
    f.write("\n" + linea)
    f.close()

# Genera una línea (string) para guardarla en el fichero informes.
def linea_informe(informe):
    id = str(informe.getId)
    actividad = str(informe.getActividad.id)

    clientes = ""
    if len(informe.getClientes) > 0:
        for clien in informe.getClientes:
            clientes += "," + str(clien.id)
        clientes = clientes[(clientes.find(",") + 1):]
    clientes = "(" + clientes + ")"

    empleados = ""
    if len(informe.getEmpleados) > 0:
        for emple in informe.getEmpleados:
            empleados += "," + str(emple.id)
        empleados = empleados[(empleados.find(",") + 1):]
    empleados = "(" + empleados + ")"

    linea = id + "," + actividad + "," + clientes + "," + empleados
    return linea

def guardar_informe(informe):
    linea = linea_informe(informe)
    f = open("Datos/Informes.txt", "a+")  # <- a significa que es para añadir (append) líneas al final, no sobreescribe
    f.write("\n" + linea)
    f.close()

def modificar_informe(informe):
    linea_a_modificar = linea_informe(informe)
    posicion = 0

    with open('Datos/Informes.txt') as f:
        x = 0
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == informe.getId:
                posicion = x
            x += 1
    # f.close()

    with open('Datos/Informes.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == posicion:
                linea = linea_a_modificar
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1

def modificar_cliente(cliente):
    linea_a_modificar = "{0},{1},{2},{3},{4},{5},{6}".format(str(cliente.id),str(cliente.dni),str(cliente.nombre),
                                                 str(cliente.apellidos),str(cliente.email),
                                                 str(cliente.fecha_nacimiento),str(cliente.tipocliente.name))
    posicion = 0

    with open('Datos/Clientes.txt') as f:
        x = 0
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == cliente.id:
                posicion = x
            x += 1
    # f.close()

    with open('Datos/Clientes.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == posicion:
                linea = linea_a_modificar
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1

def modificar_empleado(empleado):
    linea_a_modificar = "{0},{1},{2},{3},{4},{5},{6},{7}".format(str(empleado.id),str(empleado.dni),str(empleado.nombre),
                                                 str(empleado.apellidos),str(empleado.email),
                                                 str(empleado.fecha_nacimiento),str(empleado.departamento.name),
                                                 str(empleado.fecha_contratacion))
    posicion = 0

    with open('Datos/Empleados.txt') as f:
        x = 0
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == empleado.id:
                posicion = x
            x += 1
    # f.close()

    with open('Datos/Empleados.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == posicion:
                linea = linea_a_modificar
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1

def modificar_actividad(actividad):
    linea_a_modificar = "{0},{1},{2},{3},{4},{5}".format(str(actividad.id),str(actividad.descripcion),str(actividad.fecha_vencimiento),
                                                 str(actividad.fecha_planificacion),str(actividad.tipoactividad.name),
                                                 str(actividad.tipoetapa.name))
    posicion = 0

    with open('Datos/Actividades.txt') as f:
        x = 0
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == actividad.id:
                posicion = x
            x += 1
    # f.close()

    with open('Datos/Actividades.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == posicion:
                linea = linea_a_modificar
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1


def borrar_informe(informe):
    with open('Datos/Informes.txt') as f:
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == informe.getId:
                # linea_a_modificar = linea
                lista_lineas.remove(linea)
    # f.close()

    # lista_lineas.remove(linea_a_modificar)

    with open('Datos/Informes.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1


# Elimina el cliente de los informes en los que aparezca (y guarda los cambios en el fichero)
def borrar_cliente_de_informes(cliente):
    informes = cargar_datos_informes()
    for informe in informes:
        clientes = informe.getClientes()
        if cliente in clientes:
            informe.getClientes.remove(cliente)
            modificar_informe(informe)

# Elimina el empleado de los informes en los que aparezca (y guarda los cambios en el fichero)
def borrar_empleado_de_informes(empleado):
    informes = cargar_datos_informes()
    for informe in informes:
        empleados = informe.getEmpleados()
        if empleado in empleados:
            empleados.remove(empleado)
            modificar_informe(informe)

# Elimina los informes relacionados con una actividad (y guarda los cambios en el fichero)
def borrar_informes_de_actividad(actividad):
    informes = cargar_datos_informes()
    for informe in informes:
        if actividad in informe:
            borrar_informe(informe)
            informes.remove(informe)

def borrar_cliente(cliente):
    with open('Datos/Clientes.txt') as f:
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == cliente.id:
                # linea_a_modificar = linea
                lista_lineas.remove(linea)
    # f.close()

    # lista_lineas.remove(linea_a_modificar)

    with open('Datos/Clientes.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1

    # Imitando "ON DELETE CASCADE" eliminamos al cliente de aquellos informes en los que aparezca.
    borrar_cliente_de_informes(cliente)


def borrar_empleado(empleado):
    with open('Datos/Empleados.txt') as f:
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == empleado.id:
                # linea_a_modificar = linea
                lista_lineas.remove(linea)
    # f.close()

    # lista_lineas.remove(linea_a_modificar)

    with open('Datos/Empleados.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1

    # Imitando "ON DELETE CASCADE" eliminamos al empleado de aquellos informes en los que aparezca.
    borrar_empleado_de_informes(empleado)


def borrar_actividad(actividad):
    with open('Datos/Actividades.txt') as f:
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == empleado.id:
                # linea_a_modificar = linea
                lista_lineas.remove(linea)
    # f.close()

    # lista_lineas.remove(linea_a_modificar)

    with open('Datos/Actividades.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1

    # Si se elimina la actividad, el informe también. Puesto que el informe basa sus datos en la actividad.


# Genera y devuelve un id (string) de 5 caracteres aleatorios
def generar_id():
    abc = "abcdefghijklmnopqrstuvwxyz"
    nums = "1234567890"
    #simbs = "!¡?¿=_-+*^'"  # <- para los id no voy a usar símbolos
    id = ""
    while len(id) < 5:
        x = random.randint(1, 3)
        if x == 1:
            x = random.randint(0, (len(abc) - 1))
            id += abc[x]
        elif x == 2:
            x = random.randint(0, (len(abc) - 1))
            id += abc.upper()[x]
        elif x == 3:
            x = random.randint(0, (len(nums) - 1))
            id += nums[x]
    return id

# Recorre una lista, ya sea de clientes, empleados o actividades, buscando si el id existe o no, devuelve un boolean.
# Devuelve True si el id es válido (único), y False si el id ya existe.
def comprobar_id(id, lista):
    for valor in lista:
        if id == valor.id:
            return False
    return True

# Utiliza la función generar_id y comprueba el id generado para ver que no existe, si no existe, lo asigna
# Para saber si el id existe o no, utiliza la función comprobar_id
def generar_id_cliente():
    clientes = cargar_datos_clientes()
    while True:
        id = generar_id()
        if comprobar_id(id, clientes):
            return id

# Funciona igual que generar_id_cliente
def generar_id_actividad():
    actividades = cargar_datos_actividades()
    while True:
        id = generar_id()
        if comprobar_id(id, actividades):
            return id

# Funciona igual que generar_id_cliente
def generar_id_empleado():
    empleados = cargar_datos_empleados()
    while True:
        id = generar_id()
        if comprobar_id(id, empleados):
            return id

# Funciona igual que generar_id_cliente
def generar_id_informe():
    informes = cargar_datos_informes()
    while True:
        id = generar_id()
        if comprobar_id(id, informes):
            return id


