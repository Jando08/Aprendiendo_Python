'''
Reto (Censura de groserías): Tienes la frase "Este examen de programación es una porquería". 
Usa el método para cambiar la palabra "porquería" por "maravilla" antes de mostrar la frase final en pantalla.
'''

#frase con groseria
frase_con_groseria = 'Este examen de programacion es una porqueria'

#convertir la frase con groseria a una mas amigable
frase_sin_groseria = frase_con_groseria.replace('porqueria','maravilla')

#imprimir resultado final
print(f'La frase paso de {frase_con_groseria} a {frase_sin_groseria}') 