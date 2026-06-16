from abc import ABC, abstractmethod


class Consola(ABC):

    @abstractmethod
    def encender_consola(self):
        pass



class NintendoSwitch(Consola):
    def __init__(self, nombre_usuario):
        self.nombre = nombre_usuario

    def encender_consola(self):
        print(f"Nintendo Switch de {self.nombre} encendida. ¡Cargando interfaz!")



class PlayStation5(Consola):
    def __init__(self, nombre_usuario):
        self.nombre = nombre_usuario

    
    def encender_consola(self):
        print(f"PlayStation 5 de {self.nombre} encendida. Mostrando pantalla de inicio de PSN...")

if __name__ == "__main__":
    
    
    switch_jando = NintendoSwitch("Jando")
    ps5_jando = PlayStation5("Alejandro")

    
    mis_consolas = [switch_jando, ps5_jando]

    print("===  ENCENDIENDO EL SET DE JUEGOS ===")
    
    
    for consola in mis_consolas:
        consola.encender_consola()  