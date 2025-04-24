#calculadora con while y elif 
#libreria
import math
#while true
while True:
    #MENÚ
    print("calculadora de operaciones básicas")
    print("1. suma")
    print("2. resta")
    print("3. multiplicación")
    print("4. divición")
    print("5. potencia")
    print("6. raíz cuadrada")
    print("7. salir")
    #opcion
    opción = int(input("ingrese una opción: "))
    if opción == 7:
        print("saliendo de la calculadora ...")
        break
    elif opción == 1:
        num1 = float(input("ingrese el primer número: "))
        num2 = float(input("ingrese el segundo número: "))
        suma = num1 + num2
        print(f"suma = {suma}")
    elif opción == 2:
        num1 = float(input("ingrese el primer número: "))
        num2 = float(input("ingrese el segundo número: "))
        resta = num1 - num2
        print(f"resta = {resta}")
    elif opción == 3:
        num1 = float(input("ingrese el primer número: "))
        num2 = float(input("ingresa el segundo número: "))
        multiplicacion = num1 * num2
        print(f"multiplicacion = {multiplicacion}")
    elif opción == 4:
        num1 = float(input("ingrese el primer número: "))
        num2 = float(input("ingresa el segundo número: "))
        divicion = num1 / num2
        print(f"divicion = {divicion}")
    elif opción == 5:
        num1 = float(input("ingrese el primer número: "))
        num2 = float(input("ingresa el segundo número: "))
        pow = num1 ** num2
        print(f"potencia = {pow}")
    elif opción == 6:
        num1 = float(input("ingrese el primer número: "))
        raiz = math.sqrt(num1)
        print(f"raíz cuadrada = {raiz}")
    else:
        print("opción errónea!!!")
print("gracias por utlizar la calculadora!!!")