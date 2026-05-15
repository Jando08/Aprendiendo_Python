#hacer un programa para calcular descuento

#pedir al usuario el total de su compra
compra_sin_descuento = float(input('Ingrese el total de su compra: '))
descuento = 0.0
compra_con_descuento = 0.0
mensaje = ''

#imprimr mensaje dependiendo del total de la compra
if compra_sin_descuento > 100:
    descuento = compra_sin_descuento * 0.20
    compra_con_descuento = compra_sin_descuento - descuento
    mensaje = f'Felicidades, tienes un descuento del 20%. El total de tu compra con descuento es: {compra_con_descuento}'
elif compra_sin_descuento > 50:
    descuento = compra_sin_descuento * 0.10
    compra_con_descuento = compra_sin_descuento - descuento
    mensaje = f'Felicidades, tienes un descuento del 10%. El total de tu compra con descuento es: {compra_con_descuento}'
else:
    mensaje = f'Lo sentimos, no tienes descuento. El total de tu compra es: {compra_sin_descuento}'

#imprimir mensaje
print(mensaje)