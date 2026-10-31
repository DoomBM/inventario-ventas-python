import Almacen
from Almacen import inventario


def venta():
    num = int()
    bienvenida()
    carrito = []
    agregados = {}
    validacion = True
    while validacion:
        nombre = input("¿Que producto ingresara al carrito?: ")
        if len(inventario) == 0 or len(nombre) == 0:
            print("Producto no encontrado")
            break
        for producto in inventario:
            if producto["nombre"] == nombre:
                nombre = producto["nombre"]
            while True:
                    try:
                        num = int(input("Cual es la cantidad que llevaras?"))
                        if 0 <= num <= producto["stock"]:
                            agregados["cantidad"] = num
                            producto["stock"] -= num
                            break
                        elif producto["stock"] < 0:
                            producto["stock"] = 0
                        else:
                            print("Algo salio mal")
                    except ValueError:
                        print("Ingrese un numero valido.")
        agregados = {
            "nombre" : nombre,
            "cantidad" : num,
        }
        carrito.append(agregados)
        otro_product = input("¿Deseas agregar otra cosa? (presione 'S' para confirmar o enter para salir): " )
        if otro_product == "S":
            validacion = True
        else:
            validacion = False
    print(carrito)

def bienvenida():
    print("Bienvenido a la papeleria")
    print("-" * 30)
    print("Estos son los productos disponibles:")
    Almacen.mostrar_inventario()
    print("-" * 30)
    print()

Almacen.menu_almacen()
venta()