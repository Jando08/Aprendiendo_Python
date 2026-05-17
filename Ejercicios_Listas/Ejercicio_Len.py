'''
Reto (Carrito de compras): Tienes una lista con los productos que un usuario quiere comprar: 
carrito = ["Camisa", "Pantalón", "Zapatos", "Gorra"]. Usa el método adecuado para imprimir un mensaje que diga: 
"Tienes X productos en tu carrito de compras" (donde X sea el número real de elementos).
'''

#crear la lista
carrito = ['Camisa', 'Pantalon', 'Zapatos', 'Gorra', 'Cinto']

#calcular el total de elementos que tento en la lista carrito
calcular_carrito = len(carrito)

#imprimir el total de elementos
print(f'Tiene un total de {calcular_carrito} productos en su carrito')