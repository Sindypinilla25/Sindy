import json
path = "productos.json"
class Producto:
    def __init__(self, nombre, marca, precio, cantidad):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad

class Ferreteria:
    def __init__(self):
        pass

    def agregar_producto_a_json(self):
        """
        Se encarga de guardar a un 
        """
        nombre = input("\nIngrese el nombre del producto: ")
        marca = input("Ingrese la marca del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad de ingreso: "))

        nuevo_producto = Producto(nombre, marca, precio, cantidad)
        product = {
            "nombre": nuevo_producto.nombre, 
            "marca": nuevo_producto.marca, 
            "precio": nuevo_producto.precio,
            "cantidad": nuevo_producto.cantidad
        }

        with open(path, "r", encoding="utf-8") as file:
            leido: list[dict] = json.load(file)

        leido.append(product)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(leido, file, indent=4)

        print(f"\033[32mProducto: {product} agregado con exito!\033[0m")
    
    def buscar_producto_json(self):    
        pregunta = int(input("\nBuscar por: [ Nombre -> 1 | Marca -> 0 ]: "))
        with open(path, "r", encoding="utf-8") as file:
            leido = json.load(file)

        if pregunta == 1:
            nombre = str(input("Ingrese nombre: ")).lower()
            for producto in leido:
                if producto["nombre"] == nombre:
                    print(f"\n{producto}\n")
        
        elif pregunta == 0:
            marca = str(input("Ingresa marca: ")).lower()
            for marca in leido:
                if marca["marca"] == marca:
                    print(marca)

    def mostrar_productos_json(self):
        with open(path, "r", encoding="utf-8") as file:
            print(f"\n{json.load(file)}\n")

def menu():
    ferreteria = Ferreteria()
    while True:
        print("\nMenú de Ferretería:")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Mostrar todos los productos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ferreteria.agregar_producto_a_json()
        elif opcion == "2":
            ferreteria.buscar_producto_json()
        elif opcion == "3":
            ferreteria.mostrar_productos_json()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("⚠ Opción no válida. Inténtelo de nuevo.")

menu()
