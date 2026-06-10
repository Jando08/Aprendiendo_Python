# Módulo: Sintaxis\_Variables

Este módulo agrupa ejemplos prácticos para ilustrar y reforzar los conceptos fundamentales de la sintaxis de Python, centrándose en la manipulación de variables y los tipos de datos básicos. Es un conjunto de recursos diseñados para el aprendizaje progresivo de la programación.

**Ubicación del Módulo:**
`[Proyecto]/Sintaxis_Variables`

---

## Estructura de Archivos (File Structure)

La implementación del módulo se divide en tres archivos especializados, cada uno dedicado a un subconjunto de conocimientos sintácticos:

| Archivo | Propósito | Descripción |
| :--- | :--- | :--- |
| `Calculadora_Edad_Perro.py` | Módulo de aplicación | Contiene lógica de negocio centrada en la conversión de unidades de tiempo, simulando la edad de un perro en unidades humanas o caninas. |
| `Sintaxis_Basica.py` | Módulo de práctica | Agrupa ejemplos de sintaxis y estructuras de control básicas de Python. |
| `Variables_Tipos_de_Datos.py` | Módulo de conceptos | Demuestra el uso y la inicialización de variables con diversos tipos de datos de Python (cadenas, enteros, flotantes, etc.). |

## Exportaciones y Contenido Público (Exports)

Los siguientes elementos son expuestos (o exportados) desde los módulos componentes y están disponibles para ser importados y utilizados en otros proyectos.

### **`Calculadora_Edad_Perro.py`**

Este módulo exporta funciones o variables relacionadas con el cálculo de edades.

| Nombre | Tipo | Archivo Fuente | Descripción |
| :--- | :--- | :--- | :--- |
| `nombre_perro` | `module` | `Calculadora_Edad_Perro.py` | Exporta el nombre del perro utilizado en los ejemplos. |
| `edad_perro_humana` | `module` | `Calculadora_Edad_Perro.py` | Calcula y expone la edad del perro en unidades humanas. |
| `edad_perro_canina` | `module` | `Calculadora_Edad_Perro.py` | Calcula y expone la edad del perro utilizando una escala canina. |

### **`Variables_Tipos_de_Datos.py`**

Este módulo sirve como repositorio de ejemplos de variables inicializadas con diferentes tipos de datos.

| Nombre | Tipo | Archivo Fuente | Uso Típico |
| :--- | :--- | :--- | :--- |
| `nombre` | `module` | `Variables_Tipos_de_Datos.py` | Almacena una cadena de texto (string) que representa un nombre. |
| `edad` | `module` | `Variables_Tipos_de_Datos.py` | Almacena un valor entero (integer) que representa una edad. |
| `precio_bitcoin` | `module` | `Variables_Tipos_de_Datos.py` | Almacena un valor flotante (float) con precisión decimal, útil para precios. |
| `me_gusta_python` | `module` | `Variables_Tipos_de_Datos.py` | Variable de ejemplo que utiliza un tipo de dato booleano (boolean) o una cadena descriptiva. |