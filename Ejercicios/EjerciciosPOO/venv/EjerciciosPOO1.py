def es_numero_decimal(n):
    try:
        n = float(n)
    except:
        return False
    return True

def es_numero_entero(n):
    try:
        n = int(n)
    except:
        return False
    return True

class Alumno():

    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota

    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getNota(self):
        return self.nota

    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def setNota(self, nota):
        self.nota = nota

    def alumno_aprobado(self):
        if es_numero_decimal(nota):
            if nota >= 5:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido) + ", Nota: " + str(self.nota)

def ejercicio1():
    a = Alumno("Daniel","Tamargo",4.9)
    print(str(a.nombre), str(a.apellido) + ", Nota:", str(a.nota))
    print(a)

#######################################################################################################################

def ejercicio2():
    correcto = False
    while correcto == False:
        base = input("Base: ")
        if es_numero_decimal(base):
            correcto = True
    correcto = False
    while correcto == False:
        altura = input("Altura: ")
        if es_numero_decimal(altura):
            correcto = True

class Triangulo():
    t_base = 0.0
    t_altura = 0.0

    def __init__(self, base, altura):
        self.t_base = base
        self.t_altura = altura

    def tipo_triangulo(self):
        pass

    def perimetro(self):
        pass

    def area(self):
        return self.t_base * self.t_altura / 2

# Como lo hago sin saber cuanto mide cada lado o los angulos?????



#######################################################################################################################


class Calculadora():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __suma(self):
        return self.a + self.b
    def __resta(self):
        return self.a + self.b
    def __multiplicacion(self):
        return self.a * self.b
    def __division(self):
        return self.a / self.b

    def resultados(self):
        print("Suma:", str(self.__suma()))
        print("Resta:", str(self.__resta()))
        print("Multiplicación:", str(self.__multiplicacion()))
        print("División:", str(self.__division()))

def ejercicio3():
    correcto = False
    while correcto == False:
        a = input("Número 1: ")
        if es_numero_entero(a):
            correcto = True
    correcto = False
    while correcto == False:
        b = input("Número 2: ")
        if es_numero_entero(b):
            correcto = True

    calc = Calculadora(int(a), int(b))
    calc.resultados()

#######################################################################################################################

class Agenda():

    contactos = []

    def __init__(self):
        self.contactos = []

    def addContacto(self, contacto):
        self.contactos.append(contacto)
    def deleteContacto(self, contacto):
        self.contactos.remove(contacto)
    def editContacto(self, index, contacto):
        self.contacto[index] = contacto




















