#función simple 
def mensaje():
    """
    muestra un mensaje
    """
    print("unisangil")

#llamada a la función
mensaje() 

#función con parametros
def suma(a,b):
    """
    suma dos números: int a, int b
    """
    rta = a + b
    print(rta)
#llamada a la función
suma(10,5)

#función con retorno
def multiplicacion(a,b):

    """
    multiplica dos números: int a, int b
    y retorna el resultado
    """
    rta =a * b
    return rta
#llaamada a la función 
rta = multiplicacion(10,5)
print(rta*2)

#funcion con retorno y sin parametros
def solicitar_datos():
    """
    solicitar 2 numeros int
    y los retorna num1,num2
    """
    num1= int(input("ingrese el primer número: "))
    num2= int(input("ingrese el segundo número: "))
    return num1,num2
#llamada a la función
a,b =solicitar_datos()
print(f"primer número={a} y segundo número={b}")

#llamar a suma 
suma(a,b)
#llamar a multiplicación
mul=multiplicacion(a,b)
print(f"la multiplicación = {mul}")
