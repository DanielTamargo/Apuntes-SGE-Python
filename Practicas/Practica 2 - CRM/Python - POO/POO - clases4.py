class PersonaEquipo():

    def __init__(self,id,nombre,apellido,edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        cadena = 'Id: ' + str(self.id) + ' Nombre: '+ str(self.nombre) + ' Apellido: '+ str(self.apellido) + ' Edad: '+ str(self.edad)
        return cadena

    def concentrarse(self):
        print(self.nombre, ' ', self.apellido, ' se concentra')

    def viajar(self):
        print(self.nombre, ' ', self.apellido, ' viaja')

# Subclase
class Subclase(PersonaEquipo):
    pass

pe = PersonaEquipo(1,'E','M',33)
j = Subclase(1,'E','M',33)
print(pe)
print(j)


######
# Clase jugador
class Jugador(PersonaEquipo):
    def __init__(self,id, nombre, apellido, edad, dorsal, posicion):
        PersonaEquipo.__init__(self,id,nombre,apellido,edad)
        self.dorsal = dorsal
        self.posicion = posicion

    def jugarPartido(self):
        print(self.nombre, ' ', self.apellido, ' juega')


class Entrenador(PersonaEquipo):
    def __init__(self,id, nombre, apellido, edad, idFederacion):
        PersonaEquipo.__init__(self,id,nombre,apellido,edad)
        self.idFederacion = idFederacion

    def dirigirPartido(self):
        print(self.nombre, ' ', self.apellido, ' dirige el equipo')



########
jugador = Jugador(20,'Ekaitz','Martinez',33,7,'interior izquierdo')
entrenador = Entrenador(5, 'Michael', 'Brown', 50, 99)

jugador.jugarPartido()
entrenador.dirigirPartido()

jugador.concentrarse()
entrenador.concentrarse()
