from Archivos import Clases
import csv

# Carga la lista de clientes del fichero (o los datos base creados para pruebas)
def cargar_datos_productos():
    productos = []
    with open('Datos/productos.txt', 'r+') as f:
        lineas = [line.rstrip('\n') for line in f]
        for linea in lineas:
            datos = linea.split(",")
            producto = Clases.Producto(datos[1], datos[2], datos[3], datos[4], datos[0])
            productos.append(producto)

    return productos

def cargar_datos_proveedores():
    proveedores = []
    with open('Datos/proveedores.csv', 'r+') as csv_f:
        reader = csv.DictReader(csv_f)
        for fila in reader:
            proveedor = Clases.Proveedor(fila["nif"], fila["nombre"], fila["num_ventas"], fila["id"])
            proveedores.append(proveedor)

    return proveedores

def cargar_datos_clientes():
    clientes = []
    with open('Datos/Clientes.txt', 'r+') as f:
        lineas = [line.rstrip('\n') for line in f]
        for linea in lineas:
            datos = linea.split(",")
            if datos[6] == "Sponsor":
                tipocliente = Clases.TipoCliente.Sponsor
            elif datos[6] == "Proveedor":
                tipocliente = Clases.TipoCliente.Proveedor
            else:
                tipocliente = Clases.TipoCliente.Cliente
            cliente = Clases.Cliente(datos[1], datos[2], datos[3],
                                     datos[4], datos[5], tipocliente, datos[0])
            clientes.append(cliente)

    return clientes

def cargar_datos_empleados():
    empleados = []
    with open('Datos/Empleados.txt', 'r+') as f:
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

def cargar_empleado_con_id(id_empleado):
    empleados = cargar_datos_empleados()
    for empleado in empleados:
        if empleado.id == id_empleado:
            return empleado
    return None

def cargar_datos_actividades():
    actividades = []
    with open('Datos/Actividades.txt', 'r+') as f:
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

            actividad = Clases.Actividad(datos[1], datos[2], datos[3], tipoactividad, datos[0])
            actividades.append(actividad)

    return actividades

def cargar_datos_informes():
    clientes = cargar_datos_clientes()
    empleados = cargar_datos_empleados()
    actividades = cargar_datos_actividades()

    informes = []
    with open('Datos/Informes.txt', 'r+') as f:
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

            # informe = Clases.Informe(actividad, clientes, empleados, id_informe)
            informes.append(informe)

    return informes

def cargar_datos_oportunidades():
    informes = cargar_datos_informes()

    oportunidades = []
    with open('Datos/Oportunidades.txt', 'r+') as f:
        lineas = [line.rstrip('\n') for line in f]
        for linea in lineas:
            id_oportunidad = linea[0:linea.find(",")]
            nombre_oportunidad = linea[(linea.find(",") + 1):(linea.find("(") - 1)]
            ids_informes_oportunidad = linea[(linea.find("(") + 1):linea.find(")")].split(",")
            dinero_estimado = linea[(linea.find(")") + 2):linea.rfind(",")]
            nombre_tipoetapa = linea[(linea.rfind(",") + 1):]

            lista_informes_opourtunidad = []
            for id_informe_oportunidad in ids_informes_oportunidad:
                for informe in informes:
                    if id_informe_oportunidad == informe.getId():
                        lista_informes_opourtunidad.append(informe)

            if nombre_tipoetapa == "Propuesta":
                tipoetapa = Clases.TipoEtapa.Propuesta
            elif nombre_tipoetapa == "Calificado":
                tipoetapa = Clases.TipoEtapa.Calificado
            elif nombre_tipoetapa == "Ganada":
                tipoetapa = Clases.TipoEtapa.Ganada
            elif nombre_tipoetapa == "Suspendida":
                tipoetapa = Clases.TipoEtapa.Suspendida
            else:
                tipoetapa = Clases.TipoEtapa.Nueva

            oportunidad = Clases.Oportunidad(str(nombre_oportunidad), lista_informes_opourtunidad, str(dinero_estimado),
                                             tipoetapa, id_oportunidad)
            oportunidades.append(oportunidad)

    return oportunidades

def cargar_datos_usuarios():
    usuarios = []
    with open("Datos/usuarios.txt", "r+") as f:
        lineas = [line.rstrip('\n') for line in f]
        for linea in lineas:
            datos = linea.split(",")
            usuario = Clases.Usuario(datos[0], datos[1], datos[2])
    return usuarios