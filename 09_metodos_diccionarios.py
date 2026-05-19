#diccionario
diccionario = {
    'nombre' : 'Alejandro',
    'apellido' : 'Leyva',
    'edad' : 20
}


claves = diccionario.keys()
valor_de_kasdks = diccionario.get('kasdks')
print('jojojojojo')

#eliminar todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario, si quiero eliminar mas de uno es .pop('parametro1', 'parametro2'), solo se le agrega una coma
diccionario.pop('nombre')

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)