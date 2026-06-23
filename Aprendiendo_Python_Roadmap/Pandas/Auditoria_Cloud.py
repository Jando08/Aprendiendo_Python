import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_logs = pd.read_csv(ruta_archivo / "logs_servidores.csv")

df_resumen = df_logs.groupby("entorno").agg({
    "uso_ram_gb" : "max",
    "costo_por_hora" : "sum"
}).reset_index().sort_values(by="costo_por_hora", ascending=False)

print("=== REPORTE FINAL DE RECURSOS GASTADOS POR ENTORNOS ===")
print(df_resumen)