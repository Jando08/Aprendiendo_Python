import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_hardware = pd.read_csv(ruta_archivo / "hardware_sucio.csv")

print(df_hardware.isna().sum())

df_hardware["marca"] = df_hardware["marca"].fillna("Generico")
df_hardware["stock"] = df_hardware["stock"].fillna(0)
#estructura para eliminar una fila completa en de un data set
df_hardware = df_hardware.dropna(subset=["precio_usd"])

print("=== Limpiando Campo Vacios ===")
print(df_hardware)