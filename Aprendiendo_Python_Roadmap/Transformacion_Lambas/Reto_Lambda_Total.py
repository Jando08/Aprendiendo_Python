import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_importaciones = pd.read_csv(ruta_archivo / "importaciones_raw.csv")

# limpiar espacios en blanco
df_importaciones["componente"] = df_importaciones["componente"].str.strip()
# primera letra en mayuscula
df_importaciones["componente"] = df_importaciones["componente"].str.title()
# convertir a usd
df_importaciones["precio_usd"] = df_importaciones["precio_mxn"].apply(lambda x: round(x / 20.0, 2))
# clasificar productos
df_importaciones["tipo_arancel"] = df_importaciones["precio_usd"].apply(lambda x: "Alto Valor" if x > 250 else "Estandar")

#impresion final
print("=== Reporte Final Precio de Importaciones ===")
print(df_importaciones)