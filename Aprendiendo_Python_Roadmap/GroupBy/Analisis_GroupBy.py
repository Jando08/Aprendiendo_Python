import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_inventario = pd.read_csv(ruta_archivo / "inventario_completo.csv")

# agrugar grupos por campo "marca"
df_reporte = df_inventario.groupby("marca", as_index=False)["precio_usd"].sum().sort_values(by="precio_usd", ascending=False)

print(df_reporte)