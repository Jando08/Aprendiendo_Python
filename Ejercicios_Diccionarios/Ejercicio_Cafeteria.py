# Crear el diccionario
menu = {
    'expresso': {'precio' : 30, 'tiempo' : 2},  # Recuerda escribirlo igual en la consola
    'capuccino' : {'precio' : 50, 'tiempo' : 5},
    'latte' : {'precio' : 45, 'tiempo' : 4}
}

# Preguntar el nombre al usuario
nombre = input('Ingrese su nombre: ')
nombre = nombre.capitalize()

# Preguntar al usuario qué café desea ordenar
cafe_pedido = input(f'Buenos días {nombre}, ingrese el café que desea ordenar [Expresso, Capuccino, Latte]: ')
cafe_pedido = cafe_pedido.lower()
mensaje = ''

# Validar que el café existe
if cafe_pedido in menu.keys():
    precio = menu[cafe_pedido]['precio']
    tiempo = menu[cafe_pedido]['tiempo']
    
    mensaje = f'¡Perfecto! Tu {cafe_pedido} cuesta ${precio} pesos y tardará {tiempo} minutos.'
else:
    mensaje = 'Lo sentimos, no tenemos ese tipo de café en el menú.'

# Imprimir mensaje final
print(mensaje)