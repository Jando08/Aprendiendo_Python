# Clase padre
class Dispositivo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
    def encender(self):
        print(f"El dispositivo {self.marca} {self.modelo} esta encendido")


# clase hija
class Laptop(Dispositivo):
    def __init__(self, marca, modelo, ram):
        super().__init__(marca, modelo)  
        self.ram = ram

    
    def programar(self):
        print(f"Programando en la laptop de {self.ram} GB de RAM")



# creando objetos
laptop_1 = Laptop('MSI', 'Cyborg 15', 8)
laptop_2 = Laptop('HP', 'Omen Trascend', 32)
laptop_3 = Laptop('Apple', 'Macbook Pro', 16)


# probando las laptops
print("--- Probando Laptop 1 ---")
laptop_1.encender()   
laptop_1.programar()  

print("--- Probando Laptop 2 ---")
laptop_2.encender()   
laptop_2.programar()  

print("--- Probando Laptop 3 ---")
laptop_3.encender()   
laptop_3.programar()  