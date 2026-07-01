import pandas as pd
from pathlib import Path

ruta_archivo = Path(__file__).parent
df_posiciones = pd.read_csv(ruta_archivo / "nba_posiciones.csv")


# el agg en los dataframe se usa para calcular el valor que deseamos de
# varias columnas a la vez
df_reporte = df_posiciones.groupby("posicion", as_index=False).agg({
    "puntos" : ["mean"],
    "asistencias" : ["sum"],
    "jugador" : ["count"]
})

print("=== Reporte Final Stats del equipo Knicks ===")
print(df_reporte)