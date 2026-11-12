import Almacen

def compra_de_producto():
    print("¿Que producto comprara?")
    Almacen.mostrar_inventario()
    mercancia = input()
    Almacen.encontrar_productos(mercancia)


def aumentar_existencias(producto):
    while True:
        try:
            aumentar_stock = int(input("¿Cuanta cantidad desea aumentar?"))
        except ValueError:
            print("Solo se pueden ingresar un numero entero")
    if 0 > aumentar_stock <= producto:
    producto["stock"] += aumentar_stock

