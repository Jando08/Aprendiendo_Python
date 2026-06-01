# Crear diccionario
puntos_jugadores = {
    'Curry' : 30,
    'Lebron' : 25,
    'Tatum' : 27
}

busqueda = 'Durant'

try:
    puntos = puntos_jugadores[busqueda]
except KeyError:
    print(f'Error: El jugador {busqueda} no se encuentra en la base de datos')