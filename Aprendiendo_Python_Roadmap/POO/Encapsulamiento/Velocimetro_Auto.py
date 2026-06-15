class Auto:
    def __init__(self, marca, velocidad_inicial):
        self.marca = marca
        self.__velocidad = velocidad_inicial

    # ---GETTER---
    @property
    def velocidad(self):
        return self.__velocidad
    

    # ---SETTER---
    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        if nueva_velocidad >= 0 and nueva_velocidad <= 280:
            self.__velocidad = nueva_velocidad
            print(f"Acelerando... Velocidad actual: {self.__velocidad} km/h")
        else:
            print(f"ERROR! la velocidad ingresada debe estar en el rango de (0-280)")



# 1. Creamos el carro
mi_nave = Auto("Nissan GTR", 0)

# 2. Leemos velocidad inicial usando la propiedad
print(f"El {mi_nave.marca} arranca a: {mi_nave.velocidad} km/h")

# 3. Le pisamos al acelerador (Valor válido)
mi_nave.velocidad = 120
print(f"Velocidad actual: {mi_nave.velocidad} km/h")

# 4. Intentamos meter reversa cuántica o romper la barrera del sonido (Valores inválidos)
mi_nave.velocidad = -20
mi_nave.velocidad = 500


