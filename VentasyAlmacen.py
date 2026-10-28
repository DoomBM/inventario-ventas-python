inventario = []
categorias = []
productos = {}


def mostrar_inventario():
    for producto in inventario:
        print(f"ID: {productos['ID']}- '{producto['nombre']}'")
        print(f"En existencia: {producto['stock']}")
        print(f"Costo: ${producto['costo']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Categoria: {producto['categoria']}")
        print("---------------------------------")

def agregar_producto():
    otro = True
    while otro:
        productos["ID"] = len(inventario ) + 1
        while True:
            nombre = input("Ingrese el nombre del producto: ").strip()
            if len(nombre) > 0:
                productos["nombre"] = nombre
                break
            print("El nombre no puede estar vacío. Inténtalo de nuevo.")
        while True:
            try:
                productos["costo"] = float(input("Ingrese el costo del producto: $"))
                break
            except ValueError:
                print("Ingrese un numero valido")


        while True:
            try:
                productos["precio"] = float(input("Ingrese el precio: $"))
                break
            except ValueError:
                print("Ingrese un precio valido")
        while True:
            try:
                productos["stock"] = int(input("¿Cuantos deseas agregar?:"))
                break
            except ValueError:
                print("Esa cantidad no es valida")
        while True:
            clasificar = input("¿A que categoria permanece?")
            if clasificar in categorias:
                productos["categoria"] = clasificar
                break
            else:
                mensaje = input("Esa categoria no existe, ¿Deseas agregarla?")
                if mensaje.lower() == "si":
                    categorias.append(clasificar)
                    productos["categoria"] = clasificar
                    print("Categoria agregada")
                    break
                else:
                    print("Algo salio mal")

        if (productos["precio"] > 0 and len(productos["nombre"]) > 0
                and productos["stock"] >= 0 and productos["costo"] >= 0):
            inventario.append(productos)
            print()
            print("Producto agregado")
        else:
            print("Algo salio mal ✖️")
        agregar = input("Desea agregar otro producto? (presiona 'S' si es asi y enter para salir)")
        if agregar.upper() == "S":
            otro = True
        else:
            otro = False
    
    mostrar_inventario()



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
                elimina = int(input("Eliminar categoria (pon su numero): "))
                if 1 <= elimina <= len(categorias):
                    categorias.pop(elimina - 1)
                    print("Categoria eliminada.")
                    break
                print("Categoria inexistente.")
            except ValueError:
                print("Ingrese un numero valido.")

    elif editar_categoria == 3:
        return

