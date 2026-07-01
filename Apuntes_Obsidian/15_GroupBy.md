# 📊 Agrupaciones de Datos: El Poder de `.groupby()`

En Pandas, `.groupby()` permite dividir los datos de un DataFrame en grupos basados en una o más columnas, para luego aplicar funciones de agregación. Este proceso se conoce en Ciencia de Datos como la estrategia **Split-Apply-Combine** (Dividir-Aplicar-Combinar).

## 🛠️ Herramientas Clave

### 1. Sintaxis Básica de Agregación
`df_agrupado = df.groupby("columna_grupo")["columna_calculo"].funcion()`

* `"columna_grupo"`: La columna que tiene categorías repetidas (ej. "marca", "equipo").
* `"columna_calculo"`: La columna numérica a la que le quieres hacer la operación matemática (ej. "precio", "puntos").
* `.funcion()`: La operación matemática que se ejecutará por grupo:
  * `.sum()` -> Suma total.
  * `.mean()` -> Promedio.
  * `.count()` -> Cuenta cuántos registros hay.

## ⚠️ Buena Práctica (El Índice Oculto)
Por defecto, `.groupby()` convierte la columna agrupada en el nuevo **índice** del DataFrame. Para evitar esto y mantener una tabla plana y limpia con índices numéricos normales, siempre utiliza `as_index=False`:
`df.groupby("marca", as_index=False)["precio_usd"].sum()`


### 🚀 Agregaciones Múltiples Avanzadas con `.agg()`
Cuando necesitas calcular diferentes estadísticas en un solo reporte, pasamos un diccionario dentro de `.agg()`, donde la LLAVE es la columna a calcular y el VALOR es una lista con las funciones que queremos:

df.groupby("columna_grupo", as_index=False).agg({
    "columna_numerica_1": ["sum", "mean"],
    "columna_numerica_2": ["count"]
})
