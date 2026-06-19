import pandas as pd

# Datos de la muestra de alumnos
alumnos = {
    "Nombre":["Alejandro", "Erick", "Milan"],
    "Materia":["Data Science", "Linux", "Mecatronica"],
    "Calificacion":[100, 70, 100]
}

df_alumnos = pd.DataFrame(alumnos)

# Filtramos alumnos con nota mayor o igual a 70 (Calificación aprobatoria)
mascara_aprobados = df_alumnos["Calificacion"] >= 70
df_aprobados = df_alumnos[mascara_aprobados]

print("=== ALUMNOS APROBADOS ===")
print(df_aprobados["Nombre"])