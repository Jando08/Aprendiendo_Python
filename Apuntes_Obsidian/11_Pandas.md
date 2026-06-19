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


