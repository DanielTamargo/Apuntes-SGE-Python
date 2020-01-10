from enum import Enum
import colorama
import datetime
import dateutil.relativedelta as dr

#from Archivos import Funciones as Fun
import Funciones as Fun

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
# -------------------------------------------------- Enumeraciones --------------------------------------------------- #
#----------------------------------------------------------------------------------------------------------------------#
class TipoCliente(Enum):
    Cliente = 1  # <- por defecto
    Sponsor = 2
    Proveedor = 3

class TipoActividad(Enum):
    Reunion = 1  # <- por defecto
    Llamada = 2
    Promocion = 3
    Informe = 4 # <- no es realizar un informe de gráficas, está enfocado en informar a los clientes

class TipoEtapa(Enum):
    Nueva = 1  # <- por defecto
    Propuesta = 2
    Calificada = 3
    Ganada = 4
    Suspendida = 5

class Departamento(Enum):
    Comercial = 1  # <- por defecto
    Administrativo = 2
    Ventas = 3
    RRHH = 4
    Salud = 5

#----------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------- Clases ------------------------------------------------------- #
#----------------------------------------------------------------------------------------------------------------------#
class Persona():
    # Una clase padre. Contiene los datos de una persona. Sirve para clientes y empleados.
    # No puedo crear múltiples constructores como hacía en Java, así que voy a crear solo uno,
    ##### con valores predeterminados que se sobreescriben solos en caso de recibirlos.
    # Todas las personas tienen id, pero no es lo mismo un id empleado que un id cliente, por lo que no va aquí
    def __init__(self, dni=None, nombre=None, apellidos=None, email=None, fecha_nacimiento=None):
        if email is None:
            self.email = "test@test.com"
        else:
            self.email = email

        if fecha_nacimiento is None:
            self.fecha_nacimiento = "Unknown"
        else:
            self.fecha_nacimiento = fecha_nacimiento

        if apellidos is None:
            self.apellidos = "Prueba"
        else:
            self.apellidos = apellidos

        if nombre is None:
            self.nombre = "Test"
        else:
            self.nombre = nombre

        if dni is None:
            self.dni = "OOOOOOOOX"
        else:
            self.dni = dni

    # Calcula la edad en base a la fecha de nacimiento. Se basa en la fecha de nacimiento
    def edad(self):
        fecha_nac = str(self.fecha_nacimiento)
        if fecha_nac != "Unknown":
            fecha_nac = datetime.datetime.strptime(fecha_nac, '%Y-%m-%d')
            hoy = datetime.datetime.today()
            try:
                cumpleanyos = fecha_nac.replace(year=hoy.year)
            except:
                cumpleanyos = fecha_nac.replace(year=hoy.year, month=fecha_nac.month + 1, day=1)
            if cumpleanyos > hoy:
                return hoy.year - fecha_nac.year - 1
            else:
                return hoy.year - fecha_nac.year
        else:
            return -1 # <- Tratar el -1 como un error

#----------------------------------------------------------------------------------------------------------------------#
class Cliente(Persona):
    # Participan en actividades.
    def __init__(self, dni=None, nombre=None, apellidos=None, email=None, fecha_nacimiento=None, tipocliente=None,
                 id=None):
        Persona.__init__(self, dni, nombre, apellidos, email, fecha_nacimiento)
        if id is None:
            self.id = Fun.generar_id_cliente()
        else:
            self.id = id
        if tipocliente is None:
            self.tipocliente = TipoCliente.Cliente
        else:
            self.tipocliente = tipocliente

    def __str__(self):
        if self.tipocliente != TipoCliente.Cliente:
            return "{0} - {1}, {2}. {3}.".format(str(self.id), str(self.apellidos), str(self.nombre),
                                                 str(self.tipocliente.name))
        else:
            return "{0} - {1}, {2}.".format(str(self.id), str(self.apellidos), str(self.nombre))

    def mostrar_info(self):
        c = colores()
        cadena = c["lc"] + "ID: " + c["rst"] + "{0}\n" + c["lc"] + "DNI:" + c["rst"] + " {1}\n" + c["lc"] \
                 + "Nombre: " + c["rst"] + "{2}\n" + c["lc"] + "Apellidos: " + c["rst"] + "{3}\n" \
                 + c["lc"] + "Fecha: " + c["rst"] + "{4}\n" + c["lc"] + "Tipo: " + c["rst"] + "{5}"
        print(cadena.format(str(self.id), str(self.dni), str(self.nombre), str(self.apellidos),
                            str(self.fecha_nacimiento), str(self.tipocliente.name)))

