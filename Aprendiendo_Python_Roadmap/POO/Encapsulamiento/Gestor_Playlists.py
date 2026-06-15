class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

class Playlist:
    def __init__(self, nombre_playlist):
        self.nombre_playlist = nombre_playlist
        self.lista_canciones = []

    def agregar_cancion(self, objeto_cancion):
        self.lista_canciones.append(objeto_cancion)
        print(f"Ha sido agregada la cancion {objeto_cancion.titulo} del artista {objeto_cancion.artista}")

    def mostrar_playlist(self):
        for cancion in self.lista_canciones:
            print(f" {cancion.titulo} - {cancion.artista}")


# creamos las canciones
cancion_1 = Cancion('Devil in a New Dress', 'Kanye West')
cancion_2 = Cancion('Nikes', 'Frank Ocean')
cancion_3 = Cancion('Osos Maduros', 'Mi mochila huele a semen')
cancion_4 = Cancion('La La La', 'Shakira')

# creamos la playlis
reproductor = Playlist('Playlista locochona asi como yo')

# hacemos funcionar las funciones con los objetos
reproductor.agregar_cancion(cancion_1)
reproductor.agregar_cancion(cancion_2)
reproductor.agregar_cancion(cancion_3)
reproductor.agregar_cancion(cancion_4)

# imprimir el resultado final
reproductor.mostrar_playlist()
