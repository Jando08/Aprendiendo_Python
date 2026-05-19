#crear el diccionario
mascota = {
    'nombre' : 'nachita',
    'especie' : 'perro',
    'edad' : 3
}

#modificar un valor 
#cuando se le quiere sumar o restar un valor a un valor no fijo es diccionario['campo'] += 1
mascota['edad'] = 4
#mascota['edad'] += 1

#preguntarle al dueño de que color es la mascota
color_mascota = input('Ingrese el color de su mascota: ')

#agregar el color de la mascota al diccionario
mascota['color'] = color_mascota

print(mascota)