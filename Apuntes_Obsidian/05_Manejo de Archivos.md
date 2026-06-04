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

