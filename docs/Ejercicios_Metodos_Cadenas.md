# Documentación del Módulo: Ejercicios de Métodos de Cadenas (Strings)

Este módulo agrupa ejercicios prácticos diseñados para reforzar la comprensión y el uso de los métodos nativos de manipulación de cadenas (strings) en Python. Cada archivo corresponde a un método específico, proporcionando ejemplos prácticos y funciones para resolver desafíos comunes.

**Ubicación del Proyecto:** `/home/tadeofed/Aprendiendo_Python/Ejercicios_Metodos_Cadenas`

***

## 📁 Estructura de Archivos (`File Structure`)

Esta tabla detalla la organización del proyecto y el propósito de cada archivo Python.

| Archivo | Tipo | Propósito Descriptivo | Métodos Enfocados |
| :--- | :--- | :--- | :--- |
| `Ejercicio_Capitalize.py` | Módulo Python | Ejercicios sobre la conversión y manejo de mayúsculas y minúsculas de textos. | `capitalize()` |
| `Ejercicio_Count.py` | Módulo Python | Ejercicios que se centran en contar o identificar patrones dentro de cadenas. | `count()` |
| `Ejercicio_Endwith.py` | Módulo Python | Prácticas para verificar si una cadena termina con un sufijo específico. | `endswith()` |
| `Ejercicio_Find.py` | Módulo Python | Implementación de búsqueda de subcadenas dentro de un texto mayor. | `find()` |
| `Ejercicio_Index.py` | Módulo Python | Ejercicios de manipulación y acceso por índice (posición) de caracteres en una cadena. | `index()` |
| `Ejercicio_Len.py` | Módulo Python | Cálculo de la longitud de diferentes tipos de cadenas. | `len()` |
| `Ejercicio_Lower.py` | Módulo Python | Métodos para convertir cadenas a minúsculas de manera controlada. | `lower()` |
| `Ejercicio_Replace.py` | Módulo Python | Ejercicios sobre la sustitución de segmentos de texto dentro de una cadena. | `replace()` |
| `Ejercicio_Split.py` | Módulo Python | Funciones que dividen una cadena en una lista utilizando un delimitador específico. | `split()` |
| `Ejercicio_Startwith.py` | Módulo Python | Prácticas para verificar si una cadena comienza con un prefijo determinado. | `startswith()` |
| `Ejercicio_Title.py` | Módulo Python | Manejo de capitalización para títulos o nombres propios. | `title()` |
| `Ejercicio_Upper.py` | Módulo Python | Conversión de textos completos a mayúsculas. | `upper()` |

***

## 📤 Exportaciones (Módulos y Funciones Disponibles)

Esta tabla lista todos los elementos funcionales o variables que están exportados desde el módulo, agrupados por su archivo de origen.

| Nombre | Tipo | Archivo Origen | Descripción / Uso |
| :--- | :--- | :--- | :--- |
| **Manejo de Capitalización (`Ejercicio_Capitalize.py`)** | | | |
| `nombre_normal` | `module` | `Ejercicio_Capitalize.py` | Muestra el procesamiento de un nombre en formato normal. |
| `nombre_mayuscula` | `module` | `Ejercicio_Capitalize.py` | Muestra el procesamiento de un nombre en formato mayúsculo. |
| **Conteo de Caracteres (`Ejercicio_Count.py`)** | | | |
| `trabalenguas` | `module` | `Ejercicio_Count.py` | Contabiliza la ocurrencia de patrones en un trabalenguas. |
| `letra_encontrada` | `module` | `Ejercicio_Count.py` | Cuenta la frecuencia de una letra específica en el texto. |
| **Verificación de Sufijo (`Ejercicio_Endwith.py`)** | | | |
| `archivo` | `module` | `Ejercicio_Endwith.py` | Verifica si una cadena de tipo archivo cumple con un patrón final. |
| `mensaje` | `module` | `Ejercicio_Endwith.py` | Verifica si un mensaje termina con un formato específico. |
| **Búsqueda de Subcadenas (`Ejercicio_Find.py`)** | | | |
| `frase` | `module` | `Ejercicio_Find.py` | Implementa la búsqueda de una subcadena dentro de una frase. |
| `encontrar_palabra` | `module` | `Ejercicio_Find.py` | Función que demuestra la posición de la palabra buscada. |
| **Acceso por Índice (`Ejercicio_Index.py`)** | | | |
| `frase_larga` | `module` | `Ejercicio_Index.py` | Cadena base utilizada para ejercicios de índice. |
| `letra` | `module` | `Ejercicio_Index.py` | Elemento de prueba para el acceso por índice. |
| `letra` | `module` | `Ejercicio_Index.py` | (Repetido) Elemento de prueba para el acceso por índice. |
| **Longitud (`Ejercicio_Len.py`)** | | | |
| `tweet` | `module` | `Ejercicio_Len.py` | Cadena de ejemplo para calcular longitud (ej. un tuit). |
| `mensaje` | `module` | `Ejercicio_Len.py` | Cadena de ejemplo de mensaje. |
| `calcular_caracteres` | `module` | `Ejercicio_Len.py` | Función dedicada al cálculo de la longitud total de caracteres. |
| `calcular_caracteres` | `module` | `Ejercicio_Len.py` | (Repetido) Función de cálculo de caracteres. |
| **Minúsculas (`Ejercicio_Lower.py`)** | | | |
| `correo_normal` | `module` | `Ejercicio_Lower.py` | Muestra un correo electrónico en formato estándar (normal). |
| `password_normal` | `module` | `Ejercicio_Lower.py` | Muestra una contraseña de ejemplo en formato estándar. |
| `correo_minuscula` | `module` | `Ejercicio_Lower.py` | Muestra un correo electrónico en formato de minúsculas. |
| `password_minuscula` | `module` | `Ejercicio_Lower.py` | Muestra una contraseña de ejemplo completamente en minúsculas. |
| **Reemplazo (`Ejercicio_Replace.py`)** | | | |
| `frase_con_groseria` | `module` | `Ejercicio_Replace.py` | Frase inicial que contiene contenido a ser censurado. |
| `frase_sin_groseria` | `module` | `Ejercicio_Replace.py` | Frase resultante tras aplicar la sustitución de contenido inapropiado. |
| **División (`Ejercicio_Split.py`)** | | | |
| `fecha_nacimiento` | `module` | `Ejercicio_Split.py` | Cadena de fecha que requiere división. |
| `fecha_convertida` | `module` | `Ejercicio_Split.py` | Resultado de la división y reestructuración de la fecha. |
| **Verificación de Prefijo (`Ejercicio_Startwith.py`)** | | | |
| `url` | `module` | `Ejercicio_Startwith.py` | Cadena de URL para verificar su inicio. |
| `mensaje` | `module` | `Ejercicio_Startwith.py` | Cadena de mensaje para verificar su inicio. |
| **Títulos y Nombres Propios (`Ejercicio_Title.py`)** | | | |
| `nom_peli_minu` | `module` | `Ejercicio_Title.py` | Nombre de película o título en minúsculas. |
| `nom_peli_mayu_prim_letra` | `module` | `Ejercicio_Title.py` | Aplicación de capitalización de título (Mayúscula inicial). |
| **Mayúsculas (`Ejercicio_Upper.py`)** | | | |
| `grito_de_ayuda_minuscula` | `module` | `Ejercicio_Upper.py` | Frase de ejemplo en minúsculas. |
| `grito_de_ayuda_mayuscula` | `module` | `Ejercicio_Upper.py` | Frase de ejemplo convertida completamente a mayúsculas. |