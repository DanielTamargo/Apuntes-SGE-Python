# Quitar Tildes
tildes = {'á' : 'a', 'à' : 'a'}
palabra = 'hálà'
print("Antes de quitar:", palabra)
for i in range(0, len(palabra)):
    if palabra[i] in tildes.keys():
        palabra = palabra.replace(palabra[i], tildes[palabra[i]])
print("Después de quitar:", palabra)

