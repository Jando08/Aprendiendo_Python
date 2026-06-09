lakers_stats = {
    "LeBron James": 28.5,
    "Anthony Davis": 24.9,
    "Austin Reaves": 15.9,
    "D'Angelo Russell": 18.0
}

for jugador in lakers_stats:

    puntos = lakers_stats[jugador]
    
    if puntos >= 25:
        print(f"{jugador} es candidato a MVP con {puntos} PPP.")
    else:
        print(f"{jugador} tiene una buena temporada ({puntos} pts), pero no le alcanza para MVP.")
