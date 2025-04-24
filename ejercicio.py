#variable
Progrmación={
    "Docente":{
        "Nombre":"Carlos",
        "Apellido":"Gonzalez",
        "telefono": 3208894758,
        "correo":"gjeoghie@gmail.com",
    },
    "Estudiantes":[
        {
            "Nombre":"Sara",
            "Apellido":"Perez",
            "cedula": 1208894758,
            "correo":"huhugds@gmail.com",
        },
        {
            "Nombre":"Sofia",
            "Apellido":"Zuares",
            "cedula": 1209894758,
            "correo":"lopawkd@gmail.com",
        }
    ],
    "Codigo":1456,
    "estado":1
}
print(type[Progrmación])
print(Progrmación["Docente"])
print(Progrmación["Docente"]["Nombre"])
#lista de los estudiantes 
for Estudiantes in Progrmación["Estudiantes"]:
    print(Estudiantes)

#items
print(Progrmación.items())
#items
print(Progrmación["Docente"].items())

#keys
print(Progrmación.keys())
print(Progrmación["Docente"].keys())


#values
print(Progrmación.values())
print(Progrmación["Docente"].values())

for Estudiantes in Progrmación["Estudiantes"]:
    print(Estudiantes.values)

#gets


#añadir
Progrmación["programa"]="ingenieria en sitemas"
print(Progrmación)

#eliminar
del Progrmación["programa"]
print(Progrmación)