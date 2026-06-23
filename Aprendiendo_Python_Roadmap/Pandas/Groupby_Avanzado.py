import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_salarios = pd.read_csv(ruta_archivo / "nba_salarios.csv")


df_resumen = df_salarios.groupby("conferencia").agg({
    'puntos_por_partido' : "mean",
    'salario_millones' : "sum"
}).reset_index()

print("=== REPORTE DE SALARIOS Y PUNTOS POR PARTIDO DE CADA CONFERENCIA ===")
print(df_resumen)