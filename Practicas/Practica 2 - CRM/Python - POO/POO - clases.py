class Vehiculo():

    #Constructor
    def __init__(self,matricula, ruedas, color):
        self.matricula = matricula
        self.ruedas = ruedas
        self.color = color

    #Getters y Setters
    def getMatricula(self):
        return self.matricula
    def getRuedas(self):
        return self.ruedas
    ###
    def setMatricula(self,matricula):
        self.matricula = matricula

v = Vehiculo('123ABC', 4, 'azul')

print("Datos del vehículo: ", v.matricula, v.ruedas, v.color)

#######################################################################

class Alumno():
    nombre = 'Alumno'
    apellido = 'ApellidoAlumno'
    DNI = 'XXXXXXXXXX'

alumno = Alumno()
print('Datos del alumno: ', alumno.nombre, ' ', alumno.apellido, ' ', alumno.DNI)

#######################################################################

class Alumno2():

    def __init__(self):
        self.nombre = 'Alumno'
        self.apellido = 'ApellidoAlumno'
        self.DNI = 'XXXXXXXXXX'

alumno = Alumno2()
print('Datos del alumno: ', alumno.nombre, ' ', alumno.apellido, ' ', alumno.DNI)

########################################################################
