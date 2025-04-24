import json
archivo=open("informacion.json","r")
contenido=json.load(archivo)
print(contenido)
archivo.close()