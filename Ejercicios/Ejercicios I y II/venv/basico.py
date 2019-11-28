
#DICCIONARIO, DECLARACIÓN, RECORRER CON FOR MOSTRANDO CLAVE Y VALOR
jugadores={'1':'Lebron', '2':'Noccioni','3':'Tam'}
print("Lista de jugadores (Dorsal --> Jugador)")
'''
for key, value in jugadores.items():
    print(key,"-->",value)
'''
for key in jugadores:
    print(key,"-->",jugadores[key])

