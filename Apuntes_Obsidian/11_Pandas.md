# 🐼 Introducción a Pandas

Pandas es la librería reina en la Ciencia de Datos para la **manipulación y análisis de datos**. Está construida sobre NumPy, lo que significa que hereda toda su velocidad matemática, pero añade etiquetas (nombres) a las filas y columnas.

En lugar de ver datos como vectores planos, con Pandas los vemos como **tablas interactivas**.

## 🏗️ Las 2 Estructuras de Datos Principales

Pandas se divide principalmente en dos componentes que debes dominar:

### 1. Series (1 Dimensión)

Es el equivalente a una sola **columna** de una tabla. Es un arreglo unidimensional donde cada elemento tiene una etiqueta llamada **Índice (Index)**.

### 2. DataFrame (2 Dimensiones)

Es el equivalente a una **tabla completa** (como una hoja de Excel o una tabla de PostgreSQL). Es una colección de Series que comparten el mismo índice.


## 🛠️ Comandos Esenciales de Ingesta

Para crear o cargar datos en Pandas, usamos los siguientes métodos:

- `pd.DataFrame(diccionario)`: Convierte un diccionario de Python en una tabla estructurada.
    
- `pd.read_csv('archivo.csv')`: El pan de cada día; lee un archivo CSV y lo convierte en DataFrame automáticamente.
    
- `pd.read_sql('SELECT * FROM tabla', conexion)`: Conecta Pandas directo con bases de datos como PostgreSQL.
    

## 🔥 ¿Por qué lo usa un Data Scientist? (Ventajas clave)

1. **Manejo de datos faltantes:** Detecta y limpia valores nulos (`NaN`) con una sola línea de código.
    
2. **Alineación inteligente:** Une, fusiona (`merge`) y concatena tablas usando llaves primarias o índices, igual que los `JOIN` de SQL.
    
3. **Filtros potentes:** Permite hacer segmentación de datos masivos en microsegundos.


## 📈 Siguiente Paso con Pandas: Inspección Básica 

Cuando trabajas con DataFrames reales, las tablas no tienen 3 filas, ¡tienen 5 millones! No puedes imprimirlas completas porque saturarías tu terminal. Por eso, un Data Scientist usa comandos de **inspección**.

Abre tu nota en Obsidian y agrega estos tres comandos que son obligatorios:

- `df.head(n)` -> Muestra solo las primeras `n` filas de la tabla (si no le pones número, por defecto te muestra 5). Es el comando más usado para "asomarse" a ver los datos.
    
- `df.shape` -> Te dice el tamaño exacto de tu tabla en formato `(filas, columnas)`. Ojo: no lleva paréntesis al final porque es un atributo, no una función.
    
- `df.info()` -> Te da un resumen completo de la tabla: cuántas columnas hay, cómo se llaman, si tienen valores nulos (vacíos) y qué tipo de dato almacena cada una (`int64`, `float64` u `object` para texto).


## 📈 Siguiente Nivel con Pandas: Selección de Columnas y Filtros

Ya sabes crear la tabla y revisarla. Ahora toca aprender a **extraer información específica**.

### 1. Seleccionar una sola columna

Si solo te interesa ver las calificaciones, no necesitas toda la tabla. Puedes llamarla como si fuera una llave de diccionario:
![[Pasted image 20260619114830.png]]

### 2. Filtrar filas (Igualito que en NumPy)

¿Te acuerdas de las máscaras booleanas que dominaste ayer con NumPy? ¡En Pandas se usan exactamente igual!

Si quieres filtrar a los alumnos que sacaron una calificación perfecta (100), creas la máscara y se la pasas al DataFrame:
![[Pasted image 20260619114859.png]]


### 💡 ¿Cómo puedes mejorar siempre que me mandes código?

Me encanta que me preguntes esto, pa. En el mundo del software y la Ciencia de Datos, a esto le llamamos **Code Review** (Revisión de Código). Para que tus entregas pasen de "funcionales" a nivel "Senior", acostúmbrate a revisar estos 4 puntos antes de darles play:

#### 1. Sigue las reglas de PEP 8 (El estilo oficial de Python)

Python es muy fijado en cómo se ve el código.

