class Celular:
    def __init__(self, modelo, porcentaje_bateria):
        self.modelo = modelo
        self.__porcentaje_bateria = porcentaje_bateria  

    # método GETTER
    def ver_bateria(self):
        return self.__porcentaje_bateria
    
    # método SETTER 
    def cargar_bateria(self, cantidad):
        self.__porcentaje_bateria += cantidad
        
        # Validamos si el TOTAL se pasó del límite físico de la batería
        if self.__porcentaje_bateria > 100:
            self.__porcentaje_bateria = 100
            print("¡Batería completamente llena! (100%)")
        else:
            print(f"Cargando... Batería actual: {self.__porcentaje_bateria}%")


telefono = Celular("HP Omen Phone", 40)

# Intentamos ver la batería usando el método seguro
print(f"Batería inicial: {telefono.ver_bateria()}%")

# Le metemos una carga normal de 30% (Debería subir a 70%)
telefono.cargar_bateria(30)

# Intentamos meterle una carga exagerada de 80% (Debería topar en 100)
telefono.cargar_bateria(80)

# Verificamos el estado final seguro
print(f"Batería final: {telefono.ver_bateria()}%")