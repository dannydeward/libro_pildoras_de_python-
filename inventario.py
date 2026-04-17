class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrar(self):
        for p in self.productos:
            print(f"{p.nombre} - ${p.precio}")

inv = Inventario()
inv.agregar(Producto("Galletas", 100))
inv.agregar(Producto("Jugo", 80))
inv.mostrar()
