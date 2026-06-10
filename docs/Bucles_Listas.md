# Documentación del Proyecto: Lógica y Estructuras de Control
***

**Módulo:** Bucles y Estructuras de Datos (Listas)
**Ubicación del Proyecto:** `/home/tadeofed/Aprendiendo_Python/Aprendiendo_Python_Roadmap/Bucles_Listas`
**Propósito:** Este módulo recopila y organiza diversos scripts Python diseñados para practicar y aplicar estructuras de control fundamentales como bucles (`for`, `while`) y la manipulación avanzada de estructuras de datos como listas, consolidando el aprendizaje práctico en diferentes escenarios.

---

## 📁 Estructura de Archivos del Proyecto (File Structure)

Esta sección detalla el conjunto de archivos Python que componen el proyecto. Cada archivo encapsula la lógica para una funcionalidad específica.

| Archivo | Tipo | Propósito Principal |
| :--- | :--- | :--- |
| `Control_Calidad.py` | Módulo Python | Implementación de lógica para la simulación de inspecciones de calidad de pantallas. |
| `Detector_Ataques.py` | Módulo Python | Desarrollo de módulos dedicados a la detección y el conteo de patrones de eventos, como intentos fallidos. |
| `Estadisticas_NBA.py` | Módulo Python | Manejo de cálculos y reportes estadísticos avanzados relacionados con partidos de la NBA. |
| `Filtro_Reproducciones.py` | Módulo Python | Funcionalidad dedicada a filtrar y procesar colecciones de datos de reproducciones de video. |
| `Inventario_Gaming.py` | Módulo Python | Gestión y cálculo de métricas económicas para la simulación de un inventario de productos de gaming. |
| `Monitor_NBA.py` | Módulo Python | Módulo de monitoreo y clasificación de equipos basados en datos históricos de la NBA. |

## 📦 Módulos Exportables y Funcionalidades Clave (Exports)

Esta tabla lista los componentes funcionales o módulos específicos que han sido definidos y exportados dentro de los archivos, permitiendo su uso en otras partes del proyecto.

| Nombre del Export | Tipo de Componente | Archivo de Origen | Descripción Funcional |
| :--- | :--- | :--- | :--- |
| `pixeles_muertos` | Módulo | `Control_Calidad.py` | Lógica para el conteo de píxeles muertos detectados durante pruebas de calidad. |
| `pantallas_defectuosas` | Módulo | `Control_Calidad.py` | Módulo que clasifica y registra pantallas que superan el umbral de defectos. |
| `intentos_fallidos` | Módulo | `Detector_Ataques.py` | Calcula y reporta la frecuencia de intentos de acceso o ejecución fallidos. |
| `alerta_criticas` | Módulo | `Detector_Ataques.py` | Módulo encargado de generar alertas ante patrones de ataque o actividad crítica. |
| `puntos_partidos` | Módulo | `Estadisticas_NBA.py` | Calcula y reporta la cantidad total de puntos anotados por los equipos. |
| `partizados_totales` | Módulo | `Estadisticas_NBA.py` | Determina el recuento de partidos jugados dentro de un conjunto de datos. |
| `reproducciones` | Módulo | `Filtro_Reproducciones.py` | Implementación del filtro principal para procesar y seleccionar reproducciones específicas. |
| `precios` | Módulo | `Inventario_Gaming.py` | Gestiona el cálculo y la asignación de precios unitarios para el inventario. |
| `gasto_total` | Módulo | `Inventario_Gaming.py` | Calcula el gasto o el costo total basado en el inventario y los precios unitarios. |
| `clasificados` | Módulo | `Monitor_NBA.py` | Genera la clasificación (ranking) de equipos basada en las métricas de la NBA. |