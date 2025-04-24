import json
información=open("Vercion_1.json","r")
contenido=json.load(información)
print(contenido)
información.close()