# ⚡ Transformación de Datos: Columnas Avanzadas con `.apply()` y Lambda

En Pandas, cuando las operaciones matemáticas simples no son suficientes para transformar los datos de una columna, utilizamos el método `.apply()`. Al combinarlo con funciones **Lambda** (funciones anónimas en una sola línea), podemos manipular strings o aplicar condicionales fila por fila de forma masiva.

## 🛠️ Herramientas Clave

### 1. Métodos de Strings en Pandas (`.str`)
Para modificar texto en una columna, se debe usar el accesor `.str` antes del método de Python convencional:
* `df["columna"].str.upper()` -> Convierte todo a MAYÚSCULAS.
* `df["columna"].str.lower()` -> Convierte todo a minúsculas.
* `df["columna"].str.replace("a", "b")` -> Reemplaza texto.

### 2. El Súper Poder de `.apply()` y Lambda
Una función lambda es una función abreviada sin nombre que se escribe en una sola línea. Su sintaxis dentro de Pandas es:
`df["nueva_columna"] = df["columna_origen"].apply(lambda x: operacion_con_x)`

Donde `x` representa el valor de la celda fila por fila.

### 3. Condicionales (`if-else`) dentro de un Lambda
Podemos estructurar un `if/else` en una sola línea de la siguiente forma:
`lambda x: "Valor_Si_Verdadero" if x > 10 else "Valor_Si_Falso"`


### ➕ Agregar una Fila Nueva Entera
Para meter un registro nuevo hasta el fondo de la tabla:
1. Crear un diccionario con los datos: `datos = {"col1": [val1], "col2": [val2]}`
2. Convertirlo a DataFrame: `df_fila = pd.DataFrame(datos)`
3. Concatenar: `df = pd.concat([df, df_fila], ignore_index=True)`