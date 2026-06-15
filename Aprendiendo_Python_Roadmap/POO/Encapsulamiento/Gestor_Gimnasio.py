class Socio:
    def __init__(self, nombre, mensualidad_inicial):
        self.nombre = nombre
        self.__mensualidad = mensualidad_inicial

    # metodo GETTER
    @property
    def mensualidad(self):
        return self.__mensualidad
    
    # metodo SETTER
    @mensualidad.setter
    def mensualidad(self, nueva_mensualidad):
        if nueva_mensualidad >= 0:
            self.__mensualidad = nueva_mensualidad
            print(f"Mensualidad de {self.nombre} actualizada a: ${nueva_mensualidad}")
        else:
            print(f"ERROR: ${nueva_mensualidad} no es una mensualidad valida")


class Gimnasio:
    def __init__(self, nombre_gym):
        self.nombre_gym = nombre_gym
        self.__lista_socios = []
    
    def registrar_socio(self, nuevo_socio):
        self.__lista_socios.append(nuevo_socio)

    # metodo GETTER
    @property
    def ingresos_totales(self):
        suma_ingresos = 0

        for socio in self.__lista_socios:
            suma_ingresos += socio.mensualidad

        return suma_ingresos


# creamos los socios con sus mensualidades base
socio_1 = Socio("Alejandro", 450)
socio_2 = Socio("Carlos", 500)
socio_3 = Socio("Mariana", 400)

# creamos el gimnasio
Gym = Gimnasio("Iron Paradise Gym")

# registramos a los socios en el gimnasio
Gym.registrar_socio(socio_1)
Gym.registrar_socio(socio_2)
Gym.registrar_socio(socio_3)

# probamos el GETTER calculado (450 + 500 + 400 = 1350)
print(f"💵 Ingresos totales del gym: ${Gym.ingresos_totales}")

# intentamos meter un hackeo de mensualidad gratis al primer socio
socio_1.mensualidad = -100

# verificamos que la caja del gimnasio siga intacta y segura
print(f"🛡️ Ingresos totales tras intento de fraude: ${Gym.ingresos_totales}")