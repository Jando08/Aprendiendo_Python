# Lista de puntos
puntos_partidos = [25, 32, 18, 40, 30, 12]

partizados_totales = 0

for puntos in puntos_partidos:
    if puntos >= 30:
        print(f'1Partizado! El jugador anoto {puntos} puntos en el partido')
        partizados_totales += 1


print(f'Total de partizados: {partizados_totales}')

