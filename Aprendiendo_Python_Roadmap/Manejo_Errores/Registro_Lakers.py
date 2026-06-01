nombre_jugador = "Austin Reaves"
edad_ingresada = "veintidos"  
puntos_por_partido = 15       


try:
    edad_numero = int(edad_ingresada)
    proyeccion = nombre_jugador + str(puntos_por_partido)
    print('Registro exitoso sin errores')
except ValueError:
    print('Error de Edad: La edad debe ser un numero escrito en digitos, no en letras ')
except TypeError:
    print('Error de Tipo: No puedes concatenar texto con números directos. Usa str().')


print('Sistema de registro cerrado.')