#punto c

# solicitar datos al usuario
nivel_usuario = int(input("ingrese su nivel de acceso (0-5): "))
nivel_requerido = int(input("ingrese el nivel de acceso requerido (0-5): "))
tarjeta_activa =input("¿su tarjeta está activa? (true/false): ") == "true"
cambio_cantrasena_reciente = input("¿cambió su contraseña en los últimos 30 días? (true/false): ") == "true"

# verificación de acceso
if nivel_usuario >= nivel_requerido:
    if tarjeta_activa and cambio_cantrasena_reciente:
        print("acceso permitido")
    else:
        print("acceso denegado: condiciones de seguridad no cumplidas")
else:
    print("Acceso denegado: nivel de acceso insuficiente")