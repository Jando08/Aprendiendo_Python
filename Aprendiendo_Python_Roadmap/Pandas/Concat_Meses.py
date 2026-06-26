import pandas as pd
from pathlib import Path

ruta_archivos = Path(__file__).parent
df_ventas_enero = pd.read_csv(ruta_archivos / "ventas_enero.csv")
df_ventas_febrero = pd.read_csv(ruta_archivos / "ventas_febrero.csv")


df_ventas_enero["mes"] = "Enero"
df_ventas_febrero["mes"] = "Febrero"

df_anual = pd.concat([df_ventas_enero, df_ventas_febrero], ignore_index=True)
df_anual_agrupado = df_anual.groupby("producto")["unidades"].sum()

print("=== Impresion de las ventas ordenadas por meses ===")
print(df_anual)
print("\n")
print("=== Ventas totales sumadas de los meses Enero y Febrero")
print(df_anual_agrupado)