#----------------------------------------------------------------------------------------------------------------------#
class Empleado(Persona):
    # Organizan/administran actividades.
    def __init__(self, dni=None, nombre=None, apellidos=None, email=None, fecha_nacimiento=None, departamento=None,
                 fecha_contratacion=None, id=None):
        Persona.__init__(self, dni, nombre, apellidos, email, fecha_nacimiento)
        if id is None:
            self.id = Fun.generar_id_empleado()
        else:
            self.id = id
        if departamento is None:
            self.departamento = Departamento.Comercial
        else:
            self.departamento = departamento
        if fecha_contratacion is None:
            self.fecha_contratacion = "Unknown"
        else:
            self.fecha_contratacion = fecha_contratacion

    def __str__(self):
        return "{0} - {1}, {2}. {3}.".format(str(self.id), str(self.apellidos), str(self.nombre),
                                             str(self.departamento.name))

#----------------------------------------------------------------------------------------------------------------------#
class Actividad():

    def __init__(self, descripcion=None, fecha_vencimiento=None, fecha_planificacion=None, tipoactividad=None,
                 id=None):
        if id is None:
            self.id = Fun.generar_id_actividad()
        else:
            self.id = id

        if tipoactividad is None:
            self.tipoactividad = TipoActividad.Reunion
        else:
            self.tipoactividad = tipoactividad

        if descripcion is None:
            self.descripcion = "No tiene descripción."
        else:
            self.descripcion = descripcion

        if fecha_planificacion is None:
            self.fecha_planificacion = datetime.date.today()
        else:
            self.fecha_planificacion = fecha_planificacion

        if fecha_vencimiento is None:
            fecha = datetime.date.today()
            fecha = fecha + dr.relativedelta(days=7)
            self.fecha_vencimiento = fecha

        else:
            self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return "{0} - {1}, {2}. {3}".format(str(self.id), str(self.tipoactividad.name), str(self.fecha_vencimiento),
                                            str(self.descripcion))

#----------------------------------------------------------------------------------------------------------------------#
class Informe():
    # El informe relaciona la actividad con una lista de clientes (participan) y empleados (administran)
    def __init__(self, actividad=None, clientes=None, empleados=None, id=None):
        self.__actividad = actividad
        if id is None:
            self.__id = Fun.generar_id_informe()
        else:
            self.__id = id
        if actividad is None:
            self.__actividad = ""
        else:
            self.__actividad = actividad
        if clientes is None:
            self.__clientes = []
        else:
            self.__clientes = clientes
        if empleados is None:
            self.__empleados = []
        else:
            self.__empleados = empleados

    def __str__(self):
        return str(self.__id), str(self.__actividad)

    # Como quiero mostrar los clientes y empleados, en vez de to string haré una función específica
    def mostrar_informe(self):
        c = colores()
        print(c["ly"] + "Informe: " + c["rst"] + str(self.__id))
        print(c["ly"] + "Actividad: " + c["rst"] + str(self.__actividad))
        if len(self.__clientes) > 1:
            x = 1
            print(c["ly"] + "Lista de clientes: " + c["rst"])
            for cliente in self.__clientes:
                print(str(x) + ". " + str(cliente))
                x += 1
        elif len(self.__clientes) > 0:
            print(c["ly"] + "Cliente: " + c["rst"] + str(self.__clientes[0]))
        else:
            print(c["lr"] + "Actualmente no hay clientes asociados a la actividad." + c["rst"])
        if len(self.__empleados) > 1:
            x = 1
            print(c["ly"] + "Lista de empleados: " + c["rst"])
            for empleado in self.__empleados:
                print(str(x) + ". " + str(empleado))
                x += 1
        elif len(self.__empleados) > 0:
            print(c["ly"] + "Empleado: " + c["rst"] + str(self.__empleados[0]))
        else:
            print(c["lr"] + "Actualmente no hay empleados asociados a la actividad." + c["rst"])

    # Getters
    def getId(self):
        return self.__id
    def getActividad(self):
        return self.__actividad
    def getClientes(self):
        return self.__clientes
    def getEmpleados(self):
        return self.__empleados

    # Setters
    def setId(self, id):
        self.__id = id
    def setActividad(self, actividad):
        self.__actividad = actividad
    def setClientes(self, clientes):
        self.__clientes = clientes
    def setEmpleados(self, empleados):
        self.__empleados = empleados

    # Añadir a la lista
    def addCliente(self, cliente):
        self.__clientes.append(cliente)
    def addEmpleado(self, empleado):
        self.__empleados.append(empleado)

    # Eliminar de la lista
    def deleteCliente(self, cliente):
        if cliente in self.__clientes:
            self.__clientes.remove(cliente)
            return True
        else:
            return False
    def deleteEmpleado(self, empleado):
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)
            return True
        else:
            return False

