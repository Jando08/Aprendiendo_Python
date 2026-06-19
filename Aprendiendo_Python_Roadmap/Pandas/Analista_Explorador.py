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

# head sirve para indicar cuandas filas queremos imprimir de nuestra tabla
print(df.head(2))

# shape nos indica cuantas filas y columnas tenemos en la tabla
print(df.shape)

# info() muestra el tipo de datos que tenemos guardados en la tabla
df.info()