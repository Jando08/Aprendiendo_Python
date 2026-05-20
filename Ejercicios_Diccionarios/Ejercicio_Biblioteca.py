# Crear el diccionario
biblioteca = {
    'el quijote': {'autor': 'Cervantes', 'copias': 3},
    'harry potter': {'autor': 'J.K. Rowling', 'copias': 1},
    'cien años de soledad': {'autor': 'Gabriel Garcia', 'copias': 0}
}

# Usuario pide libro
libro_prestado = input('Ingrese el nombre del libro que desea llevarse prestado: ')
libro_prestado = libro_prestado.lower()
mensaje = ''

# logica de la biblioteca
if libro_prestado not in biblioteca.keys():
    mensaje = 'Lo siento, ese libro no es parte de nuestro catálogo'
elif libro_prestado in biblioteca.keys() and biblioteca[libro_prestado]['copias'] == 0:
    autor = biblioteca[libro_prestado]['autor']
    mensaje = f'El libro de {autor} existe, pero lamentablemente no quedan copias disponibles'
else:
    autor = biblioteca[libro_prestado]['autor']
    biblioteca[libro_prestado]['copias'] -= 1
    nuevas_copias = biblioteca[libro_prestado]['copias']
    
    mensaje = f'¡Préstamo exitoso! Te llevas un libro de {autor}. Quedan {nuevas_copias} disponibles en el estante'

# Imprimir mensaje final
print(mensaje)