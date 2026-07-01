import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_ventas = pd.read_csv(ruta_archivo / "ventas_bunker.csv")

df_ventas_agrupado = df_ventas.groupby("marca", as_index=False).agg({
    "precio_usd" : ["sum", "mean"],
    "componente" : ["count"]
})

df_ventas_agrupado = df_ventas_agrupado.sort_values(by=("precio_usd", "sum"), ascending=False)

print("=== Reporte Final de Ventas del Bunker ===")
print("=== Mayor a Menor en ganancias ===")
print(df_ventas_agrupado)