def buscar_productos(buscar):
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return
    encontrado = False
    for producto in inventario:
        es_id = buscar.isdigit() and producto["ID"] == int(buscar)
        es_nombre = producto["nombre"].lower() == buscar.lower()
        if es_id or es_nombre:
            encontrado = True
            print("-" * 30)
            print(f"ID: {producto['ID']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"En existencia: {producto['stock']}")
            print(f"Costo: ${producto['costo']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Categoria: {producto['categoria']}")
            print("-" * 30)

        modificar = input("¿Quieres realizarle alguna modificación? (Escribe 'Y' para aceptar): ")
        if modificar.upper() == "Y":
            actualizar_datos(producto['ID'])

        break
    if not encontrado:
        print("No se encontró ningún producto con ese nombre o ID.")

def actualizar_datos(buscar):
        for producto in inventario:
            if producto["ID"] == int(buscar):
                while True:
                    modificar = int(input("¿Que deseas cambiar?"
                                      "\n1.Nombre"
                                      "\n2.Stock"
                                      "\n3.Costo"
                                      "\n4.Precio"
                                      "\n5.Categoria"
                                      "\n6.Salir"))
                    if modificar == 1:
                        print(f"El nombre actual de este producto es: {producto['nombre']}")
                        nuevo_nombre = input("Cambiar el nombre a: ").strip()
                        id_actual = producto['ID']
                        if not nuevo_nombre:
                            print("El nombre no puede estar vacio")
                        elif any(producto['nombre'] == nuevo_nombre and producto['ID'] != id_actual for producto in
                               inventario):
                            print("Ese nombre ya está siendo usado por otro producto.")
                        else:
                            producto["nombre"] = nuevo_nombre
                            print("¡Nombre actualizado con éxito!")
                    elif modificar == 2:
                        print(f"El stock actual de este producto es: {producto['stock']}")
                        while True:
                            try:
                                nuevo_stock = int(input("Cambiar el stock a: "))
                                if nuevo_stock >= 0:
                                    producto['stock'] = nuevo_stock
                                    break
                            except ValueError:
                                print("Ingrese un numero valido.")
                    elif modificar == 3:
                        print(f"El costo actual de este producto es de: ${producto['costo']}")
                        while True:
                            try:
                                nuevo_costo = float(input("Cambiar el costo de este producto: "))
                                if nuevo_costo >= 0:
                                    producto['costo'] = nuevo_costo
                                    break
                            except ValueError:
                                print("Ingrese un numero valido.")
                    elif modificar == 4:
                        print(f"El precio actual de este producto es de: ${producto['precio']}")
                        while True:
                            try:
                                nuevo_precio = float(input("Cambiar el precio de este producto: "))
                                if nuevo_precio >= 0:
                                    producto['precio'] = nuevo_precio
                                    break
                            except ValueError:
                                print("Valor invalido")
                    elif modificar == 5:
                        print(f"La categoria actual de este producto es: {producto['categoria']}")
                        cambiar_categoria = input("Cambiar el categoria de este producto: ")
                        if cambiar_categoria in categorias:
                            if cambiar_categoria == producto['categoria']:
                                producto['categoria'] = cambiar_categoria
                        else:
                            print("Esa categoria no existe")
                    elif modificar == 6:
                        return
                    else:
                        print("Opcion invalida.")
        return

def eliminar_producto(buscar):
    if len(inventario) == 0:
        print("No hay elementos en el inventario.")
        return
    for producto in inventario:
        es_id = buscar.isdigit() and producto["ID"] == int(buscar)
        es_nombre = producto["nombre"].lower() == buscar.lower()
        if es_id or es_nombre:
            confirmar = input(f"¿Seguro que quieres eliminar '{producto['nombre']}'? (Y/N): ")
            if confirmar.upper() == "Y":
                inventario.remove(producto)
                print(f"El producto '{producto['nombre']}' ha sido eliminado.")
            else:
                print("Eliminación cancelada.")
            return
    print("No se encontró ningún producto con ese nombre o ID.")

def poco_stock():
    for producto in inventario:
        if producto["stock"] <= 5:
            print(f"Hay poco stock del producto {producto['nombre']}!!")

def venta():
    carrito = []
    agregados = {}
    validacion = True
    while validacion:
        agregados["nombre"] = input("¿Que producto ingresara al carrito?: ")
        if len(agregados) == 0:
            print("Producto no encontrado")
            break
        for producto in inventario:
            if producto["nombre"] == agregados["Nombre"]:
                carrito.append(producto)
            while True:
                try:
                    num = int(input("Cual es la cantidad que llevaras?"))
                    if num >= 0:
                        agregados["cantidad"] = num
                        break
                except ValueError:
                    print("Ingrese un numero valido.")
        otro_product = input("¿Deseas agregar otra cosa? (presione 'S' para confirmar o enter para salir): " )
        if otro_product == "S":
            validacion = True
        else:
            validacion = False



print("=" * 30)
print("ingrese una opcion valida: "
      "\n1. Agregar nuevo producto. "
      "\n2. Visualizar el inventario. \n"
      "3. Editar categorias. "
      "\n4. Buscar producto. "
      "\n5. Eliminar producto o categoria."
      "\n6. Salir" )
print("=" * 30)

poco_stock()
print()

mostrar_inventario()

while True:
    try:
        opcion = int(input("Seleccione una opcion: "))
        break
    except ValueError:
        print("Ingrese una opcion valida")

while opcion !=6:
    if opcion ==1:
        agregar_producto()

    elif opcion == 2:
        if not inventario:
            print("No hay productos")

        else:
            mostrar_inventario()

    elif opcion ==3:
        editar_categorias()

    elif opcion == 4:
        buscar_producto = input("¿Que producto buscas?")
        buscar_productos(buscar_producto)
    elif opcion ==5:
        eliminar = input("¿Que producto vas a eliminar?")
        eliminar_producto(eliminar)

    print()
    print("==========================================================================================")
    try:
        poco_stock()
        opcion = int(input("Seleccione una opcion de vuelta: "))
    except ValueError:
        print("Esa opcion no es valida")