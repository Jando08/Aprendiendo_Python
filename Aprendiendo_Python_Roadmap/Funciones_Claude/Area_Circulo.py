# crea las funciones area_circulo(radio) y volumen_cilindo(radio, altura)
# la segunda debe llamar a la primera internamente

import math

def area_circulo(radio):
    return math.pi * radio ** 2    

def volumen_cilindro(radio, altura):
    base = area_circulo(radio)     
    return base * altura           

print(volumen_cilindro(3, 15))   