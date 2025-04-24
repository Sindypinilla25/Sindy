#crear lista
lista =[2,'a','sindy',3.14,True,100,'@']
print(type[lista])
print(lista)

#indibidualisar elementos
numero = lista[0]
decimal = lista[3]
print(decimal)

#tamaño 
tamaño = len (lista)
print(f"tamaño lista: {tamaño}")
estado = lista[4]
print(estado)
dato = lista[-4]
print(dato)
print(lista[-7])
#recorrido
print(lista[0:3])
print(lista[:])
print(lista[2:])
print(lista[:4])
print(lista[-4:])
print(lista[-5:-1])

#lista vacia
numeros = []
print(numeros)
#añadir valores a la lista
numeros.append(10)
numeros.append(1)
numeros.append(5)
numeros.append(True)
print(numeros)
tamaño_numeros =len(numeros)
print(f"tamaño lista:{tamaño_numeros}")

numeros.insert(0,'sindy')
print(numeros)
numeros.insert(2,'unisangil')
print(numeros)
numeros.insert(-1,'6')
print(numeros)
tamaño_numeros =len(numeros)
print(f"tamaño lista:{tamaño_numeros}")

numeros.append(3208894805)
numeros.append(3102992012)
print(numeros)
numeros.insert(5,'gato')
print(numeros)
numeros.insert(-5,'rojo')
print(numeros)
tamaño_numeros =len(numeros)
print(f"tamaño lista:{tamaño_numeros}")

#eliminar datos de una lista
numeros.remove("unisangil")
print(numeros)
tamaño_numeros =len(numeros)
print(f"tamaño lista:{tamaño_numeros}")

numeros.pop()
print(numeros)
numeros[1:3]=[]
print(numeros)

#individualisar con for
for dato in numeros:
    print(f"datos: {dato}")

lista1 = [10,2,30,4,5,1]
print(lista1)
#invertir datos de una lista
lista1.reverse()
print(lista1)
#ordenar los datos
lista1.sort()
print(lista1)
#ordenar los datos desentes
lista1.sort(reverse=True)
print(lista1)



