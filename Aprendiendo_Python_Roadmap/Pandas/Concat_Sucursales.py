import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_sucursal_norte = pd.read_csv(ruta_archivo / "sucursal_norte.csv")
df_sucursal_sur = pd.read_csv(ruta_archivo / "sucursal_sur.csv")

df_sucursal_norte["sucursal"] = "Norte"
df_sucursal_sur["sucursal"] = "Sur"

df_global = pd.concat([df_sucursal_norte, df_sucursal_sur], ignore_index=True)
df_global_agrupado = df_global.groupby("sucursal")["ingreso"].sum()

print("=== Reporte de ingresos mensuales por sucursal ===")
print(df_global_agrupado)