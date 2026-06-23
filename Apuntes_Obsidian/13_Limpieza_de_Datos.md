## 🧹 Limpieza de Datos: El Manejo de Valores Faltantes (`NaN`)

En la Ciencia de Datos, más del **70% del tiempo** de un proyecto se va en limpiar los datos. Un DataFrame sucio con valores nulos altera las operaciones estadísticas (la media, la desviación estándar, etc.) y hace que los modelos de Machine Learning truenen como palomitas.

### ❓ ¿Qué es un `NaN`?

En Pandas, un dato faltante se etiqueta como **`NaN`** (_Not a Number_). Proviene técnicamente de la librería NumPy (`np.nan`) y representa un vacío, un valor desconocido o un error de registro.

## 🛠️ Las 3 Operaciones Sagradas de la Limpieza

Para limpiar tu set de datos, el flujo de trabajo estándar tiene tres fases obligatorias:

### 1. El Diagnóstico (`.isna().sum()`)

Antes de borrar o modificar cualquier cosa, necesitas saber a qué te enfrentas. Este comando analiza todo tu DataFrame, encuentra los nulos y te da un conteo sumado por cada columna.
![[Pasted image 20260622215420.png]]

### 2. La Imputación o Relleno (`.fillna()`)

Consiste en **reemplazar** los `NaN` por un valor estratégico para no perder toda la fila de información.

- **¿Cuándo usarlo?** Cuando la columna es vital y puedes asumir un valor por defecto (como poner `0` en una deuda, o calcular la `media` o la `mediana` de la columna para no alterar la tendencia).
![[Pasted image 20260622215442.png]]

### 3. La Eliminación (`.dropna()`)

Consiste en **borrar** por completo las filas o columnas que contienen valores nulos.

- **¿Cuándo usarlo?** Cuando el dato faltante es crítico y no se puede inventar ni promediar (por ejemplo, si falta el ID del cliente o el nombre del producto), o cuando las filas con nulos son un porcentaje insignificante de tu base de datos (menos del 5%).
![[Pasted image 20260622215502.png]]

### 💡 Un único "Pro-Tip" de Senior para tus notas

Tu código corre al 100%, pero si notas tu terminal, probablemente te arrojó un texto de advertencia amarillo gigante llamado `SettingWithCopyWarning` justo en la línea donde creaste la columna.

No es un error (el código funciona), es solo Pandas siendo un poquito tóxico. Te advierte que `df_ventas_limpio` es un "pedazo" que derivó de `df_ventas_sucio`, y cambiarlo podría alterar la tabla original.

Para evitar que Pandas te mande ese aviso enfadoso en Kitty, la regla de oro es agregarle un `.copy()` al final de tu `.dropna()`. Así le dices de forma explícita que es una tabla totalmente nueva e independiente:

![[Pasted image 20260622222026.png]]

### Código Ejercicios:

#### ventas_sucias.csv
![[Pasted image 20260622222115.png]]

#### Consultor_Ventas.py
![[Pasted image 20260622222144.png]]

