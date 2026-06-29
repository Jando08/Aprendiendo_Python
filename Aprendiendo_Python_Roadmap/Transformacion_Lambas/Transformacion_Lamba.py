import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_nba = pd.read_csv(ruta_archivo / "nba_transformacion.csv")

# limpiar espacios en blanco
df_nba["jugador"] = df_nba["jugador"].str.strip()

# primera letra mayuscula
df_nba["jugador"] = df_nba["jugador"].str.title()

# agregar una nueva columna
df_nba["categoria"] = df_nba["puntos_por_partido"].apply(lambda x: "Elite Scorer" if x >= 20 else "Role Player")

print("=== Formato Limpio Estadisticas NBA ===")
print(df_nba)