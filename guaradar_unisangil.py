import json
Unisangil={
    "San Gil":{
    },
    "Yopal":{
    },
    "Chiquinquira":[
        {
            "Facultad de Ciencias Economicas y Admistrativas"[
                {
                    "Administracion de Empresas"
                },
                {
                    "Contaduria Publica"
                },
                {
                    "Tecnologia en Gestión de Empresas de Economia Solidaria"
                }
            ],
            "Facultad de Ciencias Naturales e Ingenieria"[
                "Ingenieria de Sistemas":[
                    {
                        "Semestre 1"
                    },
                    {
                        "Semestre 2 "
                    },
                    {
                        "Semestre 3"
                    },
                    {
                        "Semestre 4"
                    },
                    {
                        "Semestre 5"
                    },
                    {
                        "Semestre 6"
                    },
                    {
                        "Semestre 7"
                    },
                    {
                        "Semestre 8"
                    },
                ]
            ],
            "Facultad de Ciencias Juridicas y Políticas"[
                "Derecho"
            ]
        }
    ]
}
archivo=open("informacion.json","w")
json.dump(Unisangil,archivo)
archivo.close()