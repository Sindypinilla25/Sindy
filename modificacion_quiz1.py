#Importar libreria
import json
from datetime import datetime

información=open("Vercion_1.json","r")
contenido=json.load(información)
print(contenido)
información.close()

#Modificar el contenido
ingenieriadesistemas= input("Ingrese el nuevo nombre de la carrera: ")
contenido["carrera"] = ingenieriadesistemas
contenido["fecha_modificacion"] = str(datetime.now())
#Guardar el json
#Variable para guardar el archivo
información= open("vercion_v1.json", "w")
#Guardar el archivo en formato JSON
json.dump(contenido, información)
#Cerrar el archivo
información.close()