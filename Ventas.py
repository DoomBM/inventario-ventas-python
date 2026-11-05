import Almacen
import datetime

def venta():
    carrito_compras = []
    bienvenida()
    print()
    while True:
        armar_carrito(carrito_compras)
        print()
        total = mostrar_carrito(carrito_compras)
        ultimos_cambios(carrito_compras)

        finalizar_compra = input("Presione: \n'S' para finalizar la compra \n'M' para modificar la compra \ncualquier itra tecla para cancelar la compra ")
        if finalizar_compra.upper() == "S":
            fecha = datetime.datetime.now()
            carrito_compras.append(fecha.strftime("%d/%m/%Y %H:%M:%S"))
            carrito_compras.append(total)
            break
        elif finalizar_compra.upper() == "M":
            continue
        else:
            carrito_compras.clear()
            break



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

def mostrar_carrito(carrito):
    total = 0
    for recorrido in carrito:
        print(f"ID: {recorrido['ID']}")
        print(f"Nombre: {recorrido['nombre']}")
        print(f"Cantidad: {recorrido['cantidad']}")
        subtotal = recorrido["precio"] * recorrido["cantidad"]
        print(f"Precio: {subtotal}")
        total += subtotal
    print(f"Total: {total}")
    return total



def ultimos_cambios(carrito):
    print("-"*30)
    while True:
        print("¿Deseas realizar otro cambio?")
        print("1. Agregar otro(s) producto(s) \n2. Eliminar otro(s) producto(s) \n3. Regresar")
        opcion = input()
        if opcion == "1":
            armar_carrito(carrito)
            break
        elif opcion == "2":
            eliminar_producto(carrito)
            break
        elif opcion == "3":
            break
        else:
            print("Ingrese una opcion valida")


def eliminar_producto(carrito):
    for indice, articulo in enumerate(carrito, start=1):
        print(f"{indice}: {articulo['nombre']}")
    while True:
        try:
            eliminar = int(input("¿Que producto deseas eliminar?: "))
        except ValueError:
            print("Ingrese un numero valido.")
            continue
        if 0 < eliminar <= len(carrito):
            carrito.pop(eliminar - 1)
            break
        else:
            print("Ingrese un numero valido.")





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