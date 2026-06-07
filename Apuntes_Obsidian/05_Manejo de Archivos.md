# 📁 Manejo de Archivos (`.txt`) 
Permite la persistencia de datos, es decir, guardar la información de manera permanente en el disco duro. 
## ✍️ Escribir Archivos con `with open()`
Usamos la estructura moderna `with` para que Python cierre el archivo automáticamente al terminar y no se corrompa. * El modo `"w"` (*Write*) crea el archivo o sobrescribe todo su contenido. * El comando `\n` se usa para hacer saltos de línea (un Enter).

## 📑 Apunte de Obsidian: La Estructura `with` en Python
El bloque **with** (conocido tecnicamente como Contetext Manager o Administrador de Contexto) es la forma estandar y segura de manejar recursos externos en Python, como archivos (.txt), conexiones a bases de datos o sockets de red.

## 🎯 ¿Para qué sirve? (Información Importante)
Antes, para manejar un archivo tenias que abrirlo y acordarte de cerrarlo manuelamente con **.close()**. Si tu codigo fallaba a la mitad, el archivo se quedaba abierto y se corrompia. **with** elimina ese problema: se **encarga de abrir el recurso y garantiza que se cierre automaticamente** en cuanto el codigo termina de ejecutarse (con sangria), incluso si ocurre un error inesperado dentro del bloque.

## ⚙️ Características Principales

1. **Cierre Automático Garantizado:** No importa si tu código termina limpio o explota a la mitad; el archivo se cierra de forma segura.
    
2. **Código más Limpio:** Reduce las líneas de código al eliminar la necesidad de usar funciones de cierre manual o estructuras complejas de seguridad.
    
3. **Control de Ámbito (Scope):** Las variables que escribes dentro del bloque funcionan allí, pero el flujo del archivo solo está activo mientras estés dentro de la indentación (sangría).


## 🚦 Normas y Sintaxis Básica

Para usarlo correctamente, debes seguir esta estructura:
![[Pasted image 20260603215508.png]]

1. **`with open(...)`**: Llama a la función para interactuar con el archivo.
    
2. **`as alias`**: Le asigna un nombre temporal (una variable) al archivo abierto para que puedas usar métodos como `.write()` o `.read()` dentro del bloque.
    
3. **La Sangría (Indentación):** Todo lo que esté alineado hacia la derecha dentro del `with` tiene acceso al archivo. En cuanto pones una línea de código sin sangría al extremo izquierdo, el archivo ya se cerró.


## ⚠️ Errores Comunes y Soluciones

Al trabajar con `with` y archivos, estos son los dolores de cabeza más habituales:
### 1. `ValueError: I/O operation on closed file.`

- **¿Por qué ocurre?:** Intentaste leer o escribir en el archivo (usando el alias) _fuera_ del bloque `with` (cuando ya se había cerrado).
    
- **❌ Código Incorrecto:**
![[Pasted image 20260603215628.png]]

* **✔️ Solución:** Mete la línea de código dentro de la sangría del `with`.


### 2. `NameError: name 'archivo' is not defined`
* **¿Por qué ocurre?:** Te saltaste el paso de bautizar el archivo con la palabra clave `as`. * **❌ Código Incorrecto:**
![[Pasted image 20260603215754.png]]

- **✔️ Solución:** Asegúrate de escribir `as nombre_variable` al final de la línea del `with`.
    

### 3. Borrado Accidental de Datos

- **¿Por qué ocurre?:** Usar el modo `"w"` (_Write_) abre el archivo, pero **elimina todo lo que existía dentro de él** antes de escribir lo nuevo. No es un error de letras rojas, sino un error de lógica.
    
- **✔️ Solución:** Si lo que quieres es _añadir_ texto al final de un archivo sin borrar lo que ya tiene, debes cambiar el modo `"w"` por el modo `"a"` (_Append_ / Adjuntar).


# 📑 Apunte de Obsidian: Escritura Óptima de Archivos (Ciclos y Métodos)

Cuando manejamos volúmenes grandes de datos (como una lista de jugadores), no escribimos línea por línea. Automatizamos el proceso combinando el bloque `with` con estructuras de repetición.

## 🎯 ¿Para qué sirve? (Información Importante)

