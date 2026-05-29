# Torneo de Pro players
# Lista
inscritos = ['Sacy', 'Aspas', 'Less']
print(f'Lista de jugadores inscritos original {inscritos}')

# Registro
inscritos.append('King')

# Posicion 1
inscritos.insert(1, 'Chronicle')

# Descalificacion
inscritos.remove('Aspas')

# Orden alfabetico
inscritos.sort()

# Mensaje final
total_jugadores = len(inscritos)
print(f'\nEl total de jugadores para competir son: {total_jugadores}')
print(f'Lista oficial de los jugadores final: {inscritos}')
