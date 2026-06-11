# crear la clase
class Partido:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = 0
        self.goles_visitante = 0

    def anotar_gol(self, equipo):
        if self.equipo_local == equipo:
            self.goles_local += 1
        elif self.equipo_visitante == equipo:
            self.goles_visitante += 1
        else:
            print("Ese nombre de equipo no esta inscrito en el torneo")
        
    def mostrar_marcador(self):
        print(f'Marcador en vivo: {self.equipo_local} {self.goles_local} - {self.equipo_visitante} {self.goles_visitante}')


# 1. Creamos el partido de hoy
partido_hoy = Partido("Mexico", "Sudafrica")

# 2. Empieza la acción (Prueba los métodos)
partido_hoy.anotar_gol("Mexico")
partido_hoy.anotar_gol("Mexico")
partido_hoy.anotar_gol("Sudafrica")

# 3. Verificamos el tablero antes de que sople el silbatazo final
partido_hoy.mostrar_marcador()