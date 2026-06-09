perfil_jugador = {
    'nombre' : 'Austin Reaves',
    'numero' : 15,
    'ultimos_partidos' : [12, 15, 18]
}

total_puntos = sum(perfil_jugador['ultimos_partidos'])

print(f'El total de los puntos de {perfil_jugador['nombre']} en los 3 ultimos partidos fueron: {total_puntos}')