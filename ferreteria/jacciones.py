import json

path = "D:/Archivos_Usuario/Desktop/PROGRAMACIÓN 1/Calculadora_Figuras_Gometricas/ferreteria/productos.json"

def readJson():
    with open(path, "r", encoding="utf-8") as file:
        readed = json.load(file)
    return readed

print(readJson())