- **Espacios en asignaciones:** En tu diccionario pusiste `"Nombre" : [...]` (con espacio antes y después de los dos puntos). Lo estándar y limpio en PEP 8 es **sin espacio antes** y **un espacio después**: `"Nombre": [...]`.
    
- Lo mismo con el signo de igual: `df = pd.DataFrame(alumnos)` (ahí lo hiciste perfecto, espacio antes y después).
    

#### 2. Nombres de variables ultra claros

Tu consistencia es buena, pero en proyectos grandes, si tienes muchas tablas flotando, llamarle a todo `df` se vuelve confuso. Es mejor ponerles un nombre corto pero descriptivo. Por ejemplo: `df_alumnos` o `df_filtrado`. Así, cuando lo leas tres meses después en Obsidian, sabrás exactamente qué hay dentro.

#### 3. No abuses de los comentarios obvios

Comentar tu código es excelente para aprender, pero un programador profesional solo comenta el **"¿Por qué?"** y no el **"¿Qué?"**.

- Por ejemplo: `# importar la libreria de pandas` está de más porque cualquiera que vea `import pandas` ya sabe qué estás haciendo.
    
- Deja los comentarios solo para explicar lógica compleja o reglas de negocio (ej: `# El mínimo para aprobar la materia en esta escuela es 70`).
    

#### 4. Tipado de datos preventivo (Data Science Mental)

Antes de aplicar una máscara como `>= 70`, asegúrate mentalmente o con un `df.info()` de que la columna sea numérica. Si por error en el diccionario hubieras puesto `"70"` (como texto entre comillas), tu código habría tronado feo en la terminal. Siempre valida tus tipos de datos.

## 📈 Siguiente Nivel con Pandas: Operaciones de Agregación (Agrupar Datos)

Ya que dominas la creación, inspección, filtrado y selección de columnas, estás listo para conocer el equivalente en Pandas a lo que hacíamos ayer en NumPy con `np.sum()` o `np.mean()`, pero llevado al siguiente nivel: **operaciones sobre columnas enteras**.

En Pandas, puedes aplicar funciones estadísticas directamente a una columna específica seleccionándola primero. Por ejemplo:
![[Pasted image 20260619121559.png]]

### 🧠 El método definitivo: `.describe()`

Si quieres verte como un verdadero analista Pro, en lugar de sacar la media, el máximo y el mínimo uno por uno, Pandas tiene un método mágico que te hace la estadística descriptiva completa de tus columnas numéricas con una sola línea de código:
![[Pasted image 20260619121622.png]]


### 📊 Flujo Básico de Exploración y Filtros
1. **Inspección:** `df.shape` para dimensiones y `df.info()` para tipos de datos.
2. **Selección Múltiple:** Usar doble corchete `df[["Col1", "Col2"]]`.
3. **Máscaras:** `df[df["Columna"] > X]` para aislar filas bajo una condición.
4. **Resumen Estadístico:** `df["Columna"].describe()` para obtener métricas clave automáticas.


## 📊 ¿Qué es el `groupby` y para qué sirve?

En el mundo real, los jefes o los clientes no quieren ver filas individuales; quieren ver **resúmenes ejecutivos**. Quieren respuestas a preguntas como:

- ¿Cuánto se vende _por cada categoría_ de producto?
    
- ¿Cuál es el salario promedio _por cada departamento_ de la empresa?
    
- ¿Cuántos goles se meten _por cada equipo_ de la liga?
    

Para resolver esto en Pandas de forma ultra veloz, usamos el método `.groupby()`. Este comando hace un proceso bellísimo que en Ciencia de Datos conocemos como **Split-Apply-Combine** (Dividir - Aplicar - Combinar):

1. **Split (Dividir):** Separa los datos en grupos basados en una columna (ej. agrupa por "departamento").
    
2. **Apply (Aplicar):** Ejecuta una función matemática a cada grupo por separado (ej. saca el promedio `.mean()` o suma `.sum()`).
    
3. **Combine (Combinar):** Junta los resultados de todos los grupos y te los entrega en una tabla de resumen limpia.


### 📝 Abre Obsidian: Concepto Clave de `groupby`

Es súper importante que anotes esto en tu nota de hoy (`04_groupby_y_agregaciones.md`) porque es un comportamiento de Pandas que a veces confunde a la gente:

