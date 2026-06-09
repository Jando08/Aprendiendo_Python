def calcular_cuenta(precio_comida, num_personas, propina):
    propina_calculada = precio_comida * propina / 100
    precio = precio_comida + propina_calculada
    precio_final = precio / num_personas
    return precio_final

print(calcular_cuenta(600, 4, 10))   
print(calcular_cuenta(1000, 5, 15))  
print(calcular_cuenta(400, 2, 20))   