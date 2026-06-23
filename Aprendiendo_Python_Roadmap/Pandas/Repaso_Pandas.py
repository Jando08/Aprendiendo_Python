import pandas as pd
from pathlib import Path

ruta_script = Path(__file__).parent
df_canciones = pd.read_csv(ruta_script / "top_canciones.csv")

mascara_temazos = df_canciones["reproducciones"] > 100
df_vips = df_canciones[mascara_temazos]

duracion_promedio = df_vips["duracion_min"].mean()

print("=== Reporte de Canciones más Reproducidas ===")
print(f"El numero de canciones que pasaron el filtro de Temazos fueron: {df_vips.shape[0]} \n")
print(f"Las canciones y las reproducciones son: \n {df_vips[["cancion", "reproducciones"]]}")
print(f"El promedio de duracion de la playlist es: {duracion_promedio:,.2f} min")