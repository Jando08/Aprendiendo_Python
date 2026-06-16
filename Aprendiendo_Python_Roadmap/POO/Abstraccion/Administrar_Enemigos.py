from abc import ABC, abstractmethod

class Enemigo(ABC):
    def __init__(self, monstruo):
        self.monstruo = monstruo

    
    @abstractmethod
    def atacar(self):
        pass

class Zombie(Enemigo):
    def __init__(self, monstruo):
        super().__init__(monstruo)

    def atacar(self):
        print(f"{self.monstruo} camina lento y te muerde el brazo! DMG: 15")


class Dragon(Enemigo):
    def __init__(self, monstruo, elemento):
        super().__init__(monstruo)
        self.elemento = elemento

    
    def atacar(self):
        print(f"{self.monstruo} vuela alto y lanza un soplo de {self.elemento}! DMG: 80")


if __name__ == "__main__":

    #creando los monstruos
    monstruo_1 = Zombie("Messi")
    monstruo_2 = Dragon("Chimuelo", "Plasma")

    horda_enemigos = [monstruo_1, monstruo_2]

    for enemigo in horda_enemigos:
        enemigo.atacar()
