'''
Reto (Fusión de inventarios): Tienes dos almacenes de frutas. 
almacen_a = ["Manzana", "Plátano"] y almacen_b = ["Uva", "Naranja", "Sandía"].
Agrega todos los elementos del almacen_b dentro del almacen_a en un solo paso 
e imprime cómo quedó el almacen_a.
'''

#crear ambas listas
almacen_a = ['Manzana', 'Platano']
almacen_b = ['Uva', 'Naranja', 'Sandia']

#agregar almacen b a almacen a
almacen_a.extend(almacen_b)

#imprimir resultado final
print(almacen_a)