#----------------------------------------------------------------------------------------------------------------------#
class Oportunidad():

    def __init__(self, nombre=None, informes=None, dinero_estimado=None, tipoetapa=None, id=None):
        if nombre is None:
            self.nombre = "Sin nombre"
        else:
            self.nombre = nombre
        if informes is None:
            self.informes = []
        else:
            self.informes = informes
        if dinero_estimado is None:
            self.dinero_estimado = 100
        else:
            self.dinero_estimado = dinero_estimado
        if tipoetapa is None:
            self.tipoetapa = TipoEtapa.Nueva
        else:
            self.tipoetapa = tipoetapa
        if id is None:
            self.id = Fun.generar_id_oportunidad()
        else:
            self.id = id

    def __str__(self):
        return "{0} ({1}) - Etapa: {2}. Dinero estimado: {3}€".format(str(self.nombre), str(self.id), str(self.tipoetapa.name), str(self.dinero_estimado))

    def addInforme(self, informe):
        self.informes.append(informe)
    def deleteInforme(self, informe):
        if informe in self.informes:
            self.informes.remove(informe)

    def mostrar_oportunidad(self):
        c = colores()
        print(c["ly"] + "Oportunidad: " + c["rst"] + str(self.nombre) + "(" + str(self.id) + ")")
        if len(self.informes) > 1:
            x = 0
            print(c["ly"] + "- Lista de informes: " + c["rst"], end="")
            for informe in self.informes:
                if x == 0:
                    print(str(informe.getId()), end="")
                else:
                    print(", " + str(informe.getId()), end="")
                x += 1
        elif len(self.informes) > 0:
            print(c["ly"] + "- Informe: " + c["rst"] + str(self.informes[0].getId()), end="")
        else:
            print(c["lr"] + "Actualmente no hay informes asociados a la actividad." + c["rst"], end="")
        print()
        print(c["ly"] + "- Dinero estimado: " + c["rst"] + str(self.dinero_estimado))
        print(c["ly"] + "- Etapa: " + c["rst"]  + str(self.tipoetapa.name))


#----------------------------------------------------------------------------------------------------------------------#
# ---------------------------------------------- No llegó a funcionar ------------------------------------------------ #
#----------------------------------------------------------------------------------------------------------------------#
    '''
    # No se pueden crear múltiples constructores.
    # Solución: Crear un constructor con datos predeterminados en caso de que no reciba nada (dato=None, dato2=None)
    # Constructor con todos los datos (por si se quiere introducir un id manualmente)
    def __init__(self, id, dni, nombre, apellidos, fecha_nacimiento, tipocliente):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.tipocliente = tipocliente
    
    # Constructor con todos los datos menos el id (se genera automáticamente)
    def __init__(self, dni, nombre, apellidos, fecha_nacimiento, tipocliente):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.tipocliente = tipocliente
    
    # Constructor con todos los datos menos id y tipocliente (se usa el tipocliente por defecto)
    def __init__(self, dni, nombre, apellidos, fecha_nacimiento):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
    '''
