jugador = input('Ingrese el nombre del nuevo jugador de los Lakers: ')

try:
    # Intentamos hacer la operación con el archivo
    with open('seleccionados.txt', 'a') as archivo:
        archivo.write(f'{jugador}\n')
    
    # Si todo sale bien, se ejecuta este mensaje
    print(f'El jugador {jugador} ha sido guardado con éxito!')

except PermissionError:
    print("Error: No tienes permisos para escribir en este archivo.")

except Exception as e:
    # Este es nuestro escudo general por si pasa cualquier otra cosa rara
    print(f"Ocurrió un error inesperado al guardar: {e}")
