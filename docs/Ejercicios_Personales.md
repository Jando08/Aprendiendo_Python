# Documentación del Módulo: Ejercicios Personales

Este módulo agrupa una serie de ejercicios de programación diseñados para la práctica de conceptos fundamentales de Python. Está estructurado para permitir la separación lógica de diferentes problemas de negocio o escenarios de simulación.

**Ubicación del Módulo:**
`/home/tadeofed/Aprendiendo_Python/Ejercicios_Personales`

***

## 📁 Estructura de Archivos

Esta tabla lista los archivos que componen el módulo. Cada archivo contiene la lógica y las funcionalidades específicas para un ejercicio determinado.

| Archivo | Tipo | Propósito Descriptivo |
| :--- | :--- | :--- |
| `Practica_if_else.py` | Módulo Python | Contiene ejercicios enfocados en la aplicación de estructuras condicionales (`if/elif/else`), ideal para practicar la lógica de decisión. |
| `Simulador_Equipaje_Aeropuerto.py` | Módulo Python | Implementa un simulador que gestiona la información y las reglas de equipaje para un aeropuerto. |
| `Tienda_Mascotas.py` | Módulo Python | Gestiona la lógica de negocio para una tienda de mascotas, incluyendo cálculo de precios y descuentos. |

***

## 📦 Exportaciones del Módulo (`Exports`)

Esta sección detalla todos los elementos (constantes, variables, o resultados de funciones) que son exportados o accesibles desde cada módulo individual. Estos elementos representan los datos clave o resultados que otros componentes podrían consumir.

### 1. Exportaciones de `Practica_if_else.py`

| Nombre Exportado | Tipo | Descripción Contextual |
| :--- | :--- | :--- |
| `usuario_registrado` | `module` | Indicador o datos relacionados con un usuario previamente registrado. |
| `password_correcto` | `module` | Verificación o valor asociado a una contraseña válida. |
| `mensaje` | `module` | Mensaje de resultado o retroalimentación general generado por el ejercicio. |

### 2. Exportaciones de `Simulador_Equipaje_Aeropuerto.py`

Este módulo exporta varias variables que representan los parámetros de entrada y los resultados clave del simulador de equipaje.

| Nombre Exportado | Tipo | Descripción Contextual |
| :--- | :--- | :--- |
| `nombre` | `module` | Nombre del pasajero o dueño del equipaje. |
| `nombre` | `module` | *Segundo registro de nombre.* Puede representar un segundo nombre o un dato de identificación. |
| `tipo_boleto` | `module` | El tipo de billete de avión adquirido. |
| `tipo_boleto` | `module` | *Segundo registro de tipo de boleto.* Podría indicar una categoría o nivel específico del billete. |
| `peso_maleta` | `module` | El peso calculado o declarado del equipaje. |
| `mensaje` | `module` | Mensaje de salida que informa si el equipaje es aceptable o qué acciones son necesarias. |

### 3. Exportaciones de `Tienda_Mascotas.py`

Este módulo expone datos relacionados con el cliente y la transacción de compra en la tienda de mascotas.

| Nombre Exportado | Tipo | Descripción Contextual |
| :--- | :--- | :--- |
| `bienvenida` | `module` | Texto o función utilizada para dar la bienvenida al usuario de la tienda. |
| `bienvenida` | `module` | *Segundo registro de bienvenida.* Podría representar una versión o mensaje complementario de bienvenida. |
| `nombre` | `module` | Nombre del dueño de la mascota o del cliente. |
| `nombre` | `module` | *Segundo registro de nombre.* Podría representar un identificador secundario o apodo. |
| `edad` | `module` | La edad del animal o la mascota en cuestión. |
| `mensaje` | `module` | Mensaje de confirmación o resultado de la compra. |
| `descuento` | `module` | El porcentaje o valor monetario del descuento aplicado a la compra. |