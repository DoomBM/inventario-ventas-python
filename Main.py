import Almacen
import Ventas
import Compras
hirtorial_ventas = []
historial_compras = []

print("=== PAPELERIA TODO A LA MANO ===")

print("¿A que seccion iremos hoy?")

while True:
    seccion = input("1. Almacen \n2. Ventas \n3. Compras \n7. Cerrar\n6. Cerrar\n").strip()
    if seccion.lower() == "1" or seccion.lower() == "almacen":
        Almacen.menu_almacen()

        continuar =input("Presione cualquier tecla para finalizar Finalizar \n2. R) Regresar")
        if continuar.upper() == "R":
            Almacen.menu_almacen()
        else:
            continue
    elif seccion.lower() == "2" or seccion.lower() == "ventas":
        registrar_venta = Ventas.venta()
        hirtorial_ventas.append(registrar_venta)

        continuar = input("Presione cualquier tecla para finalizar Finalizar \n2. R) Regresar")
        if continuar.upper() == "R":
            registrar_venta = Ventas.venta()
            hirtorial_ventas.append(registrar_venta)
        else:
            continue
    elif seccion.lower() == "3" or seccion.lower() == "compras":
        registrar_compra = Compras.compra_de_producto()
        historial_compras.append(registrar_compra)

        continuar = input("Presione cualquier tecla para finalizar Finalizar \n2. R) Regresar")
        if continuar.upper() == "R":
            registrar_compra = Compras.compra_de_producto()
            historial_compras.append(registrar_compra)
        else:
            continue
    elif seccion.lower() == "4" or seccion.lower() == "historial de ventas":
        print("==historial de ventas==")
        for venta in historial_compras:
            print(venta)
    elif seccion.lower() == "5" or seccion.lower() = "historial de ventas":
        print("==historial de ventas==")
        for compra in historial_compras:
            print(compra)
    elif seccion.lower() == "6" or seccion.lower().lower() == "cerrar":
        break

    else:
        continue






