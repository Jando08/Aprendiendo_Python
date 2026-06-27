import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_estadisticas_nba = pd.read_csv(ruta_archivo / "nba_sucio.csv")

# conteo de los campos nulos por columna
print(df_estadisticas_nba.isnull().sum())

# corregir partidos jugados
promedio_partidos_jugados = df_estadisticas_nba["partidos_jugados"].mean()
df_estadisticas_nba["partidos_jugados"] = df_estadisticas_nba["partidos_jugados"].fillna(promedio_partidos_jugados)


df_estadisticas_nba["equipo"] = df_estadisticas_nba["equipo"].fillna("Sin Equipo")
df_estadisticas_nba = df_estadisticas_nba.dropna(subset=["salario_millones"])

print("=== Reporte de Estadisticas sobre los Jugadores ===")
print(df_estadisticas_nba)