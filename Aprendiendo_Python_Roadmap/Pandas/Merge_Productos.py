import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_productos = pd.read_csv(ruta_archivo / "productos.csv")
df_pedidos = pd.read_csv(ruta_archivo / "pedidos.csv")

df_resultado = df_productos.merge(df_pedidos, on="id_producto", how="inner")

print("=== Resultado de unir archivos CSV ===")
print(df_resultado)
