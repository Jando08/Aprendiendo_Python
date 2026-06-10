# Módulo: Diccionarios

Este módulo centraliza la implementación y el uso de estructuras de datos de tipo diccionario en Python, facilitando la gestión de datos asociados a cuentas de usuario, inventarios, estadísticas de jugadores y funcionalidades de prueba. Sirve como un repositorio de código para ejercicios prácticos sobre manipulación de diccionarios.

**Ubicación del Módulo:**
`/home/tadeofed/Aprendiendo_Python/Aprendiendo_Python_Roadmap/Diccionarios`

---

## 📂 Estructura de Archivos (`File Structure`)

La siguiente tabla describe los módulos componentes que conforman el proyecto y su respectivo objetivo funcional.

| Archivo | Tipo | Propósito Descriptivo |
| :--- | :--- | :--- |
| `Administrador_Cuentas.py` | Módulo Python | Contiene la lógica para la gestión, búsqueda y manipulación de datos de cuentas de usuario. |
| `Arsenal_Jugador.py` | Módulo Python | Implementa la estructura de datos que representa el arsenal de un jugador, incluyendo la gestión de armas. |
| `Detector_MVP.py` | Módulo Python | Dedicado a la simulación y cálculo de estadísticas o métricas (MVP) de jugadores. |
| `Inventario_OXXO.py` | Módulo Python | Gestiona el inventario de productos, con funcionalidades de búsqueda y cálculo de precios. |
| `Perfil_Jugador.py` | Módulo Python | Define la estructura y el cálculo de métricas de perfil general de un jugador (ej. total de puntos). |
| `Prueba_Diccionarios.py` | Módulo Python | Un módulo de prueba dedicado a demostrar y verificar las funcionalidades de manejo de diccionarios. |

---

## 🚀 API de Exportación (`Exports`)

Esta sección lista todos los elementos (módulos, constantes o clases) que son expuestos públicamente por los módulos internos y que pueden ser importados y utilizados por otros scripts del proyecto.

| Nombre | Tipo de Elemento | Módulo Fuente | Descripción Breve |
| :--- | :--- | :--- | :--- |
| `usuarios` | Módulo | `Administrador_Cuentas.py` | Datos o funciones relacionadas con la gestión de usuarios. |
| `username` | Módulo | `Administrador_Cuentas.py` | Elemento o variable para la identificación de usuario. |
| `cuenta_encontrada` | Módulo | `Administrador_Cuentas.py` | Resultado o estructura de datos de una cuenta localizada. |
| `arsenal` | Módulo | `Arsenal_Jugador.py` | Colección de armas o equipos pertenecientes al jugador. |
| `arma` | Módulo | `Arsenal_Jugador.py` | Elementos o datos asociados a las armas del jugador. |
| `arma_encontrada` | Módulo | `Arsenal_Jugador.py` | Estructura de datos para una arma localizada. |
| `lakers_stats` | Módulo | `Detector_MVP.py` | Estadísticas relacionadas con el equipo Lakers para cálculos de MVP. |
| `inventario` | Módulo | `Inventario_OXXO.py` | Diccionario principal que contiene todos los productos del inventario. |
| `busqueda` | Módulo | `Inventario_OXXO.py` | Función o método para buscar productos dentro del inventario. |
| `precio` | Módulo | `Inventario_OXXO.py` | Estructura o cálculo del precio de los productos. |
| `perfil_jugador` | Módulo | `Perfil_Jugador.py` | Datos o estructura que representan el perfil completo del jugador. |
| `total_puntos` | Módulo | `Perfil_Jugador.py` | Cálculo o valor del total de puntos acumulados por el jugador. |
| `mi_laptop` | Módulo | `Prueba_Diccionarios.py` | Elemento de prueba utilizado para demostrar el funcionamiento del módulo. |