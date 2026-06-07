# Crea una funcion estadisticas(numeros) que reciba 
# una lista y retorne de una sola vez, el minimo, 
# el maximo y el promedio

def estadisticas(numeros):
    minimo = min(numeros)
    maximo = max(numeros)
    promedio = sum(numeros) / len(numeros)

    return minimo, maximo, promedio


minimo, maximo, promedio = estadisticas([4, 8, 2, 10, 6])

print(minimo)
print(maximo)
print(promedio)