Permite volcar colecciones enteras de datos (Listas o Diccionarios) directamente en un archivo de texto utilizando pocas líneas de código, manteniendo el programa rápido y fácil de mantener.

## 🛠️ Opción 1: La forma Dinámica (Ciclo `for` + `.write()`)

Esta es la mejor opción porque toma una lista normal de Python y, mientras va leyendo a cada jugador, ella solita le pega el `\n` antes de meterlo al archivo.

### 📋 Código de Ejemplo:

![[Pasted image 20260603221244.png]]

## ⚡ Opción 2: La forma Ultra-Rápida (El método `.writelines()`)

Python tiene un método hermano de `.write()` llamado **`.writelines()`** (en plural). Este método acepta una lista completa de golpe.

> ⚠️ **Norma Importante de `.writelines()`:** Este método **NO** añade los saltos de línea por sí solo. Si le pasas la lista limpia, los va a amontonar todos. Para usarlo de forma óptima, se suele combinar con una "compresión de listas" para añadir el `\n` en una sola línea de código.

### 📋 Código de Ejemplo:

![[Pasted image 20260603221318.png]]

## ⚠️ Errores Comunes y Soluciones en Automatización

### 1. `TypeError: write() argument must be str, not list`

- **¿Por qué ocurre?:** Intentaste pasarle una lista completa al método `.write()` individual.
    
- **❌ Código Incorrecto:** `archivo.write(["Kobe", "LeBron"])`
    
- **✔️ Solución:** Si vas a pasar una lista completa de golpe, cambia el método a `.writelines()`. Si usas `.write()`, debes meterlo dentro de un ciclo `for`.
    

### 2. El último renglón queda vacío

- **¿Por qué ocurre?:** Al usar `jugador + "\n"` adentro del `for`, el último jugador también recibe un "Enter", dejando una línea en blanco al final del archivo de texto.
    
- **✔️ Solución:** Por lo general, en archivos de datos esto no es un problema. Pero si necesitas que quede perfecto, la Opción 1 es la más fácil de adaptar con un `if` para controlar el último elemento.

# 📑 Apunte de Obsidian: Lectura de Archivos en Python

La lectura de archivos nos permite recuperar datos almacenados permanentemente en el disco duro (como listas de jugadores, configuraciones o registros) y cargarlos en la memoria del programa para procesarlos.

## 🎯 ¿Para qué sirve? (Información Importante)

Al igual que para escribir, usamos la estructura segura `with open()`, pero esta vez cambiamos el modo a **`"r"`** (_Read_, que significa leer en inglés). Al leer un archivo, Python nos ofrece diferentes métodos dependiendo de si queremos todo el texto junto o separado línea por línea.

## ⚙️ Características y Métodos de Lectura

Python tiene tres herramientas principales para extraer la información. Cada una tiene un comportamiento único:

### 1. El método `.read()` (Todo de golpe)

Lee absolutamente todo el contenido del archivo y lo transforma en un **único String (texto largo)**, incluyendo los saltos de línea invisibles.

- **Ideal para:** Archivos cortos o cuando solo quieres mostrar el contenido en pantalla idéntico a como está en el bloc de notas.
    

### 2. El método `.readlines()` (Convertir en Lista)

Lee el archivo completo, pero **lo divide línea por línea y te devuelve una Lista de Python**. Cada renglón del archivo se convierte en un elemento de la lista.

- **Ideal para:** Volver a meter datos masivos (como tu lista de jugadores) dentro de una estructura limpia de Python para usarla con ciclos `for`.
    
- _Nota:_ Los elementos de la lista mantendrán el carácter `\n` al final de cada renglón.
    

### 3. El ciclo `for` directo sobre el archivo (Línea por línea eficiente)

En lugar de cargar todo el archivo en la memoria ram de golpe, puedes recorrer el archivo directamente con un `for`.

- **Ideal para:** Archivos gigantescos (de miles de líneas) porque lee un renglón, lo procesa, lo borra de la memoria y pasa al siguiente.
    

## 🚦 Normas y Sintaxis Básica

El modo por defecto de `open()` es precisamente `"r"`. Si no pones ninguna letra, Python asumirá que vas a leer. Sin embargo, por buena práctica siempre se escribe de forma explícita:
![[Pasted image 20260605181408.png]]

## ⚠️ Errores Comunes y Soluciones

