"""
Define una función llamada convertir_a_dolares que reciba un parámetro llamado pesos.
Dentro de la función, calcula el equivalente en dólares. Vamos a suponer que el tipo de cambio es de 17 pesos por dólar (así que divide pesos / 17).
Usa la palabra clave return para devolver el resultado de esa división.
Fuera de la función:
Crea una variable externa llamada mis_pesos y asígnale un valor numérico entero o decimal (por ejemplo, 850).
Llama a tu función pasándole mis_pesos como argumento, y guarda el resultado que te devuelva en una variable llamada dolares_totales.
Muestra el resultado final en pantalla con un f-string limpio: "${mis_pesos} pesos equivalen a ${dolares_totales} dólares."
"""

def convertir_a_dolares(pesos):
    dolar = pesos / 17
    return dolar

mis_pesos = 17.00
dolares_totales = convertir_a_dolares(mis_pesos)

mensaje = f'Mis ${mis_pesos} pesos equivalen a ${dolares_totales} dolares'

print(mensaje)