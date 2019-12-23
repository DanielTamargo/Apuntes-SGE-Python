class Vehiculo():

    #Constructor
    def __init__(self,matricula, ruedas, color):
        self.matricula = matricula
        self.__ruedas = ruedas #privado: sólo se puede usar dentro de la clase
        self.color = color

    def mostrarInfo(self):
        print('Información del vehículo')
        print('Matrícula: ', self.matricula)
        print('Ruedas: ', self.__ruedas)
        print('Color: ', self.color)


v = Vehiculo('3333',2,'blanco')
# No es visible --> atributo que no es visible fuera de la clase
#print(v.ruedas)

#Pero llamando al método mostrarInfo:
#v.mostrarInfo()

####################################################################

class Vehiculo2():

    #Constructor
    def __init__(self,matricula, ruedas, color):
        self.matricula = matricula
        self.__ruedas = 4
        self.color = color

    #Método similar a toString de Java. Sirve para mostrar un objeto
    def __str__(self):
        return "Matrícula {}, {} Ruedas".format( self.matricula, self.__ruedas )

    def mostrarInfo(self):
        print('Información del vehículo')
        print('Matrícula: ', self.matricula)
        print('Ruedas: ', self.__ruedas)
        print('Color: ', self.color)

    def cambiarRuedas(self,numRuedas):
        self.__ruedas=numRuedas
        self.mostrarInfo()

    def getRuedas(self):
        return self.__ruedas

    #Podemos usar directamente el setter para cambiar las ruedas
    def setRuedas(self,numRuedas):
        self.__ruedas=numRuedas

    #Y si queremos, podemos definir otro método que use el setter para actualizar el número de ruedas
    def cambiarRuedasconSetter(self,numRuedas):
        self.setRuedas(numRuedas)
        self.mostrarInfo()

v = Vehiculo2('3333fsdfsd',2,'blanco')

# A pesar de haber creado un vehículo con dos ruedas, al mostrar la información, dirá que tiene 4 ruedas, porque no se
# puede cambiar desde fuera de la clase.
#v.mostrarInfo()
#print('------------')
# Utilizo el método que "quita ruedas dentro de la clase". Mostrará 2 ruedas
#v.cambiarRuedas(2)


#Dará error, porque no podemos acceder directamente a este atributo o propiedad
#print(v.ruedas)
#A través del método get, podremos ver las ruedas que tiene
#print('El número de ruedas del coche es: ', v.getRuedas())

####################
# Si implementamos el método __str__
print(v)
