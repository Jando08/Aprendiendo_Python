class PerfilGamer:
    def __init__(self, nickname, nivel_inicial):
        self.nickname = nickname
        self.__nivel = nivel_inicial  # Atributo protegido

    # GETTER estilo Pythonic
    @property
    def nivel(self):
        return self.__nivel

    # SETTER con filtro de seguridad
    @nivel.setter
    def nivel(self, nuevo_nivel):
        # El nivel en este juego no puede ser negativo ni revocar rango
        if nuevo_nivel >= self.__nivel:
            self.__nivel = nuevo_nivel
            print(f"🎮 ¡GG! {self.nickname} subió al nivel {self.__nivel}")
        else:
            print(f"❌ Error: No puedes bajar de nivel. Nivel actual: {self.__nivel}")


# --- PRUEBAS DE LA RACHA ---
if __name__ == "__main__":
    jugador = PerfilGamer("JandoPro", 10)
    
    print(f"🕹️ Jugador: {jugador.nickname} | Nivel Inicial: {jugador.nivel}")
    
    # Intento válido de subir de nivel
    jugador.nivel = 11
    
    # Intento inválido (Hacker intentando bajar el nivel)
    jugador.nivel = 5