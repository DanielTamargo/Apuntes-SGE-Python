tildes = {'á' : 'a', 'à' : 'a'}
palabra = 'hálà'
for i in range(0, len(palabra)):
    #print(palabra[i])
    #print(palabra[i] in tildes.keys())
    if palabra[i] in tildes.keys():
        palabra.replace(palabra[i], str(tildes[palabra[i]]))
print(palabra)