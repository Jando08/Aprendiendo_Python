"""
Abre un bloque try.
Pídele al usuario el precio de un producto y la cantidad de productos.
Calcula el total multiplicando ambos valores.
Muestra el resultado con un f-string: "El total a pagar es de $[total] pesos."
Añade un bloque except ValueError. 
Si el usuario escribe letras en el precio o en la cantidad,"Error: Has ingresado un dato inválido. Por favor, asegúrate de usar números."
"""

nombre = input("Ingrese su nombre: ")
print(f'Bienvenido {nombre}')


try:
    precio_producto = float(input('Ingresa el precio del producto: '))
    cantidad_producto = int(input('Ingresa la cantidad de producto(s) que compraste: '))
    total = precio_producto * cantidad_producto
    mensaje = f'El total a pagar es ${total} pesos'
except ValueError:
    mensaje = 'Error: Has ingresado un dato inválido. Por favor, asegúrate de usar números.'


print(mensaje)