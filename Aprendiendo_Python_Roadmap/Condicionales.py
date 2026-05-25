"""
Crea una variable llamada temperatura y asígnale un valor numérico
Escribe una estructura condicional (if, elif, else) que evalúe la temperatura
bajo las siguientes reglas:
Si la temperatura es mayor a 30, debe imprimir: "Hace mucho calor."
Si la temperatura está entre 18 y 30 debe imprimir: "La temperatura es agradable."
Si la temperatura es menor a 18, debe imprimir: "Hace frío. Encendiendo la calefacción."
"""


# creamos variables y pedimos la temperatura al usuario
temperatura = int(input("Ingres la temperatura: "))
mensaje = ""

# imprimiendo mensaje dependiendo de la temperatura
if temperatura > 30:
    mensaje = 'Hace mucho calor. Prende el aire w'
elif temperatura >= 18:
    mensaje = 'La temperatura es agradable'
else:
    mensaje = 'Hace frio. Encendiendo la calefaccion'

# imprimiendo mensaje
print(mensaje)