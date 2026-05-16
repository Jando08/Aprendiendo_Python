'''
Reto: Pide al usuario el título de su película favorita en minúsculas (ej: "el señor de los anillos"). 
El programa debe formatearlo correctamente como un título real, donde cada palabra inicie con mayúscula.
'''

#pedir al usuario el nombre de la pelicula
nom_peli_minu = input('Ingresa el nombre de tu pelicula favorita en minusculas: ')

#convertir la cadena con .title()
nom_peli_mayu_prim_letra = nom_peli_minu.title()

#imprimir el resultado
print(nom_peli_mayu_prim_letra)