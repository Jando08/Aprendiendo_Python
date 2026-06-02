premios = ["Novato del Año", "All-Star MVP", "MVP de la Temporada", "MVP de las Finales"]

año_a_buscar = 2  

try:
    premio_ganado = premios[año_a_buscar]
    print(f"En el año {año_a_buscar} el jugador ganó: {premio_ganado}")

except IndexError:
    print("Ese año todavía no se ha jugado o el jugador no ganó ningún premio.")

print("Proceso de consulta terminado.")

print('xdddddddddd')

