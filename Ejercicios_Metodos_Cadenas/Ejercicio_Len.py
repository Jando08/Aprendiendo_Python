'''
Reto (Validación de tweets): Pide al usuario que escriba un pensamiento. 
Si el texto tiene más de 140 caracteres, muéstrale un mensaje que diga "Tu mensaje es demasiado largo para publicar". 
Si no, dile "Mensaje publicado con éxito".
'''

#pedir el tweet al usuario
tweet = input('Que estas pensando ahora mismo: ')
mensaje = ''
calcular_caracteres = 0

#calcular el total de caracteres
calcular_caracteres = len(tweet)

#imprimir mensaje dependiendo la longitud
if calcular_caracteres > 140:
    mensaje = 'Tu mensaje es demasiado largo para publicar'
else:
    mensaje = 'Mensaje publicado con exito'

#imprimr mensaje final
print(mensaje)

