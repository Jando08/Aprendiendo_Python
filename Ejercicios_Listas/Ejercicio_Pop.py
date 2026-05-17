'''
Reto (Última tarea completada): Tienes una lista de tareas pendientes: 
tareas = ["Lavar ropa", "Estudiar Python", "Cocinar"].
El usuario acaba de terminar la última tarea de la lista ("Cocinar"). 
Usa el índice negativo -1 para eliminarla de la lista e imprime las tareas restantes.
'''

#crear la lista de tareas pendientes
tareas = ['Lavar ropa', 'Estudiar Python', 'Cocinar']

#eliminar la ultima tarea de la lista
tareas.pop(-1)

#imprimir lista final
print(tareas)