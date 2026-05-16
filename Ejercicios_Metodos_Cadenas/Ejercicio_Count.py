'''
Reto: Pide al usuario que escriba un trabalenguas. 
Tu programa debe contar y mostrar cuántas veces se repite la letra "r" en todo el texto.
'''

#pedir al usuario que escriba un trabalenguas
trabalenguas = input('Ingresa un trabalenguas: ')

#calcular cuantas veces sale la "r" en el trabalenguas
letra_encontrada = trabalenguas.count('r')

#imprimir el resultado
print(f'La letra r fue encontrada un total de {letra_encontrada} veces en el trabalenguas')

