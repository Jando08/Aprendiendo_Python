'''
Reto: Imagina que estás creando un sistema de inicio de sesión. 
El usuario ingresa su correo electrónico mezclando mayúsculas y minúsculas (Ej: CoRReO@eXamPle.com).
Asegúrate de normalizarlo convirtiéndolo todo a minúsculas para guardarlo limpio en tu base de datos.
'''

#pedir al usuario que ingrese los valores
correo_normal = input('Ingrese su correo electronico: ')
password_normal = input('Ingrese su contrasenia: ')

#convertir las cadenas a minusculas
correo_minuscula = correo_normal.lower()
password_minuscula = password_normal.lower()

#imprimir en pantalla el resultado
print(f'Su correo fue convertido de {correo_normal} a : {correo_minuscula}')
print(f'Su contrasenia fue convertida de {correo_normal} a : {correo_minuscula}')