# importar libreria
import numpy as np

# arreglo para guardar los consumos
consumo_bruto = np.array([120, 450, 80, 600, 310, 520])

# calcular el valor total de cada valor bruto
costos_pesos = consumo_bruto * 3

# mascara 
mascara = costos_pesos > 1000

# si gastan mas de 1000 pesos son gastos criticos
gastos_criticos = costos_pesos[mascara]

# calcular el costo total y promedio de luz
costo_luz = np.sum(costos_pesos)
costo_promedio = np.mean(costos_pesos)

# imprimr valores finales
print("=== Reporte de Auditoria Energetica ===")
print(f"Costo en pesos de cada servidor: {costos_pesos}")
print(f"Servidores con gasto critico (Mas de $1000.00 pesos): {gastos_criticos}")

print("=== Metricas Globales ===")
print(f"El gasto total de la empresa en luz fue igual a: ${costo_luz}")
print(f"El coste promedio de luz de la empresa fue igual a: ${costo_promedio}")