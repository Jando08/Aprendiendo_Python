# importar la libreria 
import numpy as np

# crear la lista
presupuesto_dolares = [150, 500, 1200, 3000]

# convertir esta lista a un arregle de NumPy
precios_numpy = np.array(presupuesto_dolares)

# mostrar valores del array original
print(f"Arreglo original {precios_numpy}")

# multiplicar valores del array por 18
presupuesto_pesos = precios_numpy * 18

# imprimir precios ya convertidos a pesos mexicanos
print(f"Arreglo con pesos mexicanos {presupuesto_pesos}")