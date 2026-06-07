# Crea una funcion mayor(numeros) que reciba una lista
# y retorne el numero mas grande, sin usar la funcion max()

def mayor(numeros):
    mayor_ahora = numeros[0]

    for numero in numeros:
        if numero > mayor_ahora:
            mayor_ahora = numero

    return mayor_ahora


print(mayor([8, 13, 24, 9, 15]))
print(mayor([30, 100, 200]))