> ⚠️ **El Índice Cambiante:** Cuando agrupas por una columna (en este caso `"categoria"`), esa columna **deja de ser una columna normal y se convierte en el nuevo Índice (Index)** de la tabla. Por eso en la terminal ves que el nombre `categoria` aparece un renglón más abajo que `cantidad` e `ingreso`.

Si más adelante quisieras resetear la tabla para que `categoria` vuelva a ser una columna común y corriente (con sus índices numéricos `0, 1, 2`), solo le agregas `.reset_index()` al final:
![[Pasted image 20260623121855.png]]

## 🛠️ La Sintaxis de un Analista Senior: El Método `.agg()`

En lugar de poner `.sum()` o `.mean()` al final, abres `.agg()` y le pasas un **diccionario de Python**. En ese diccionario, la _llave_ es la columna que quieres calcular, y el _valor_ es la operación que le vas a aplicar (en texto).
![[Pasted image 20260623122044.png]]

## 🛠️ La Herramienta Extra: `.sort_values()`

Si quieres ordenar tu resumen ejecutivo con base en una de las columnas que acabas de calcular, la sintaxis se ve así:

![[Pasted image 20260623122833.png]]

## 🐼 4. El Siguiente Nivel: Pandas + SQLAlchemy (Análisis Profesional) 
Para proyectos modernos de Data Science en Python, `pd.read_sql_query()` requiere un motor de conexión gestionado por **SQLAlchemy** para evitar advertencias de compatibilidad (`UserWarning`). 
### ⚙️ Instalación del Entorno Analítico 
pip install pandas sqlalchemy psycopg2-binary


## 🔍 5. Filtrado de Datos con Máscaras Booleanas en Pandas 
En lugar de escribir múltiples cláusulas `WHERE` en SQL, Pandas permite filtrar datos en memoria utilizando indexación condicional. 
### 📝 Sintaxis de Filtrado 
# Sintaxis base:
dataframe[dataframe["columna"] condicion]



## 🔗 Combinar DataFrames con `.merge()`

En Ciencia de Datos, la información suele estar fragmentada en múltiples tablas para evitar la duplicidad (normalización). El método `.merge()` de Pandas funciona exactamente igual que un **`JOIN` en SQL**, permitiendo cruzar dos tablas mediante una columna en común (llave).

### 🛠️ Tipos de Unión (`how`)
* **`inner` (Por defecto):** Conserva solo los registros cuyas llaves existen en **ambas** tablas. Si un ID no coincide, se descarta.
* **`left`:** Conserva todos los registros de la tabla izquierda y trae las coincidencias de la derecha. Si no hay coincidencia, rellena con `NaN`.
* **`right`:** Conserva todos los de la derecha y trae las coincidencias de la izquierda.
* **`outer`:** Conserva absolutamente todo. Si no hay coincidencia en algún lado, rellena con `NaN`.

### 💻 Sintaxis Estándar
```python
df_resultado = df_izquierda.merge(df_derecha, on="columna_compartida", how="inner")
```

## 📑 Nota 2: `06_concat_pandas.md`
## 🥞 Concatenar DataFrames con `.concat()`
A diferencia de `.merge()`, que combina columnas mediante una llave, `pd.concat()` se utiliza para **amontonar o apilar** DataFrames que comparten exactamente la misma estructura de columnas (por ejemplo, reportes mensuales o diarios). 
### 💡 Puntos Clave
* **Es una función de Pandas:** Se invoca como `pd.concat()`, no como un método del DataFrame. * **Recibe una lista:** Los DataFrames a unir se deben pasar dentro de corchetes `[...]`. * **`ignore_index=True`:** Obligatorio si quieres que Pandas regenere el índice (`0, 1, 2...`) secuencialmente, evitando que se repitan los índices de los archivos originales. 
### 💻 Sintaxis Estándar 
![[Pasted image 20260625222358.png]]


### 🧠 En resumen para tu Obsidian:

> 📌 **`ignore_index=True`**: Se usa al concatenar tablas (`pd.concat`) para evitar índices duplicados. Reinicia la numeración de las filas a un rango limpio que va desde `0` hasta el total de filas menos uno ($N-1$).