Al leer archivos, el más mínimo error en el nombre o la ubicación romperá el código. Aquí están los fallos típicos:

### 1. `FileNotFoundError: [Errno 2] No such file or directory`

- **¿Por qué ocurre?:** Es el error más común de todos. Ocurre cuando le pides a Python que lea un archivo que **no existe** en esa carpeta o escribiste mal el nombre (ej. pusiste `campeon.txt` en lugar de `campeones.txt`).
    
- **✔️ Solución:** Asegúrate de que el archivo esté exactamente en la misma carpeta desde donde estás corriendo tu terminal o usa una ruta completa. También puedes proteger este código con un escudo **`try/except FileNotFoundError`** que aprendiste en [[04_Manejo de Errores]].
    

### 2. Texto con espacios vacíos extraños al imprimir

- **¿Por qué ocurre?:** Si usas `.readlines()` o un ciclo `for`, cada renglón trae consigo el "Enter" invisible (`\n`). Si usas `print()`, que por defecto añade su propio salto de línea, tus datos se verán con un renglón en blanco de separación.
    
- **✔️ Solución:** Usa el método de texto `.strip()` al imprimir. Este método limpia los espacios y los `\n` que estén a las orillas del texto.


![[Pasted image 20260605181456.png]]

# 📑 Apunte de Obsidian: El Modo Append en Python

El modo Append (añadir o adjuntar) permite abrir un archivo existente y colocar el puntero de escritura **al final de todo el texto**, garantizando que los datos viejos no se borren y los nuevos se agreguen abajo.

## 🎯 ¿Para qué sirve? (Información Importante)

A diferencia del modo `"w"` (que destruye el archivo anterior para crear uno en blanco), el modo **`"a"`** respeta el contenido actual. Es el modo que se utiliza en el mundo real para crear **Logs** (registros de eventos de un sistema), bitácoras o listas dinámicas que crecen con el tiempo.

## 🚦 Normas y Sintaxis Básica

La estructura es idéntica a las anteriores, lo único que cambia es la letra del modo a **`"a"`**:
![[Pasted image 20260606170559.png]]

### 🔍 Comportamiento según el escenario:

1. **Si el archivo YA existe:** Abre el archivo sin borrar nada, se posiciona en el último carácter y escribe lo nuevo.
    
2. **Si el archivo NO existe:** Se comporta como el modo `"w"`; crea el archivo desde cero y le mete el texto.
    

## ⚠️ Errores Comunes y Soluciones

### 1. Texto pegado al último elemento viejo

- **¿Por qué ocurre?:** Si el último elemento que escribiste ayer en tu archivo no tenía un salto de línea (`\n`) al final, el modo `"a"` empezará a escribir exactamente en ese mismo renglón, dejando los datos amontonados.
    
- **❌ Resultado visual:** `Anthony DavisD'Angelo Russell`
    
- **✔️ Solución:** Asegúrate de que **siempre** que uses `.write()`, tu texto termine con `\n`, para que el archivo quede "preparado" con un renglón abajo listo para recibir más información en el futuro.

## 🛡️ Combinando `with` y `try/except` (Código a Prueba de Balas)

Aunque el bloque `with` cierra el archivo automáticamente, no puede evitar que ocurran errores externos mientras el archivo está abierto (por ejemplo, que el disco duro se llene, que no tengas permisos de administrador para escribir en esa carpeta, o que borren el archivo mientras se procesa).

Para evitar que tu programa explote con letras rojas en la terminal de CachyOS, envolvemos el bloque `with` dentro de un `try/except`.

### 📋 El Código Blindado:

Modifica tu archivo `Registro_Completo.py` para que quede con esta estructura:
![[Pasted image 20260606171313.png]]

### 🧠 ¿Por qué es una buena práctica?

- Si Python no puede abrir el archivo por problemas del sistema operativo, el programa no se va a congelar; en su lugar, saltará limpiamente al bloque `except` y te dará un mensaje amigable en español.
    
- El `print` de éxito ahora solo se ejecuta si el bloque `with` terminó correctamente, asegurando que no le mientas al usuario.
    

¡Pégalo en tu editor, dale una última calada corriendo el código en tu terminal y ya tienes el tema de manejo de archivos completamente dominado de inicio a fin, bro!