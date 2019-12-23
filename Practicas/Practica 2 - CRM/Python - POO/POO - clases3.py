class Rueda():
    #Constructor
    def __init__(self,marca, anchura, tipo):
        self.marca = marca
        self.anchura = anchura
        self.tipo = tipo

    #¿Si no lo definimos?
    def __str__(self):
        return "RUEDAS: Marca {}, {} Tipo".format( self.marca, self.tipo )

class Vehiculo3():

    #Constructor
    def __init__(self,matricula, r, color):
        self.matricula = matricula
        self.ruedas = r
        self.color = color

    def __str__(self):
        return "Matrícula {}, {} Ruedas".format( self.matricula, self.ruedas )

r = Rueda('Pirelli',195,'Invierno')
v=Vehiculo3('12345', r, 'azul')

print(v)
