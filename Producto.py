class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Sandwish(Producto):
    def __init__(self, nombre, precio, ingredientes):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes
        
    def pedido(self):
        print(f"Nombre sandwish: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Ingredientes: {', '.join(self.ingredientes)}")