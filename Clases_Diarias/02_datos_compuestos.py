# creando una lista que se puede modificar
lista = ["Jando", "Andronova", "Dmitry", "Svetlana"]
# creando una tupla que no se puede modificar
tupla = ("Jando", "Andronova", "Dmitry", "Svetlana")
print(tupla)

# para acceder a un elemento de la lista se utiliza el numero
# de indice el cual tenga, en python los indices empiezan en 0
'''
print(lista[0])  # Jando
print(lista[1])  # Andronova
print(lista[2])  # Dmitry
print(lista[3])  # Svetlana
'''

# la diferencia entre una lista y una tupla es que la tupla no se puede modificar

#ejemplo
#esto si funciona
lista[3] = "Maquinola"
#esto no funciona
#tupla[3] = "Maquinola"


#creando un conjunto set
conjunto = {"Jando", "Andronova", "Dmitry", "Svetlana"}
#los conjutos no se pueden modificar pero si se pueden agregar elementos
#ademas no puedes acceder a un elemtno por su indice, y no permite valores repetidos

#creando un diccionario, la estructura es key : value y separamos por comas
diccionario = {
    'nombre': 'jando',
    'apellido' : 'parra',
    'edad' : 20,
    'apodo' : 'andronova'
}
#para imprimir valores de los diccionarios en lugar de utilizar su indice se utiliza
# la clave o nombre del diccionario
print(diccionario['edad'])