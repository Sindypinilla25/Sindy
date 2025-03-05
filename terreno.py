import math

#solicitar al usuario
base = float(input("ingrese la base del terreno =triangulo: "))
altura = float(input("ingrese la altura del terreno =triangulo: "))
altura_rectangulo = float(input("ingrese la altura del terreno = rectangulo"))
#calcular el area del terreno
triangulo = (base*altura)/2
#calcular el area del rectangulo 
rectangulo = base*altura_rectangulo
#calcular el area total
area_total = triangulo+rectangulo


