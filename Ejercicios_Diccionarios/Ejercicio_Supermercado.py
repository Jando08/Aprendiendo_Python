#crear el diccionario
carrito = {
    'Pantalon' : 350,
    'Camisa' : 200,
    'Tenis' : 800
}

#calcular el total de los productos
total = carrito['Pantalon'] + carrito['Camisa'] + carrito['Tenis']

#pedirle al usuario que ingrese un cupon de descuento
descuento = input('Ingresa un cupon de descuento(%): ')
mensaje = ''

if descuento == 'DESCUENTO10':
    total -= 100
    mensaje = f'!Cupon valido, Se han descontado 100 pesos'
else:
    mensaje = '!Cupon no valido o caducado'

print(mensaje)
print(f'El total de su compra ahora es {total}')
