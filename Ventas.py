import Almacen
from Almacen import inventario
from Almacen import productos

def venta():
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
                agregados["nombre"] = nombre
            else:
                print("Producto no encontrado")
        while True:
            try:
                num = int(input("Cual es la cantidad que llevaras?"))
                if 0 <= num <= productos["stock"]:
                    agregados["cantidad"] = num
                    productos["stock"] -= num
                    break
                elif productos["stock"] < 0:
                    productos["stock"] = 0
                else:
                    print("Algo salio mal")
            except ValueError:
                print("Ingrese un numero valido.")
        carrito.append(agregados)
        otro_product = input("¿Deseas agregar otra cosa? (presione 'S' para confirmar o enter para salir): " )
        if otro_product == "S":
            validacion = True
        else:
            validacion = False
    return carrito

def bienvenida():
    print("Bienvenido a la papeleria")
    print("-" * 30)
    print("Estos son los productos disponibles:")
    Almacen.mostrar_inventario()
    print("-" * 30)
    print()

Almacen.menu_almacen()
venta()