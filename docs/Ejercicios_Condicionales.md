# Documentación Técnica: Módulo de Ejercicios de Lógica Condicional

Este módulo recopila una serie de ejercicios prácticos diseñados para fortalecer la comprensión y aplicación de la lógica condicional (`if`/`elif`/`else`) en el lenguaje Python. Su objetivo es proporcionar ejemplos claros y reutilizables para diversos escenarios de toma de decisiones en programación.

---

**Ubicación del Módulo:**
`/home/tadeofed/Aprendiendo_Python/Ejercicios_Condicionales`

## 📚 Estructura de Archivos

La siguiente tabla detalla los archivos que componen este módulo y el propósito específico de cada uno, agrupando los ejercicios por su temática lógica.

| Archivo | Tipo | Propósito / Descripción |
| :--- | :--- | :--- |
| `ejercicio_calcular_descuento.py` | Módulo Python | Implementa la lógica para calcular descuentos y precios finales basados en condiciones específicas de compra. |
| `ejercicio_calificaciones.py` | Módulo Python | Gestiona la asignación de puntuaciones y determina la calificación final de un estudiante basándose en parámetros establecidos. |
| `ejercicio_edad_mayor_menor.py` | Módulo Python | Realiza comprobaciones de edad para determinar si una persona es mayor o menor de edad, aplicando lógica de rangos. |
| `ejercicio_numero_par_impar.py` | Módulo Python | Verifica si un número entero dado es par o impar utilizando el operador de módulo (`%`). |
| `ejercicio_triangulo.py` | Módulo Python | Contiene la lógica para validar si tres lados pueden formar un triángulo, aplicando las desigualdades geométricas. |

## 🚀 Exportaciones (API)

Esta sección lista las funciones (módulos o métodos) disponibles para ser importadas y utilizadas desde cada archivo, facilitando la integración de la lógica de los ejercicios en otras partes de la aplicación.

### `ejercicio_calcular_descuento.py`

| Nombre de la Función | Tipo | Fuente | Descripción |
| :--- | :--- | :--- | :--- |
| `compra_sin_descuento` | Módulo | `ejercicio_calcular_descuento.py` | Calcula el total de la compra cuando no se aplica ningún descuento. |
| `descuento` | Módulo | `ejercicio_calcular_descuento.py` | Determina el porcentaje de descuento aplicable según el valor total. |
| `compra_con_descuento` | Módulo | `ejercicio_calcular_descuento.py` | Calcula el precio final de la compra después de aplicar el descuento correspondiente. |
| `mensaje` | Módulo | `ejercicio_calcular_descuento.py` | Genera mensajes de texto descriptivos sobre el estado de la compra o el descuento. |

### `ejercicio_calificaciones.py`

| Nombre de la Función | Tipo | Fuente | Descripción |
| :--- | :--- | :--- | :--- |
| `puntuacion` | Módulo | `ejercicio_calificaciones.py` | Calcula la puntuación acumulada o el promedio del estudiante. |

### `ejercicio_edad_mayor_menor.py`

| Nombre de la Función | Tipo | Fuente | Descripción |
| :--- | :--- | :--- | :--- |
| `edad` | Módulo | `ejercicio_edad_mayor_menor.py` | Verifica y clasifica la edad proporcionada como mayor o menor de edad. |
| `mensaje` | Módulo | `ejercicio_edad_mayor_menor.py` | Devuelve un mensaje de estado basado en la comprobación de edad. |

### `ejercicio_numero_par_impar.py`

| Nombre de la Función | Tipo | Fuente | Descripción |
| :--- | :--- | :--- | :--- |
| `numero` | Módulo | `ejercicio_numero_par_impar.py` | Realiza la verificación lógica para determinar si un número entero es par o impar. |
| `mensaje` | Módulo | `ejercicio_numero_par_impar.py` | Genera un mensaje textual indicando si el número ingresado cumple con la condición par o impar. |

### `ejercicio_triangulo.py`

| Nombre de la Función | Tipo | Fuente | Descripción |
| :--- | :--- | :--- | :--- |
| `lado_a` | Módulo | `ejercicio_triangulo.py` | Representa el primer lado del triángulo a verificar. |
| `lado_b` | Módulo | `ejercicio_triangulo.py` | Representa el segundo lado del triángulo a verificar. |
| `lado_c` | Módulo | `ejercicio_triangulo.py` | Representa el tercer lado del triángulo a verificar. |
| `mensaje` | Módulo | `ejercicio_triangulo.py` | Devuelve un mensaje de confirmación o rechazo sobre la validez del triángulo. |