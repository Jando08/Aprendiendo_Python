'''
Reto: Tienes un sistema que detecta enlaces web. 
Pide al usuario que introduzca una URL. 
Si la URL comienza con "https", imprime "La conexión es segura"; de lo contrario, imprime
"La conexión no es segura"
'''

#pedirle al usuario que ingrese una url
url = input('Ingrese una url de un link de lo que quieras: ')
mensaje = ''

if url.startswith('https'):
    mensaje = 'La conexio es segura'
else:
    mensaje = 'La conexion es insegura'    


#imprimir mensaje final
print(mensaje)    