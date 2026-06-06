with open('seleccionados.txt', 'r') as archivo:
    for linea in archivo:
        jugador = linea.strip().upper()
        
        if jugador.startswith('A'):
            print(linea.strip())