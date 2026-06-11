## 🎯 ¿Para qué sirven? (Estructura Clave-Valor)

Un diccionario te permite agrupar toda la información de un solo objeto o entidad en un solo lugar de forma ultra organizada.

### 📋 Sintaxis Básica:

![[Pasted image 20260609120902.png]]

## 🚦 Reglas de Oro de los Diccionarios

- **Las Claves son únicas:** No puedes tener dos claves llamadas `"nombre"`. Si pones otra abajo, Python va a borrar la primera y se va a quedar con la nueva.
    
- **Son mutables:** Puedes cambiar los valores, agregar nuevas claves o borrarlas cuando quieras.
    
- **Cualquier tipo de dato:** Adentro de un diccionario puedes meter strings, números, booleanos, ¡e incluso listas u otros diccionarios!
## ⚠️ El Error Típico: `KeyError`

- **¿Por qué ocurre?:** Intentas pedirle a Python que te dé el valor de una clave que **no existe** adentro del diccionario.
    
- **❌ Código Incorrecto:**
    

print(jugador["edad"]) # 💥 ERROR: KeyError: 'edad' (porque no la definimos arriba)


Los **Diccionarios** (`{}`) son estructuras de datos que guardan la información en formato de **Clave-Valor**. A diferencia de las listas (que usan posiciones `0, 1, 2...`), los diccionarios te permiten acceder a los datos usando un nombre único (la clave).

## 🎯 1. Sintaxis Básica y Mutación

- **Crear:** Se usan llaves `{}` y se separa la clave del valor con dos puntos `:`.
    
- **Modificar:** Accedes a la clave y le asignas el nuevo valor.
    
- **Agregar:** Si asignas un valor a una clave que **no existe**, Python la crea automáticamente.
![[Pasted image 20260609132216.png]]

## 🛡️ 2. El Método Seguro `.get()`

Cuando buscas una clave con los corchetes tradicionales (`diccionario['clave']`) y esta no existe, el programa explota con un `KeyError`. Para evitar esto, usamos el método `.get()`.

- Si la clave **existe**, te devuelve su valor (el de la derecha `:`).
    
- Si la clave **no existe**, te devuelve `None` en lugar de romper el programa.
    
- **Valor por defecto:** Puedes pasarle un segundo parámetro para que te devuelva un mensaje o número personalizado si no encuentra nada.
![[Pasted image 20260609132251.png]]

## ⛓️ 3. Colecciones Anidadas (Estructuras Complejas)

Un diccionario puede guardar cualquier tipo de dato en su lado derecho, incluyendo **listas** u **otros diccionarios**. Para acceder a los niveles más profundos, se van encadenando corchetes `[]` capa por capa.

![[Pasted image 20260609132321.png]]

## 🚦 4. Recorrer Diccionarios con Ciclos `for`

Por defecto, un ciclo `for` sobre un diccionario solo extrae las **claves**. Tenemos dos formas principales de operarlo:

### Opción A: Usando el método `.items()` (Desempaquetado directo)

Te extrae la clave y el valor al mismo tiempo en dos variables distintas.

![[Pasted image 20260609132356.png]]

## ⚠️ 5. Regla de Oro: Comillas en f-strings

Cuando uses un **f-string**, tienes que alternar (campechanear) el tipo de comillas para que Python no piense que el texto se terminó antes de tiempo.

- ❌ **Incorrecto:** `f'Bienvenido {cuenta['nombre']}'` _(Rompe el código)_
    
- ✔️ **Correcto:** `f"Bienvenido {cuenta['nombre']}"` _(Comillas dobles afuera, simples adentro)_
    

## 🚀 6. Eficiencia: ¿Por qué usar Diccionarios?

Los diccionarios en Python utilizan un mecanismo llamado **Tabla Hash (Hashing)**. No importa si el diccionario tiene 3 elementos o 10 millones; Python no busca línea por línea. Aplica una función matemática a la clave para ir **directo** a su posición en memoria, haciendo que las búsquedas con `.get()` o corchetes sean instantáneas.