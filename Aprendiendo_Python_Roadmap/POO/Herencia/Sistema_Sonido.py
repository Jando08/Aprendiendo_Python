class Sonido:
    def __init__(self, archivo, volumen_inicial):
        self.archivo = archivo
        self.__volumen = volumen_inicial
    
    # metodo getter
    @property
    def volumen(self):
        return self.__volumen
    
    # metodo setter
    @volumen.setter
    # validar que el volumen este entre 0 y 100
    def volumen(self, nuevo_volumen):
        if nuevo_volumen >= 0 and nuevo_volumen <= 100:
            self.__volumen = nuevo_volumen
        else:
            print("Ingrese un numero de volumen entre (0-100)")

    
    def reproducir(self):
        print(f"Reproduciendo {self.archivo} a un volumen de {self.volumen}%")

    


class SonidoRetro(Sonido):
    def __init__(self, archivo, volumen_inicial, bits):
        super().__init__(archivo, volumen_inicial)

        # pertenece a la clase hija
        self.bits = bits

    def reproducir(self):
        super().reproducir()
        print(f"Aplicando filtro retro de {self.bits} bits")


# creamos sonidos
sonido_normal = Sonido('despacito.mp3', 40)
sonido_retro = SonidoRetro('ramdom.wav', 70, 6)

# probar el sonido normal
sonido_normal.reproducir()

# probar sonido retro
sonido_retro.reproducir()

# probar modificar el volumen usando la @property 
sonido_retro.volumen = 95
print(f"El nuevo volumen del efecto retro es: {sonido_retro.volumen}%")