# crear una clase llamada Persona (usando camel case)
class Persona:
    # crear el constructor del objeto
    def __init__(self, nombre, clase_rol):
        # asignar los atributos
        self.nombre = nombre
        self.clase_rol = clase_rol
        self.vida = 100

        # crear un metodo
    def recibir_danio(self, cantidad):
        self.vida -= cantidad
        print(f"{self.nombre} ha recibido {cantidad} de daño! Vida restante {self.vida}")

# crear un nuevo jugador
jugador_1 = Persona('MILAN DAKKAR POLANCO MONTES', 'FOLLA ANCIANAS')
jugador_2 = Persona('ERIC ALEXANDER CASTAÑEDA CAMPOMAS', 'DONADOR DEL CASINO')
jugador_3 = Persona('ALEJANDRO PARRA LEYVA', 'PUSSY DESTROYER')

# acceder a los atributos de los jugadores
print(f"El jugador 1 es {jugador_1.nombre} y su rol de juego es {jugador_1.clase_rol}")
print(f"El jugador 2 es {jugador_2.nombre} y su rol de juego es {jugador_2.clase_rol}")
print(f"El jugador 3 es {jugador_3.nombre} y su rol de juego es {jugador_3.clase_rol}")


# invocar el metodo recien creado
jugador_1.recibir_danio(30)
jugador_2.recibir_danio(90)
jugador_3.recibir_danio(50)



# revisar como cambio el atributo de vida de los jugadores
print(f"Puntos de vida totales del jugador 1: {jugador_1.nombre} = {jugador_1.vida} ")
print(f"Puntos de vida totales del jugador 2: {jugador_2.nombre} = {jugador_2.vida} ")
print(f"Puntos de vida totales del jugador 3: {jugador_3.nombre} = {jugador_3.vida} ")