# Carrito inicial
carrito = ["Laptop", "Mouse Gamer", "Teclado Mecánico"]
print(f"Carrito inicial: {carrito}")

# Acción 1: Agregar al final
carrito.append('Audífonos')

# Acción 2: Agregar al principio
carrito.insert(0, 'Monitor Premium')

# Acción 3: Borrar por nombre específico
carrito.remove('Mouse Gamer')

# Acción 4 y 5: Corregido con f-string para que el usuario entienda los datos
print(f"\nTienes un total de {len(carrito)} productos listos para pagar.")
print(f"Tu carrito final es: {carrito}")