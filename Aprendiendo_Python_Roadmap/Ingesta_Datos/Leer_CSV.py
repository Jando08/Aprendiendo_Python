import pandas as pd
from pathlib import Path

# Ingesta segura del archivo CSV
ruta_script = Path(__file__).parent
df_empleados = pd.read_csv(ruta_script / "empleados.csv")

# Filtrado de empleados en el departamento de Data Science
mascara_ds = df_empleados["departamento"] == "Data Science"
df_data_science = df_empleados[mascara_ds]

# Cálculo de la métrica salarial
salario_promedio = df_data_science["salario"].mean()

print("=== 📊 REPORTE DE AUDITORÍA DE NÓMINA ===")
print("Personal en el área de Data Science:")
print(df_data_science[["nombre", "salario"]])
print("-" * 40)
print(f"El salario promedio del equipo es de: ${salario_promedio:,.2f} MXN")