#crear diccionario
alumnos = {
    "ana": [9, 8, 10],
    "pedro": [6, 7, 6],
    "lucia": [10, 10, 9]
}

#preguntar al usuario cual alumno buscar
buscar_alumno = input('Ingrese el nombre del usuario que desea buscar (Ana, Pedro, Lucia): ')
buscar_alumno = buscar_alumno.lower()
mensaje = ''

if buscar_alumno in alumnos.keys():
    notas = alumnos[buscar_alumno]
    #calcular el promedio
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    mensaje = f'El promedio del {buscar_alumno} es = {promedio}'
else:
    mensaje = 'El alumno no existe'


#imprimir promedio en base al alumno
print(mensaje)
