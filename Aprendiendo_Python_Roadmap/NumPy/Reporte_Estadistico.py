# importar libreria
import numpy as np

# crear arreglo tipo numpy
gastos_clientes = np.array([1200, 4500, 800, 15000, 3200])

# imprimir el gasto total de todos los clientes combinados
gasto_total = np.sum(gastos_clientes)

# imprimir el gasto en promedio de la tienda
gasto_promedio = np.mean(gastos_clientes)

# imprimir el gasto mas alto registrado en la tienda
gasto_maximo = np.max(gastos_clientes)

# imprimir los valores de la tienda
print("=== TIENDA: FERRETERIA LA HORMIGA ===")
print(f"La suma totalde los gastos de la tienda fue un total de: ${gasto_total}")
print(f"El promedio total de los gastos de la tienda fue un total de: ${gasto_promedio}")
print(f"La compra maxima de la tienda fue de un total de: ${gasto_maximo}")

