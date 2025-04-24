#guardar formatocon formato JSON
import json
#crear diccionario
datos ={
    "Nombre":"Carlos",
    "Apellido":"Gonzalez",
    "telefono": 3208894758,
    "correo":"gjeoghie@gmail.com",
    "usuario":"cgonzales24",
}
archivo=open("informacion.json","w")
json.dump(datos,archivo)
archivo.close()