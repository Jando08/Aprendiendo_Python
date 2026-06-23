import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_productos = pd.read_csv(ruta_archivo / "ventas_tecnologia.csv")

df_resumen = df_productos.groupby("categoria")[["cantidad", "ingreso"]].sum()

print("=== REPORTE DE RESUMEN FINAL CATEGORIAS ===")
print(df_resumen)