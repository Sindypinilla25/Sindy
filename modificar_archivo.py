import json
from datetime import datetime 

archivo=open("informacion.json","r")
contenido=json.load(archivo)
print(contenido)
archivo.close()

username=input("ingrese el nuevo nombre de usuario: ")
contenido["usuario"]= username
contenido["fecha_modificacion"] = str (datetime.now)

archivo=open("informacion_v1.json","w")
json.dump(contenido,archivo)
archivo.close()