#estructura for
for i in range(2):
    print(i)

for i in range(10):
    print(i)

#estructura for con range
for i in range(1, 10):
    print(i)

#estructurafor con range

for i in range(3, 10,2):
    print(i)

# variable 
x = "python"

#separar los caracteres con for
for letras in x:
    if letras == "h":
        break
    else:
        print(letras)
    print(letras)

# ejemplo 1
for mul in range(1,11):
    print(f"2 x {mul} = {2 * mul}")

# ejemplo 2
numero= int(input("ingrese un número de tabla :"))
for mul in range(1,11):
    print(f"{numero} x {mul} = {numero * mul}")

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} es par")


