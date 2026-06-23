import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_inventario = pd.read_csv(ruta_archivo / "inventario_sucio.csv")

# numero de numeros por cada columna = .isna().sum()
print(df_inventario.isna().sum())

# rellenar campos vacios = df["campo"] = df["campo"].fillna(valor)
df_inventario["precio"] = df_inventario["precio"].fillna(0)

# eliminar campos que sigan teniendo valores nulos .dropna()
df_limpio = df_inventario.dropna()

print(df_limpio)