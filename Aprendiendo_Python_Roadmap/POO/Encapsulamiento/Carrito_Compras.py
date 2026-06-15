class CarritoTech:
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        self.productos = []
        self.total_a_pagar = 0

    
    def agregar_producto(self, nombre_producto, precio):
        self.productos.append(nombre_producto)
        self.total_a_pagar += precio
        print(f"Se ha agregado el producto {nombre_producto} con el precio de {precio}")

    def remover_producto(self, nombre_producto, precio):
        if nombre_producto in self.productos:
            self.productos.remove(nombre_producto)
            self.total_a_pagar -= precio
            print(f"El producto {nombre_producto} ha sido removido con exito")
        else:
            print(f"Cuidado! {nombre_producto} no esta en la lista del carrito")


    def ver_carrito(self):
        num_productos = len(self.productos)
        print("\n--- 📊 RESUMEN DEL ORGANIZADOR ---")
        print(f"Productos gregador al carrito {num_productos}, {self.productos } \n")
        print(f"Total del carrito: {self.total_a_pagar}")
        print("-----------------------------------\n")


# pruebas
# 1. Creamos el carrito de compras
mi_carrito = CarritoTech("Alejandro")

# 2. Agregamos componentes al carrito
mi_carrito.agregar_producto("Teclado Mecanico Keychron", 1500)
mi_carrito.agregar_producto("Mouse Gamer Inalambrico", 800)
mi_carrito.agregar_producto("Set de Stickers de Kanye West", 120)

# 3. Revisamos el carrito para ver el total
mi_carrito.ver_carrito()

# 4. Nos arrepentimos del mouse y lo quitamos
mi_carrito.remover_producto("Mouse Gamer Inalambrico", 800)

# 5. Volvemos a revisar el estado final del carrito
mi_carrito.ver_carrito()
