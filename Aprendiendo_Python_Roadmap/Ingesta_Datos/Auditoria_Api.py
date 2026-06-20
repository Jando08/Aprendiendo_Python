import pandas as pd
from pathlib import Path

# Ingesta segura del archivo CSV
ruta_script = Path(__file__).parent
df_logs = pd.read_csv(ruta_script / "logs_api.csv")

# filtro de velocidad de las peticiones
mascara_peticiones = df_logs["tiempo_ms"] > 400
df_lentas = df_logs[mascara_peticiones]

# tiempo promedio de cada peticion lenta
prom_peticiones = df_lentas["tiempo_ms"].mean()

print("=== REPORTE DE PETICIONES LENTAS ===")
print(f"Se detectaron {df_lentas.shape[0]} peticiones que superan los 400ms:\n")
print(df_lentas[["endpoint", "tiempo_ms"]])
print(f"El tiempo promedio de retraso es de: {prom_peticiones:,.2f} ms")