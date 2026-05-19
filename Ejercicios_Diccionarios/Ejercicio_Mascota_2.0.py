# Crear el diccionario
mascota = {
    'nombre' : 'nachita',
    'especie' : 'perro',
    'edad' : 3
}

#preguntar al usuario qué parámetro quiere buscar
consulta = input('Qué información desea saber sobre su mascota (Nombre, Especie o Edad): ')

#guardamos el texto convertido a minúsculas
consulta = consulta.lower()
mensaje = ''

#condición si la búsqueda es exitosa
if consulta in mascota.keys():
    mensaje = f'Si tenemos ese dato guardado. El valor es: {mascota[consulta]}'
else:
    mensaje = 'Lo siento, ese dato no está registrado en el sistema'

print(mensaje)