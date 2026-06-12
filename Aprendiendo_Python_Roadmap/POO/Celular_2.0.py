class Celular:
    def __init__(self, modelo, __bateria):
            self.modelo = modelo
            self.__bateria = __bateria

    @property
    def bateria(self):
          return self.__bateria
    
    @bateria.setter
    def bateria(self, cantidad_cargar):
        self.__bateria += cantidad_cargar

        if self.__bateria > 100:
            self.__bateria = 100
            print("¡Batería completamente llena! (100%)")
        else:
            print(f"Cargando... Batería actual: {self.__bateria}%")

        
# creamos objeto 
cel_1 = Celular('Iphone', 80)

print(f"Bateria inicial del telefono {cel_1.modelo}: {cel_1.bateria}%")

cel_1.bateria = 90

print(f"Nueva bateria del telefono {cel_1.modelo}: {cel_1.bateria}%")