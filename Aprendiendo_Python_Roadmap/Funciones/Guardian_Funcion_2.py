def validar_seguridad(password): 
    return len(password) >= 8


mi_password = input("Crea tu nueva contraseña: ")
es_segura = validar_seguridad(mi_password)


if es_segura:
    mensaje = "¡Contraseña creada con éxito!"
else:
    mensaje = "Error: La contraseña debe tener al menos 8 caracteres."

print(mensaje)