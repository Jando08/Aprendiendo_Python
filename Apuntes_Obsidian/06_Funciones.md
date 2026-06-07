# 📑 Apunte de Obsidian: Funciones en Python (`def`)

Una función es un bloque de código reutilizable diseñado para realizar una tarea específica. En lugar de escribir el mismo código una y otra vez, lo agrupas dentro de una función y lo llamas cada vez que lo necesitas.

## 🎯 ¿Para qué sirve? (Información Importante)

Imagínate que en varios lados de tu programa necesitas pedir el nombre de un jugador, limpiarlo con `.strip()` y pasarlo a mayúsculas con `.upper()`. En lugar de repetir esas líneas por todo tu script, creas una función que lo haga por ti.

Esto aplica el principio **DRY** (_Don't Repeat Yourself_ / No te repitas), haciendo que tu código sea más corto, limpio y fácil de corregir.

## ⚙️ Características Principales

- **Reutilización:** Ecribes el código una sola vez y lo puedes usar miles de veces.
    
- **Modularidad:** Te permite dividir un problema gigante en pedacitos chiquitos y ordenados.
    
- **Parámetros (Entradas):** Puede recibir datos para trabajar con ellos.
    
- **Retorno (Salidas):** Puede devolverte un resultado usando la palabra clave `return`.
    

## 🚦 Normas y Sintaxis Básica

Para crear una función usamos la palabra clave **`def`** (de _define_). Mira la estructura:

![[Pasted image 20260606171720.png]]
### 🧩 Componentes clave:

1. **`def`**: Le avisa a Python que vas a construir una función.
    
2. **`nombre_de_la_funcion()`**: Se recomienda usar verbos en minúsculas y separados por guiones bajos (estilo _snake_case_).
    
3. **Parámetros (`nombre`)**: Son las variables que la función necesita recibir entre los paréntesis para poder chambear.
    
4. **`return`**: Es la cláusula de salida. Detiene la función y "escupe" el resultado hacia donde la llamaste.
    

## ⚠️ Errores Comunes y Soluciones

### 1. `TypeError: ... missing 1 required positional argument`

- **¿Por qué ocurre?:** Definiste que tu función necesita un dato para trabajar (un parámetro), pero cuando la llamaste entre los paréntesis, se te olvidó pasárselo.
    
- **❌ Código Incorrecto:**
![[Pasted image 20260606171744.png]]

- **✔️ Solución:** Pásale el dato requerido dentro de los paréntesis al llamarla: `calcular_triple(5)`.
    

### 2. La función devuelve `None` (Vacío)

- **¿Por qué ocurre?:** Tu función hace cálculos por dentro, pero se te olvidó poner la palabra clave `return` al final. Si no hay `return`, Python asume que la función no devuelve nada.
    
- **❌ Código Incorrecto:**
![[Pasted image 20260606171809.png]]


**✔️ Solución:** Asegúrate de cerrar tu función con `return resultado` para que el dato pueda salir al exterior.