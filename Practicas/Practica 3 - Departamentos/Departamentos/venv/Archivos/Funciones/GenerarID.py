########################################################################################################################
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

########################################################################################################################
# Recorre una lista, ya sea de clientes, empleados o actividades, buscando si el id existe o no, devuelve un boolean.
# Devuelve True si el id es válido (único), y False si el id ya existe.
def comprobar_id(id, lista):
    for valor in lista:
        if id == valor.id:
            return False
    return True

# La clase informe tiene los atributos privados y funciona con getters, necesita un método distinto
def comprobar_id_informe(id, lista): 
    for valor in lista:
        if id == valor.getId():
            return False
    return True

########################################################################################################################
# Utilizan la función generar_id y comprueba el id generado para ver que no existe, si no existe, lo asigna
# Para saber si el id existe o no, utiliza la función comprobar_id
def generar_id_cliente():
    clientes = cargar_datos_clientes()
    while True:
        id = generar_id()
        if comprobar_id(id, clientes):
            return id

def generar_id_empleado():
    empleados = cargar_datos_empleados()
    while True:
        id = generar_id()
        if comprobar_id(id, empleados):
            return id

def generar_id_actividad():
    actividades = cargar_datos_actividades()
    while True:
        id = generar_id()
        if comprobar_id(id, actividades):
            return id

def generar_id_informe():
    informes = cargar_datos_informes()
    while True:
        id = generar_id()
        if comprobar_id_informe(id, informes):
            return id

def generar_id_oportunidad():
    oportunidades = cargar_datos_oportunidades()
    while True:
        id = generar_id()
        if comprobar_id(id, oportunidades):
            return id

def generar_id_registroLesion():
    registroLesiones = cargar_datos_registroLesion()
    while True:
        id = generar_id()
        if comprobar_id(id, registroLesiones):
            return id