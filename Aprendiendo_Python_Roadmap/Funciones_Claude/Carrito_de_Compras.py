def agregar_producto(carrito, nombre, precio):
    carrito.append({'nombre': nombre, 'precio': precio})
    return carrito

def calcular_total(carrito):
    total = 0
    for producto in carrito:
        total = total + producto['precio']
    return total

def mostrar_carrito(carrito):
    print('--- Tu carrito ---')
    for producto in carrito:
        print(f"{producto['nombre']}: ${producto['precio']}")
    print(f"Total: ${calcular_total(carrito)}")

carrito = []
carrito = agregar_producto(carrito, "Manzanas", 25.0)
carrito = agregar_producto(carrito, "Leche", 18.5)
carrito = agregar_producto(carrito, "Pan", 12.0)
mostrar_carrito(carrito)