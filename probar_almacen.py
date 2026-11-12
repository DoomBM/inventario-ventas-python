import Almacen

# Productos de prueba
Almacen.inventario.clear()

Almacen.inventario.extend([
    {
        "ID": 1,
        "nombre": "Cuaderno",
        "stock": 20,
        "costo": 15,
        "precio": 25,
        "categoria": "Papelería"
    },
    {
        "ID": 2,
        "nombre": "Lapiz",
        "stock": 50,
        "costo": 3,
        "precio": 5,
        "categoria": "Papelería"
    }
])

# Prueba 1: buscar por ID
Almacen.buscar_productos("1")
