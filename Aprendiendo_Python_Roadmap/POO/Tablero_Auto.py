# crear la clase
class Auto:
    # agregar atributos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_actual = 0

    # metodo para aumentar la velocidad
    def acelerar(self, incremento):
        self.velocidad_actual += incremento
        print(f"La velocidad actual del coche {self.marca} es: {self.velocidad_actual} KH")

    # metodo para disminuir la velocidad
    def frenar(self, decremento):
        if decremento < 0:
            print("El decremento no puede ser negativo.")
        else:
            #Todo esto pasa si el decremento es correcto
            self.velocidad_actual -= decremento
            
            # Si se pasó de frenado, lo clavamos en 0
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
            
            # Este print ahora sí se ejecuta SIEMPRE que el auto frene bien
            print(f"El auto {self.marca} ha frenado {decremento} KH. Velocidad actual: {self.velocidad_actual} KH")


# crear objetos
carro_1 = Auto('BMW', 'X5')
carro_2 = Auto('Toyota', 'Camry')
carro_3 = Auto('Honda', 'Civic')
carro_4 = Auto('Ford', 'F-150')
carro_5 = Auto('Chevrolet', 'Camaro')

# probar los metodos
# carro 1
carro_1.acelerar(100)
carro_1.frenar(30)
# carro 2
carro_2.acelerar(80)
carro_2.frenar(30)
# carro 3
carro_3.acelerar(60)
carro_3.frenar(10)
# carro 4
carro_4.acelerar(100)
carro_4.frenar(20)
# carro 5
carro_5.acelerar(120)
carro_5.frenar(50)
