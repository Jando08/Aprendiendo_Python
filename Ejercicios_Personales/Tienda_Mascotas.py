# 1. Convertimos a mayúsculas y lo guardamos en la misma variable para poder imprimirlo modificado
bienvenida = 'Bienvenido a Nuestra Tienda de Mascotas'
bienvenida = bienvenida.upper()
print(bienvenida)

# pedir el nombre y edad al usuario
nombre = input('Ingrese su nombre por favor (no apellidos): ')
# corregimos el nombre de inmediato para que empiece con mayúscula
nombre = nombre.capitalize()

edad = int(input('Ingrese su edad por favor: '))
mensaje = ''
descuento = 10

# validar que el usuario pueda comprar en la tienda
if edad < 12:
    mensaje = 'No puede realizar una compra, necesita la supervisión de un adulto.'
else:
    
    # creando la lista de productos
    productos = ['Croquetas', 'Juguetes']

    # pedirle al usuario que ingrese un nuevo producto
    nuevo_producto = input('Ingresa el producto que desea comprar por favor: ')
    productos.append(nuevo_producto)
    
    print(f"\nTu carrito actual es: {productos}")

    # pedirle al usuario el total de su compra
    total_compra_sin_descuento = float(input('Ingrese el total de su compra por favor: '))

    # evaluamos los descuentos AQUÍ ADENTRO, donde la variable sí existe
    if nombre == 'Jando':
        mensaje = '¡Hola Jando! Por ser el dueño de la tienda tu total es: $0'
    elif total_compra_sin_descuento > 50:
        total_compra_con_descuento = total_compra_sin_descuento - descuento
        mensaje = f'Su compra al ser mayor de 50 pesos ({total_compra_sin_descuento}), se le descuenta {descuento}, y su precio final es de {total_compra_con_descuento}'
    else:
        mensaje = f'Usted no cuenta con descuento, por lo tanto su compra total queda en {total_compra_sin_descuento}'     

# Imprimimos el mensaje final (ya sea el de menor de edad o el del resultado de la compra)
print("\n" + mensaje)