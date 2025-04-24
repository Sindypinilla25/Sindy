#guardar formatocon formato JSON
import json
#crear diccionario
datos ={
    "unisangil": {
        "sedes": {
            "chiquinquira": {
                "Facultades": {
                    "Ingenierias y ciencias naturales": {
                        "ingenieria de sistemas": {
                            "primer semestre": [
                                "Calculo diferencial",
                                "Fundamentos de programacion",
                                "Algebra",
                                "diseno prototipado",
                                "Mecanica",
                                "Expresion 1"
                            ],
                            "segundo semestre": {
                                "Calculo integral": [],
                                "Matematicas discretas": [],
                                "Electromagnetismo": [],
                                "Proyecto integrador 1": [],
                                "expresion 2": [],
                                "Programacion 1": {
                                    "Docente": [
                                        "Jesus David Caro"
                                    ],
                                    "Estudiantes": [
                                        "Sindy Carolina Pinilla Murcia",
                                        "Juan David Montaño Rojas"
                                    ]
                                }
                            },
                            "tercer semestre": [
                                "Hadware y sistemas operativos",
                                "Estructura de datos",
                                "Calculo en varias variables",
                                "modelado y analisis numerico",
                                "sistemas bioticos",
                                "proyecto integrador 2",
                                "ciudadania"
                            ],
                            "cuarto semestre": [
                                "Pensamiento sistemico",
                                "redes",
                                "analisis de algoritmos",
                                "bases de datos",
                                "Programacion 2",
                                "Ecuaciones diferenciales",
                                "proyecto integrador 3"
                            ],
                            "quinto semestre": [
                                "Modelado de sistemas de informacion",
                                "adiministracion y gestion de bases de datos",
                                "Desarrollo web",
                                "Electiva diciplinaria 1",
                                "probabilidad y estadistica",
                                "proyecto integrador 4",
                                "electiva complementaria"
                            ],
                            "sexto semestre": [
                                "Ingeniera de sofware",
                                "Seguridad informatica",
                                "electiva diciplinaria2",
                                "Inteligencia artificial",
                                "Etica y comportamiento profesional"
                            ],
                            "septimo semestre": [
                                "Arquitectura de sofware",
                                "ciencia de datos",
                                "Administración de servidores}",
                                "investigacion de operaciones",
                                "gestion de proyectos1"
                            ],
                            "octavo semestre": [
                                "modalidad de grado",
                                "electiva diciplinaria3",
                                "electiva de Ingenieria"
                            ]
                        }
                    },
                    "Ciencias economicas y administrativas": [
                        "Contaduria publica",
                        "Administracion de empresas",
                        "tecnologia en gestion de empresas de economia solidaria"
                    ],
                    "Ciencias politicas y juridicas": [
                        "Derecho"
                    ]
                }
            },
            "Yopal": {
                "Facultades": {
                    "Ingenierias y ciencias naturales": [
                        "inteligencia artificial",
                        ""
                    ],
                    "Ciencias economicas y administrativas": [
                        "Contaduria publica",
                        "Administracion de empresas",
                        "tecnologia en gestion de empresas de economia solidaria"
                    ],
                    "Ciencias politicas y juridicas": [
                        "Derecho"
                    ]
                }
            },
            "San Gil": {
                "Facultades": [
                    "Ingenierias y ciencias naturales",
                    "Ciencias economicas y administrativas",
                    "Facultad de Ciencias de la Educación y de la Salud",
                    "Ciencias politicas y juridicas"
                ]
            }
        }
    }
}
información=open("Vercion_1.json","w")
json.dump(datos,información)
información.close()