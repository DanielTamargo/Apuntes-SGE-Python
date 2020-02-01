from Archivos.Funciones import CargarDatos as cd

def borrar_oportunidad(oportunidad):
    with open('Datos/Oportunidades.txt') as f:
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == oportunidad.id:
                lista_lineas.remove(linea)
    # f.close()

    with open('Datos/Oportunidades.txt', 'w+') as f:
        x = 0
        for linea in lista_lineas:
            if x == 0:
                f.write(str(linea))
            else:
                f.write("\n" + str(linea))
            x += 1

def borrar_informe_de_oportunidad(informe):
    oportunidades = cd.cargar_datos_oportunidades()
    for oportunidad in oportunidades:
        informes = oportunidad.informes
        if informe in informes:
            oportunidad.informes.remove(informe)
            modificar_oportunidad(oportunidad)

def borrar_informe(informe):
    with open('Datos/Informes.txt') as f:
        lista_lineas = [line.rstrip('\n') for line in f]
        for linea in lista_lineas:
            datos = linea.split(",")
            if datos[0] == informe.getId():
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
    informes = cd.cargar_datos_informes()
    for informe in informes:
        clientes = informe.getClientes()
        if cliente in clientes:
            informe.getClientes().remove(cliente)
            modificar_informe(informe)

# Elimina el empleado de los informes en los que aparezca (y guarda los cambios en el fichero)
def borrar_empleado_de_informes(empleado):
    informes = cd.cargar_datos_informes()
    for informe in informes:
        empleados = informe.getEmpleados()
        if empleado in empleados:
            empleados.remove(empleado)
            modificar_informe(informe)

# Elimina los informes relacionados con una actividad (y guarda los cambios en el fichero)
def borrar_informes_de_actividad(actividad):
    informes = cd.cargar_datos_informes()
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
            if datos[0] == actividad.id:
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
