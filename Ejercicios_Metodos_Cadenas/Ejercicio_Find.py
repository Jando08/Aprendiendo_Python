'''
Reto: Tienes el siguiente texto de un correo electrónico: "Hola, te escribo para decirte que tu código secreto es 9982". 
Usa el método para averiguar en qué posición exacta del texto empieza la palabra "secreto".
'''

#pedirle la frase al usuario
frase = 'Hola, te escribo para decirte que tu código secreto es 9982'

#encontrar la posicion de secreto
encontrar_palabra = frase.find('secreto')

#imprimir resultado
print(encontrar_palabra)