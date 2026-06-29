import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_presupuesto_hardware = pd.read_csv(ruta_archivo / "presupuesto_hardware.csv")

df_presupuesto_hardware["precio_usd"] = df_presupuesto_hardware["precio_mxn"].apply(lambda x: round(x / 20.0, 2))

df_presupuesto_hardware["requiere_aprobacion"] = df_presupuesto_hardware["precio_usd"].apply(lambda x: "SI" if x > 500 else "NO")

print("=== Presupuesto Final Hardware ===")
print(df_presupuesto_hardware)