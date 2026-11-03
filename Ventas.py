import Almacen
import datetime

def venta():
    bienvenida()


def armar_carrito(carrito):
    while True:
        buscar = input("¿Que producto buscas? ")
        producto = Almacen.encontrar_productos(buscar)
        ya_llevado = cantidad_en_carrito(carrito, producto["ID"])
        disponible = producto["stock"] - ya_llevado
        if producto is None:
            print("No se encontro este producto")
            continue
        if disponible < 0:
            print("No hay mas productos disponibles")
            continue
        while True:

            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Ingrese un numero valido.")
                continue
            if cantidad <= 0:
                print("la cantidad tiene que ser mayor a 0")
                continue
            if ya_llevado + cantidad > producto["stock"]:

                print("Ha rebasado el stock")
                continue
            if ya_llevado + cantidad == producto["stock"]:
                continue
            else:
                break
        articulo = {
            "ID": producto["ID"],
            "nombre": producto["nombre"],
            "cantidad": cantidad,
            "precio": float(producto["precio"]),
        }
        if ya_llevado  > 0:
            for recorrido in carrito:
                if recorrido["ID"] == producto["ID"]:
                    recorrido["cantidad"] += cantidad
                    break
        else:
            carrito.append(articulo)
        otro = input("¿Deseas agregar otra cosa? (presione 'S' si es asi o enter para salir): " )
        if otro.upper() != "S":
            break

def cantidad_en_carrito(carrito, id_producto):
    for busqueda in carrito:
        if busqueda["ID"] == id_producto:
            return busqueda["cantidad"]
    return 0

def bienvenida():
    print("Bienvenido a la papeleria")
    print("-" * 30)
    print("Estos son los productos disponibles:")
    productos_disponibles()
    print("-" * 30)
    print()

def productos_disponibles():
    if len(Almacen.inventario) > 0:
        for producto in Almacen.inventario:
            print(f"ID: {producto['ID']}")
            print(f"Producto: {producto['nombre']}")
            print(f"Cantidad: {producto['stock']}")
            print(f"precio: {producto['precio']}")
    else:
        print("No hay productos disponibles")
        return

Almacen.menu_almacen()
venta()