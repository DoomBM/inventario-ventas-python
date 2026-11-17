import Almacen
import datetime

def compra_de_producto():
    Almacen.mostrar_inventario()
    while True:
        print("¿Que producto aumentara existencias?")
        mercancia = input()
        continuar_compra = input("presione 'O' para confirmar el nombre u cualquier otra tecla para volver a escribirlo")
        if continuar_compra.upper() != "O":
            continue
        producto = Almacen.encontrar_productos(mercancia)
        if producto is None:
            agregar = input("Ese producto no existe, ¿deseas agregarlo? presione: \n"
                            "'S' para agregar un producto. \n'B' para volver. \ncualquier otra tecla para cancelar\n")
            if agregar.upper() == "S":
                nuevo = Almacen.agregar_producto()
                fecha_hoy = datetime.datetime.now()
                compra = {
                    "fecha" : fecha_hoy.strftime("%d/%m/%Y %H:%M:%S"),
                    "ID" : nuevo["ID"],
                    "nombre": nuevo["nombre"],
                    "cantidad": nuevo["stock"],
                    "costo": nuevo["costo"],
                }
                mostrar_mercancia(compra)
                return compra
            elif agregar.upper() == "B":
                continue
            else:
                break
        else:
            cantidad = aumentar_existencias(producto)
            print()
            nuevo_costo = costo_mercancia(producto)
            fecha_llegada = datetime.datetime.now()

            compra = {
                "fecha" : fecha_llegada.strftime("%d/%m/%Y %H:%M:%S"),
                "ID" : producto["ID"],
                "nombre": producto["nombre"],
                "cantidad": cantidad,
                "costo": nuevo_costo,
            }

            mostrar_mercancia(compra)
            return compra

def aumentar_existencias(producto):
    while True:
        try:
            aumentar_stock = int(input("¿Cuanta cantidad llego?"))
        except ValueError:
            print("Solo se pueden ingresar un numero entero")
            continue
        if 0 < aumentar_stock:
            producto["stock"] += aumentar_stock
            return aumentar_stock
        else:
            print("El numero tiene que ser mayor a 0")

def costo_mercancia(producto):
    historial_de_costos = []
    while True:
        try:
            costo = float(input(f"¿Que costo tuvo {producto['nombre']}?"))
        except ValueError:
            print("Solo se pueden ingresar numeros")
            continue
        if 0 <= costo:
            historial_de_costos.append(costo)
            return costo
        else:
            print("El numero tiene que ser mayor o igual a 0")

def mostrar_mercancia(datos_compra):
    print("-" * 45)
    print("       INFORMACIÓN DEL PRODUCTO COMPRADO")
    print("-" * 45)
    print(f"Fecha de llegada: {datos_compra['fecha']}")
    print(f"ID: {datos_compra['ID']}")
    print(f"Nombre: {datos_compra['nombre']}")
    print(f"¿Cuanta cantidad se ingreso?: {datos_compra['producto_ingresado']}")
    print(f"Costo: {datos_compra['costo']}")
    print("-" * 45)