inventario = []
categorias = []


def agregar_producto(productos):
    if productos > 0:
        for i in range(productos):
            producto = {}
            validacion = True

            producto["ID"] = len(inventario ) + 1
            producto["nombre"] = input(f"Ingrese el nombre del producto {i + 1}: ").strip()
            while validacion == True:
                try:
                    producto["costo"] = float(input("Ingrese el costo del producto: $"))
                    break;
                except ValueError:
                    print("Ingrese un numero valido")
                    validacion = True

            while validacion == True:
                try:
                    producto["precio"] = float(input("Ingrese el precio: $"))
                    break;
                except ValueError:
                    print("Ingrese un precio valido")
                    validacion = True
            while validacion == True:
                try:
                    producto["stock"] = int(input("¿Cuantos deseas agregar?:"))
                    break;
                except ValueError:
                    print("Esa cantidad no es valida")
                    validacion = True
            while validacion == True:
                try:
                    clasificar = input("¿A que categoria permanece?")
                    if clasificar in categorias:
                        producto["categoria"] = clasificar
                        break;
                    else:
                        mensaje = input("Esa categoria no existe, ¿Deseas agregarla?")
                        if mensaje.lower() == "si":
                            categorias.append(clasificar)
                            producto["categoria"] = clasificar
                            print("Categoria agregada")
                            break;
                        else:
                            validacion = True
                except:
                    print("Oops! Algo salio mal")
                    validacion = True
            if producto["precio"] > 0 and len(producto["nombre"]) > 0 and producto["stock"] >= 0 and producto["costo"] >= 0:
                inventario.append(producto)
                print()
                print("Producto agregado")
            else:
                print("Algo salio mal ✖️")

    return inventario

def editar_categorias():
    while True:
        try:
            editar_categoria = int(input(
                "Elige la opcion que desees:\n"
                "1. Agregar categoria.\n"
                "2. Eliminar categoria.\n"
                "3. Salir.\n"
            ))
            if 1 <= editar_categoria <= 3:
                break
            print("Elige una opcion entre 1 y 3.")
        except ValueError:
            print("Ingrese un numero valido.")

    if editar_categoria == 1:
        agregar = input("Nombre de la categoria: ").strip()
        if agregar:
            categorias.append(agregar)
            print("Categoria agregada.")
        else:
            print("El nombre no puede estar vacio.")

    elif editar_categoria == 2:
        if not categorias:
            print("No hay categorias para eliminar.")
            return

        for i, categoria in enumerate(categorias, start=1):
            print(f"{i}. {categoria}")

        while True:
            try:
                eliminar = int(input("Eliminar categoria (pon su numero): "))
                if 1 <= eliminar <= len(categorias):
                    categorias.pop(eliminar - 1)
                    print("Categoria eliminada.")
                    break
                print("Categoria inexistente.")
            except ValueError:
                print("Ingrese un numero valido.")

    elif editar_categoria == 3:
        return
print("==========================================================================================")
print("ingrese una opcion valida: \n 1. Agregar nuevo producto. \n 2. Visualizar el inventario. \n"
      "3.Editar categorias. \n 4. Salir")
print("==========================================================================================")
print()
validar = True
while validar:
    try:
        opcion = int(input("Seleccione una opcion: "))
        break;
    except ValueError:
        print("Ingrese una opcion valida")
        validar = True

while opcion !=4:
    if opcion ==1:
        reinicio = True
        while reinicio == True:
            try:
                nuevo_producto = int(input("¿Cuantos productos nuevos ingresara?"))
                agregar_producto(nuevo_producto)
                break;
            except ValueError:
                print("Ingrese un numero valido por favor")

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