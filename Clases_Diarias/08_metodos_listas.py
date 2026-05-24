#creando una lista con list
lista = list(['Hola', 'Dalto', 34])
lista2 = list([2, 3, 34, 5, 6, 7])

cadena = 'Hola'
#devuelve la cantidad de elementos de las listas
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("5")

#agregando a un elemento a la lista en un indice en especifico
lista.insert(2, 'Hola mami')

#agregando varios elementos a la lista
lista.extend([False, 2030])

#eliminando un elemento de la lista por su indice
lista.pop(3) #NOTA: si en el indice ponemos -1, se elimina el ultimo elemento de la lista


#removiendo un elemetno de la lista por su valor
lista.remove('Hola')

#ordenamos la lista (si usamos el parametro reverse=true lo ordena en reversa)
#list2.sort(reverse=True)


#invirtiendo los elementos de una lista
lista.reverse()

#elimiando todos los elementos de la lista
#lista.clear()

print(lista)