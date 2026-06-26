import pandas as pd
from pathlib import Path

rutas_archivos = Path(__file__).parent
df_ventas_hoy = pd.read_csv(rutas_archivos / "ventas_hoy.csv")
df_inventario = pd.read_csv(rutas_archivos / "inventario.csv")

df_resultado = df_inventario.merge(df_ventas_hoy, on="id_hardware", how="left")

df_resultado["cantidad_vendida"] = df_resultado["cantidad_vendida"].fillna(0)
# para crear una nueva columna solo se crea y se le da el valor igual con el mismo dataframe
df_resultado["stock_final"] = df_resultado["stock_inicial"] - df_resultado["cantidad_vendida"]

print("=== Reporte final de las ventas del dia ===")
print(df_resultado)