'''
Reto (Fila del banco): 
Tienes la fila del banco en orden de llegada: 
fila = ["Cliente 1", "Cliente 2", "Cliente 3"]. 
De repente llega un cliente VIP que tiene prioridad y debe ser 
atendido inmediatamente en el índice 0. 
Agrega "Cliente VIP" en esa posición exacta sin borrar a los demás e imprime la fila.
'''

#crear la fila
fila = ['Cliente 1', 'Cliente 2', 'Cliente 3']

#insertar cliente
nuevo_cliente = fila.insert(0, 'Cliente VIP')

#imprimir nueva fila
print(f'La fila nueva a quedado asi {fila}')


#estructura para insertar cliente
# nombre_lista.insert(indice, 'valor a insertar')