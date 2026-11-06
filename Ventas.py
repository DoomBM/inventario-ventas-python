import Almacen
from Almacen import inventario


def venta():
    carrito_compras = []-
    bienvenida()
    print()
    while True:
        armar_carrito(carrito_compras)
        if len(carrito_compras) == 0:
            mensaje_error = input("No agregaste nada. Por favor presiona una opcion"
                                  "\n'C' para agregar productos"
                                  "\nO cualquier otra tecla para cancelar la compra")
            if mensaje_error.upper() == "C":
                continue
            else:
                break
        print()
        ultimos_cambios(carrito_compras)
        total_compra = mostrar_carrito(carrito_compras)

        finalizar_compra = input("Presione: \n'S' para finalizar la compra "
                                 "\n'C' para continuar su la compra "
                                 "\ncualquier otra tecla para cancelar la compra ")
        if finalizar_compra.upper() == "S":
            fecha = datetime.datetime.now()
            venta_realizada = {
                "fecha" : fecha,
                "carrito" : carrito_compras,
                "total_compra" : total_compra,
            }
            return venta_realizada
        elif finalizar_compra.upper() == "C":
            continue
        else:
            carrito_compras.clear()
            return None

def armar_carrito(carrito):
    while True:
        buscar = input("¿Que producto buscas? ")
        producto = Almacen.encontrar_productos(buscar)
        if producto is None:
            print("No se ha encontrado ese producto. Vuelve a buscar")
            continue
        ya_llevado = cantidad_en_carrito(carrito, producto["ID"])
        disponible = producto["stock"] - ya_llevado
        if producto is None:
            print("No se encontro este producto")
            continue
        if disponible <= 0:
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
        carrito.append(agregados)
        otro_product = input("¿Deseas agregar otra cosa? (presione 'S' para confirmar o enter para salir): " )
        if otro_product == "S":
            validacion = True
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
    Almacen.mostrar_inventario()
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