# 🛡️ Manejo de Errores y Excepciones 
El manejo de errores evita que nuestro programa crashee (se cierre con letras rojas) ante fallos inesperados de datos o del sistema. 
## 🧱 Estructura Try / Except 
* **`try`**: Ponemos el código "peligroso" que podría fallar. * **`except`**: El escudo que se activa si ocurre un error específico. 
## 🗂️ Tabla de Errores Comunes 
| Excepción | ¿Por qué ocurre? | | :--- | :--- | | `ValueError` | Valor incorrecto (ej: `int("veintidos")`). | | `TypeError` | Combinar tipos de datos inválidos (ej: Texto + Número). | | `KeyError` | Buscar una clave inexistente en un diccionario. | | `IndexError` | Buscar una posición fuera del límite de una lista. | 

```python
 try: edad = int("veintidos") except ValueError: print("❌ Error: Ingresa un número válido en dígitos.")