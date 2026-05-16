'''
Reto: Pide al usuario su nombre de pila en minúsculas (ej: "pedro"). 
Tu programa debe corregirlo automáticamente para que la primera letra sea mayúscula ("Pedro").
'''

#pedir el nombre al usuario
nombre_normal = input('Ingrese su nombre en minusculas: ')

#convertir la primera letra del nombre
nombre_mayuscula = nombre_normal.capitalize()

#imprimir nombre
print(f'Su nombre paso de {nombre_normal} a: {nombre_mayuscula}')

