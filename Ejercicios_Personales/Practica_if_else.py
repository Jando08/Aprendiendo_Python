usuario_registrado = True
password_correcto = False
mensaje = ''

#validar que el usuario este registrado
if usuario_registrado == True:
    if password_correcto == True:
        mensaje = 'Bienvenido al sistema'
    else:
        mensaje = 'Contrasnia incorrecta'
else:
    mensaje = 'El usuario no existe'