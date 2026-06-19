# La regla de oro en Ciencia de Datos: NumPy SIEMPRE se importa con el alias 'np'
import numpy as np

# 1. Creamos una lista de precios normal de Python
precios_lista = [100, 250, 400, 800]

# 2. Convertimos esa lista en un Arreglo de NumPy (esto en matemáticas se llama Vector)
precios_numpy = np.array(precios_lista)

print("=== 📊 PROBANDO EL PODER DE NUMPY ===")
print(f"Arreglo original: {precios_numpy}")

# 3. LA MAGIA: Queremos aplicar un descuento del 10% a todos los productos.
# Multiplicamos TODO el bloque por 0.90 de un solo golpe. ¡Sin usar ciclos for!
precios_con_descuento = precios_numpy * 0.90

print(f"Precios con descuento: {precios_con_descuento}")