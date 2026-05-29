"""
Define una función llamada calcular_puntos_totales que reciba dos parámetros: 
dobles (cantidad de canastas de 2 puntos) y triples (cantidad de canastas de 3 puntos).
Dentro de la función:
Calcula los puntos de los dobles multiplicando dobles * 2.
Calcula los puntos de los triples multiplicando triples * 3.
Suma ambos resultados para obtener el total y guárdalo en una variable llamada puntos_finales.
Usa return para devolver el valor de puntos_finales.
Fuera de la función (Código principal):
Pídele al usuario cuántos tiros de 2 puntos metió el jugador usando int(input("Canastas de 2 puntos: ")). Guarda esto en una variable llamada tiros_dobles.
Pídele al usuario cuántos tiros de 3 puntos metió usando int(input("Canastas de 3 puntos: ")). Guarda esto en una variable llamada tiros_triples.
Llama a tu función pasándole tus dos variables como argumentos: calcular_puntos_totales(tiros_dobles, tiros_triples).
Guarda lo que te devuelva la función en una variable llamada marcador_final.
Imprime el resultado con un f-string: "El jugador anotó un total de {marcador_final} puntos en el partido."
"""

nombre = input('Ingresa tu nombre: ')

def calcular_puntos_totales(dobles, triples):
    dobles *= 2
    triples *= 3
    
    # Suma de puntos
    puntos_finales = dobles + triples
    # Devolver los puntos totales
    return puntos_finales


# Registro de puntos
tiros_dobles = int(input('Canastas de 2 puntos: '))
tiros_triples = int(input('Canastas de 3 puntos: '))

# Llamando a la funcion
marcador_final = calcular_puntos_totales(tiros_dobles, tiros_triples)

# Mensaje final
mensaje_resultado = f'El jugador {nombre} anotó un total de {marcador_final} puntos en el partido.'

print(mensaje_resultado)