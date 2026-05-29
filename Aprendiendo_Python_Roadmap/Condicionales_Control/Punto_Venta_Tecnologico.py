"""
Pídele al usuario el precio de un producto usando input() con el mensaje: "Ingresa el precio del producto (ej. 599.99): ". Guarda esto en la variable precio_texto.
Pídele al usuario la cantidad de productos que va a comprar usando input() con el mensaje: "¿Cuántas unidades llevarás?: ". Guarda esto en la variable cantidad_texto.
Aplica las Conversiones Explícitas:
Convierte precio_texto a un número decimal (float) y guárdalo en una nueva variable llamada precio_numero.
Convierte cantidad_texto a un número entero (int) y guárdalo en una nueva variable llamada cantidad_numero.
Calcula el Total: Multiplica precio_numero por cantidad_numero y guarda el resultado en una variable llamada total_pagar.
crea una variable llamada total_string y convierte explícitamente total_pagar a tipo cadena de texto (str()).
Muestra el resultado final usando un f-string: "El total a pagar por tus [cantidad_numero] productos es de $[total_string] pesos."
"""

# Guardar valores de la compra
precio_texto = input('Ingresa el precio del producto: ')
cantidad_texto = input('¿Cuántas unidades llevarás?: ')

# Hacer las conversiones
precio_numero = float(precio_texto)
cantidad_numero = int(cantidad_texto)

# Calcular el total a pagar
total_pagar = precio_numero * cantidad_numero

# Imprimir resultado final
total_string = str(total_pagar)
print(f'El total a pagar por tus {cantidad_numero} productos es de ${total_string} pesos')