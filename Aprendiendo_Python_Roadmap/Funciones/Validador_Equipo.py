# crear funcion llamada buscar_jugador(nombre, archivo_equipo = 'lakers,txt')
def buscar_jugador(nombre, archivo_equipo = 'lakers.txt'):
    # limpiar nombre y pasarlo a mayusculas
    nombre_buscado = nombre.strip().upper()

    try:
        with open(archivo_equipo, 'r') as archivo:
            for linea in archivo:
                jugador_lista = linea.strip().upper()
                if jugador_lista == nombre_buscado:
                    return True

            return False

    except FileNotFoundError:
        return 'El archivo del equipo no existe'
    



resultado1 = buscar_jugador('  Anthony Davis  ')
print(f"¿Anthony Davis está en el equipo?: {resultado1}")


resultado2 = buscar_jugador('Stephen Curry')
print(f"¿Stephen Curry está en los Lakers?: {resultado2}")


resultado3 = buscar_jugador('LeBron James', archivo_equipo='archivo_fantasma.txt')
print(resultado3)