inventario = []
categorias = []

def agregar_producto(productos):
    if productos > 0:
        for i in range(productos):
            producto = {}

            producto["ID"] = len(inventario ) + 1
            producto["nombre"] = input(f"Ingrese el nombre del producto {i + 1}: ").strip()
            while ValueError == True:
                try:
                    producto["costo"] = float(input("Ingrese el costo del producto: $"))
                except ValueError:
                    print("Ingrese un numero valido")
                    producto["costo"] = float(input("Ingrese el costo del producto: $"))

            try:
                producto["precio"] = float(input("Ingrese el precio: $"))
            except ValueError:
                print("Ingrese un precio valido")

            try:
                producto["stock"] = int(input("¿Cuantos deseas agregar?:"))
            except ValueError:
                print("Esa cantidad no es valida")
            clasificar = input("¿A que categoria permanece?")
            if clasificar in categorias:
                producto["categoria"] = clasificar

            if producto["precio"] > 0 and len(producto["nombre"]) > 0 and producto["stock"] >= 0 and producto["costo"] >= 0:
                inventario.append(producto)
            else:
                print("Algo salio mal ✖️")

    return inventario

def editar_categorias():
    i = 1
    editar_categoria = int(input("Eligue la opcion que desees: \n 1.Agregar categoria. \n2.Eliminar categoria. \n3.Salir."))
    if editar_categoria == 1:
        agregar = input("Nombre de la categoria: ")
        categorias.append(agregar)
    if editar_categoria == 2:
        for categoria in categorias:
            print(f"{i}. {categoria}")
            i += 1
        try:
            eliminar = int(input("Eliminar categoria: (pon su numero)"))
        except ValueError:
            print("Ingrese un numero valido")
        categorias.pop(eliminar - 1)
    elif editar_categoria == 3:
        return categorias

print("==========================================================================================")
print("ingrese una opcion valida: \n 1. Agregar nuevo producto. \n 2. Visualizar el inventario. \n"
      "3.Editar categorias. \n 4. Salir")
print("==========================================================================================")
print()

try:
    opcion = int(input("Seleccione una opcion: "))
except ValueError:
    print("Ingrese una opcion valido")

while opcion !=4:
    if opcion ==1:
        nuevo_producto = int(input("¿Cuantos productos nuevos ingresara?"))
        agregar_producto(nuevo_producto)

    elif opcion == 2:
        if inventario == []:
            print("No hay productos")

        else:
            print(inventario)

    elif opcion ==3:
        editar_categorias()
    print()
    print("==========================================================================================")
    try:
        opcion = int(input("Seleccione una opcion de vuelta: "))
    except ValueError:
        print("Esa opcion no es valida")