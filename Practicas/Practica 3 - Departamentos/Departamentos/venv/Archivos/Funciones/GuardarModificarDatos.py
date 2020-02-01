def guardar_cliente(cliente):
    linea = "{0},{1},{2},{3},{4},{5},{6}".format(str(cliente.id),str(cliente.dni),str(cliente.nombre),
                                                 str(cliente.apellidos),str(cliente.email),
                                                 str(cliente.fecha_nacimiento),str(cliente.tipocliente.name))
    f = open("Datos/Clientes.txt", "a+") # <- a significa que es para añadir (append) líneas al final, no sobreescribe
    f.write("\n" + linea)
    f.close()
#-----------------------------------------------------------------------------------------------------------------------
def guardar_empleado(empleado):
    linea = "{0},{1},{2},{3},{4},{5},{6},{7}".format(str(empleado.id),str(empleado.dni),str(empleado.nombre),
                                                 str(empleado.apellidos),str(empleado.email),
                                                 str(empleado.fecha_nacimiento),str(empleado.departamento.name),
                                                 str(empleado.fecha_contratacion))
    f = open("Datos/Empleados.txt", "a+") # <- a significa que es para añadir (append) líneas al final, no sobreescribe
    f.write("\n" + linea)
    f.close()
#-----------------------------------------------------------------------------------------------------------------------
def guardar_actividad(actividad):
    linea = "{0},{1},{2},{3},{4}".format(str(actividad.id),str(actividad.descripcion),str(actividad.fecha_vencimiento),
                                                 str(actividad.fecha_planificacion),str(actividad.tipoactividad.name))
    f = open("Datos/Actividades.txt", "a+") # <- a significa que es para añadir (append) líneas al final, no sobreescribe
    f.write("\n" + linea)
    f.close()
#-----------------------------------------------------------------------------------------------------------------------
# Genera una línea (string) para guardarla en el fichero informes.
def linea_informe(informe):
    id = str(informe.getId())
    actividad = str(informe.getActividad().id)

    clientes = ""
    if len(informe.getClientes()) > 0:
        for clien in informe.getClientes():
            clientes += "," + str(clien.id)
        clientes = clientes[(clientes.find(",") + 1):]
    clientes = "(" + clientes + ")"

    empleados = ""
    if len(informe.getEmpleados()) > 0:
        for emple in informe.getEmpleados():
            empleados += "," + str(emple.id)
        empleados = empleados[(empleados.find(",") + 1):]
    empleados = "(" + empleados + ")"

    linea = id + "," + actividad + "," + clientes + "," + empleados
    return linea
#-----------------------------------------------------------------------------------------------------------------------
def guardar_informe(informe):
    linea = linea_informe(informe)
    f = open("Datos/Informes.txt", "a+")  # <- a significa que es para añadir (append) líneas al final, no sobreescribe
    f.write("\n" + linea)
    f.close()
#-----------------------------------------------------------------------------------------------------------------------
def linea_oportunidad(oportunidad):
    id = str(oportunidad.id)
    nombre = str(oportunidad.nombre)
    dinero_estimado = str(oportunidad.dinero_estimado)
    tipoetapa = str(oportunidad.tipoetapa.name)

    informes = ""
    if len(oportunidad.informes) > 0:
        for informe in oportunidad.informes:
            informes += "," + str(informe.getId())
        informes = informes[(informes.find(",") + 1):]
    informes = "(" + informes + ")"

    linea = id + "," + nombre + "," + informes + "," + dinero_estimado + "," + tipoetapa
    return linea
#-----------------------------------------------------------------------------------------------------------------------
def guardar_oportunidad(oportunidad):
    linea = linea_oportunidad(oportunidad)
    f = open("Datos/Oportunidades.txt", "a+")
    f.write("\n" + linea)
    f.close()
#-----------------------------------------------------------------------------------------------------------------------
def modificar_oportunidad(oportunidad):
    linea_a_modificar = linea_oportunidad(oportunidad)
    posicion = 0

    with open('Datos/Oportunidades.txt') as f:
        x = 0
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == oportunidad.id:
                posicion = x
            x += 1
    # f.close()

    with open('Datos/Oportunidades.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == posicion:
                linea = linea_a_modificar
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1
#-----------------------------------------------------------------------------------------------------------------------
def modificar_informe(informe):
    linea_a_modificar = linea_informe(informe)
    posicion = 0

    with open('Datos/Informes.txt') as f:
        x = 0
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == informe.getId():
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
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------
def modificar_actividad(actividad):
    linea_a_modificar = "{0},{1},{2},{3},{4}".format(str(actividad.id),str(actividad.descripcion),str(actividad.fecha_vencimiento),
                                                 str(actividad.fecha_planificacion),str(actividad.tipoactividad.name))
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