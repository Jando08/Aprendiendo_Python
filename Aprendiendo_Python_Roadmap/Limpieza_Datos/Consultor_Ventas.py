import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_ventas_sucio = pd.read_csv(ruta_archivo / "ventas_sucias.csv")

df_ventas_sucio.isna().sum()

df_ventas_sucio["cantidad"] = df_ventas_sucio["cantidad"].fillna(1)

df_ventas_limpio = df_ventas_sucio.dropna().copy()


df_ventas_limpio["total_venta"] = df_ventas_limpio["cantidad"] * df_ventas_limpio["precio_unitario"]
total_venta = df_ventas_limpio["total_venta"].sum()
print("=== REPORTE FINAL DE VENTAS DE COPPEL")
print(df_ventas_limpio)
print("_" * 80)
print(f"El dinero total recaudado por las ventas fue un total de: ${total_venta:,.2f} MXN")


# Apilado vertical (uno abajo del otro)
df_total = pd.concat([df_enero, df_febrero], ignore_index=True)

