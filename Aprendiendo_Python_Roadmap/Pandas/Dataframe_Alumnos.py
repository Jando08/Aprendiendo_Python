# importar la libreria de pandas
import pandas as pd

# crear diccionario
alumnos = {
    "Nombre" : ["Alejandro", "Erick", "Milan"],
    "Materia" : ["Data Science", "Linux", "Mecatronica"],
    "Calificacion" : [100, 70, 100]
}

# convertir diccionario a dataframe
df = pd.DataFrame(alumnos)

# imprimir el diccionario
print(df)