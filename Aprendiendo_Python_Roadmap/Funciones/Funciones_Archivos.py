def agregar_jugador(nombre):
    nombre_limpio = nombre.strip().upper()

    with open('seleccionados.txt', 'a') as archivo:
        archivo.write(f'{nombre_limpio}\n')
        
    return nombre_limpio
    

agregar_jugador(' Lionel Messi ')
agregar_jugador(' Lamine Yamal ')

