La **Programación Orientada a Objetos (POO)** no es un comando nuevo de Python; es un **paradigma de programación**. Esto significa que es un chip mental, una forma diferente de pensar y estructurar tu código para modelar cosas del mundo real dentro de la computadora.

Hasta ahora, has programado de forma **Procedimental** (un script que se lee de arriba a abajo, con variables sueltas y funciones que reciben datos). El problema es que en el mundo real las cosas tienen características y acciones al mismo tiempo. La POO une esas dos cosas en una sola estructura.

## 🏛️ 1. Los Dos Conceptos Clave: El Molde y el Producto

Para entender la POO, tienes que dominar dos palabras que vas a usar el resto de tu vida como desarrollador:

- **La Clase (El Molde):** Es el plano arquitectónico, el molde de galletas o la plantilla. La Clase no es un objeto real; es solo la definición de qué propiedades y qué acciones va a tener algo. Por ejemplo, la clase `Auto` dice que todos los autos tienen un color, una marca y pueden acelerar.
    
- **La Instancia / Objeto (El Producto):** Es el objeto real creado a partir del molde. Usando el molde `Auto`, puedes crear una instancia real llamada `mi_coche` que sea de color negro y marca HP, y otra instancia llamada `tu_coche` que sea gris y marca MSI.
    

## 🚀 2. ¿Por qué es vital? (Importancia Real)

Si estás desarrollando un videojuego en **Godot**, la POO es el aire que respiras. En Godot, cada personaje, cada enemigo, cada bala y cada barra de vida es un **Objeto** que nace de una **Clase** (o Nodo).

La POO es vital por tres razones:

1. **Organización Modular:** En lugar de tener variables sueltas como `jugador1_nombre`, `jugador1_vida`, `jugador2_nombre`, `jugador2_vida`... creas un objeto `Jugador` que encapsula todo por dentro.
    
2. **Abstracción del mundo real:** Te permite mapear la realidad directamente al código. Si necesitas un sistema para la escuela, creas la clase `Alumno` (con matrícula, nombre, promedio) y la clase `Materia`.
    
3. **Mantenibilidad:** Si quieres que todos los personajes de tu juego ahora tengan una nueva habilidad, no modificas 20 funciones; solo agregas la acción en la Clase principal y en automático todos los personajes del juego la aprenden.
    

## 💥 3. Los Cuatro Pilares del Paradigma

La POO se sostiene sobre cuatro pilares teóricos fundamentales. Hoy solo los vamos a mencionar para que los tengas en el radar, pero los iremos desmenuzando paso a paso:

1. **Encapsulamiento:** Es ocultar los datos internos de un objeto para que nadie desde afuera los pueda modificar por accidente. Es como el motor de tu laptop: está protegido por la carcasa y solo interactúas con el teclado.
    
2. **Abstracción:** Ocultar la complejidad interna y solo mostrar lo que es necesario. Tú usas el método `.lower()` en un string sin necesidad de saber cuántas operaciones binarias hace el procesador por detrás.
    
3. **Herencia:** Crear una clase nueva a partir de una que ya existe. Por ejemplo, puedes tener la clase `Enemigo` y crear una subclase llamada `JefeFinal` que herede todo lo de `Enemigo` pero con más vida y ataques especiales.
    
4. **Polimorfismo:** La capacidad de que diferentes objetos respondan al mismo comando de formas distintas. Si tienes la clase `Perro` y la clase `Gato`, ambos tienen la acción `hacer_sonido()`, pero uno va a ladrar y el otro va a maullar.
    

## ⚠️ 4. El peor error al empezar POO: El método `__init__` y el fantasma de `self`

Cuando veamos el código, notarás que dentro de las clases siempre se escribe una función especial llamada `__init__` y una palabra rara llamada `self`. El 90% de los estudiantes reprueba o se confunde aquí:

- **El Error:** Pensar que `self` es una palabra mágica de Python.
    
- **La Realidad:** `self` es una variable que representa **al objeto específico que se está creando en ese preciso momento**. Si estás creando al jugador Austin Reaves, `self.nombre` significa "el nombre de Austin". Si estás creando a LeBron, `self.nombre` significa "el nombre de LeBron". Es la forma en que el molde sabe a qué galleta le está poniendo el chispazo de chocolate.

## 🛠️ La Anatomía de una Clase en Python

Para crear una clase usamos la palabra clave `class`. Por convención en la ingeniería de software, los nombres de las clases siempre empiezan con **Mayúscula** (formato _CamelCase_).

Mira fijamente este código base. No te preocupes, ahorita lo desglosamos línea por línea:

![[Pasted image 20260611093527.png]]

## 🔬 Desglose de la Sintaxis (¿Qué demonios significa cada cosa?)

### 1. El Método Especial `__init__` (El Constructor)

Este método lleva **doble guion bajo** al principio y al final (`__init__`). Python lo ejecuta en automático **únicamente cuando creas el objeto**. Su único trabajo en la vida es recibir los datos iniciales y guardarlos dentro del objeto.

### 2. El misterio de `self`

Fíjate cómo todas las funciones adentro de la clase llevan `self` como primer parámetro.

- `self` significa **"este objeto"**.
    
- Al escribir `self.nombre = nombre`, le estás diciendo a Python: _"Toma el nombre que me pasaron por el paréntesis y guárdalo permanentemente en la propiedad 'nombre' de **este** jugador específico"_.
    

### 3. Atributos vs Métodos

- **Atributos (Variables de la clase):** Son los datos, las características (`self.nombre`, `self.numero`).
    
- **Métodos (Funciones de la clase):** Son las acciones que el objeto puede realizar (`encestar_canasta()`).
    

## 🏗️ Cómo usar el molde: Crear la Instancia

Una vez que definiste la clase (el molde), crear un objeto real es ridículamente sencillo. Solo llamas a la clase como si fuera una función y le pasas los datos **sin el self** (Python mete el `self` solito por debajo del agua).

Aquí tienes el script completo de cómo se crean y se usan los objetos:

![[Pasted image 20260611093615.png]]

## 🔍 Datos clave de la Sintaxis para observar:

- Fíjate en el punto 4: Cuando `jugador_a` sumó puntos, los puntos de `jugador_b` se quedaron en `0`. Eso demuestra que **cada objeto es completamente independiente**, aunque hayan salido del mismo molde. Tienen sus propias celdas de memoria RAM separadas.
    
- Para usar un atributo o un método desde afuera del molde, siempre usas la nomenclatura del punto: `objeto.atributo` o `objeto.metodo()`.
    

Pásate este bloque de sintaxis bien estructurado a tu Obsidian, bro. Analiza cómo el `__init__` acomoda las piezas y cómo los métodos usan `self` para saber a quién le están sumando los puntos.


## Ejercicio Organizador de Tareas

![[Pasted image 20260611170158.png]]

## 🔒 ¿Qué es el Encapsulamiento?

Imagina que compras un coche del año. Tú, como conductor, tienes una interfaz pública para interactuar con él: el volante, los pedales, la pantalla táctil. Pero, ¿a poco el fabricante te deja mover los pistones del motor con la mano mientras manejas? ¡Claro que no! Todo eso viene sellado bajo el cofre para evitar que un usuario cometa un error y destruya el sistema.

En programación es **exactamente lo mismo**. Hasta ahora, todos los atributos que creábamos eran **públicos**. Cualquiera podía venir desde fuera del objeto y destruirte los datos haciendo algo como `mi_carrito.total_a_pagar = -999999`.

El **Encapsulamiento** es la acción de **ocultar o proteger los datos internos** de un objeto para que nadie los pueda modificar directamente por accidente. La única forma de verlos o cambiarlos será a través de métodos seguros que tú mismo vas a programar.

## 🛠️ ¿Cómo se hace en Python? (Los Atributos Privados)

A diferencia de otros lenguajes de programación donde usas palabras raras como `private`, en Python somos más prácticos. Para hacer que un atributo sea **privado** (secreto y protegido), solo tienes que ponerle **dos guiones bajos (`__`)** al principio de su nombre.

![[Pasted image 20260612080106.png]]

¿Viste eso? Al ponerle `__saldo`, Python blinda la variable. Si alguien intenta hackear el saldo desde fuera escribiendo `cuenta.__saldo = 1000000`, Python simplemente lo va a ignorar o va a tronar, protegiendo el dinero del usuario.

## 🚪 ¿Cómo entramos a un atributo privado? (Getters y Setters)

Si el atributo está bajo llave, ¿cómo hacemos para que el usuario pueda ver su saldo o retirar dinero? Usamos **métodos especiales** que funcionan como los guardias de seguridad de la caja fuerte:

1. **Getter (Obtener):** Un método público que sirve únicamente para _leer_ el valor del atributo privado.
    
2. **Setter (Establecer):** Un método público que sirve para _modificar_ el valor, pero aplicando validaciones (filtros) antes de guardarlo.
    

### 💻 El código completo de una clase encapsulada:

![[Pasted image 20260612080143.png]]

## Ejercicio Real

![[Pasted image 20260612082749.png]]

### 🗂️ La Plantilla Sagrada de `@property`

Para que nunca te pierdas, grábate este mapa mental de cómo se estructura la sintaxis. El truco es que **el Getter y el Setter se llaman exactamente igual**, lo único que cambia es la etiqueta (decorador) de arriba:
![[Pasted image 20260612085721.png]]


## 🧬 ¿Qué es la Herencia en programación?

En la vida real, tú heredas rasgos de tus padres (el apellido, el color de ojos, o ciertas habilidades). En la programación es exactamente igual: **La Herencia permite que una clase nueva adopte los atributos y métodos de una clase que ya existe.**

¿Para qué hacemos esto? Para cumplir la regla de oro del programador: **DRY** (_Don't Repeat Yourself_ o No te repitas a ti mismo). En lugar de escribir el mismo código cinco veces para cinco objetos similares, creas una clase "Padre" con lo básico, y luego las clases "Hijas" le heredan todo lo que tiene, ahorrándote cientos de líneas de código.

## 🧱 El problema de no usar Herencia

Imagina que estás desarrollando un videojuego (por ejemplo, en Godot o puro Python). Tienes dos tipos de personajes: un **Guerrero** y un **Mago**.

Si lo hicieras a la antigüita, tendrías que escribir esto:
![[Pasted image 20260615065649.png]]

Fíjate cómo el `nombre`, la `vida` y el método `caminar` son **idénticos** en ambas clases. Si después quieres cambiar cómo caminan los personajes, ¡tendrías que modificar el código en las dos clases por separado! Qué hueva, ¿no?

## 🚀 La Solución: Creando la Clase Padre

Con **Herencia**, primero creamos una clase general (el Padre o Súperclase) que contenga lo que todos tienen en común:
![[Pasted image 20260615065718.png]]

## 🐣 ¿Cómo se hereda en Python? (`super()`)

Para hacer que una clase sea hija de otra, simplemente **ponemos el nombre de la clase padre entre paréntesis** al momento de definir la clase hija.

Además, usamos una función mágica llamada **`super().__init__()`**. Esto le dice a Python: _"Oye, ve con mi padre y ejecuta su constructor primero para que él guarde el nombre y la vida, y yo me encargo de lo mío"_.

### 💻 Mira la magia en código:
![[Pasted image 20260615065743.png]]

## 📝 La Regla de Oro de los Paréntesis en Python

### 1. Métodos con `@property` (NO llevan paréntesis ❌)

Cuando le pones la etiqueta `@property` arriba a un método, **le estás quitando los paréntesis a la fuerza**.

¿Por qué? Porque `@property` transforma un método para que se comporte como si fuera un **atributo o variable fija**. El usuario solo quiere "ver" o "asignar" el dato, no quiere ejecutar una acción.

- **Para leer:** `print(objeto.mensualidad)`
    
- **Para modificar:** `objeto.mensualidad = 500`
    

### 2. Métodos Tradicionales / Acciones (SÍ llevan paréntesis ✅)

En el código de hoy (con `calcular_pago()` o `encender()`), **no usamos la etiqueta `@property`**. Son métodos tradicionales.

En Python, los paréntesis `()` significan **"¡CORRE O EJECUTA ESTA ACCIÓN AHORA MISMO!"**.

- `calcular_pago()` no es una variable guardada; es un bloque de código que tiene que hacer matemáticas (sumar el sueldo + el bono) justo en ese segundo.
    
- Si no le pones los `()`, Python no corre la operación; solo te diría en qué parte de la memoria RAM está guardada la función.
    

## 💡 El acordeón para tu Obsidian (Visual)

Míralo con este mapa mental rápido:

- **¿Tiene `@property`?** ➡️ Es un estado/atributo. **NO** lleva `()`.
    
- **¿Es un método normal (hace una acción)?** ➡️ Es una orden/operación. **SÍ** lleva `()`.
    

Por eso hoy escribiste `empleado_1.calcular_pago()`, porque le estabas dando la orden al objeto de sacar la calculadora y ponerse a chambear.

## 🧬 ¿Qué es el Polimorfismo?

La palabra viene del griego _Poli_ (muchas) y _Morfismo_ (formas). En programación, significa **la capacidad de tratar a diferentes objetos de la misma manera, y que cada uno responda a su propia forma.**

Imagina que tienes una lista en Python llena de canciones y efectos de sonido (algunos normales y otros retro). En lugar de ir preguntando uno por uno de qué clase son, el Polimorfismo te permite meterlos a todos en un ciclo `for` y gritarle a la lista: **`¡.reproducible()!`**.

Python, de manera automática e inteligente, va a ejecutar el método del padre para los sonidos normales, y el método sobreescrito para los sonidos retro. Tú solo escribes una línea de código, y el programa maneja las "muchas formas" por sí solo.

## 💻 Mira el Polimorfismo en acción

Vamos a usar las mismas clases que acabas de corregir. Mira cómo los metemos a todos al mismo saco (una lista) y los ponemos a chambear con un solo ciclo:
![[Pasted image 20260615080415.png]]

🕹️ Lo que imprime la terminal:
![[Pasted image 20260615080445.png]]

En Python, usamos **`super()`** cuando una clase hija quiere **llamar a su clase padre** para reutilizar su código en lugar de volverlo a escribir desde cero.

Lo usamos principalmente en dos situaciones muy específicas, y aquí tienes el resumen exacto para que lo dejes grabado en tu Obsidian:

## 🔑 Los 2 momentos para usar `super()`

### 1. En el Constructor (`__init__`) ➡️ Para heredar atributos

Se usa para heredar los datos básicos que el padre ya sabe cómo guardar (como el `nombre`, la `marca` o el `archivo`). Al usarlo, te ahorras tener que escribir `self.nombre = nombre` en todas las clases hijas.

- **Ejemplo:**
![[Pasted image 20260615082158.png]]

### 2. En la Sobreescritura de Métodos ➡️ Para SUMAR comportamiento

Se usa cuando la clase hija quiere hacer **lo mismo que hacía el padre, pero añadiendo un extra**. En lugar de borrar lo que hacía el padre, primero lo ejecutas con `super()` y abajo le pones las líneas nuevas de la hija.

- **Ejemplo:**
![[Pasted image 20260615082230.png]]

## 🚫 ¿Cuándo NO se usa `super()`?

No lo usas cuando quieres que la clase hija **reemplace por completo** la acción del padre (como en el ejercicio corto de las notificaciones que te acabo de dejar). Si el padre dice _"Enviando notificación genérica..."_ pero tú solo quieres que se vea _"📧 Email enviado..."_, simplemente **no pones `super()`** en el método de la hija y listo.


# Martes 16 de Junio del 2026

## 🎭 ¿Qué es la Abstracción?

En el mundo real, tú usas la abstracción todos los días sin darte cuenta. Piensa en tu laptop o en un carro: para manejar un carro, tú solo necesitas saber cómo usar el volante, el acelerador y el freno. **No necesitas ser un ingeniero mecánico** ni saber exactamente cómo interactúan los pistones con la gasolina dentro del motor para poder llegar a tu destino.

En programación es exactamente lo mismo: **La Abstracción consiste en ocultar los detalles complejos de cómo funcionan las cosas por dentro y mostrarle al usuario (o a ti mismo en el futuro) solo las herramientas esenciales que necesita usar.**

## 🛠️ ¿Cómo se aplica en Python? (Clases Abstractas)

Para aplicar la abstracción en Python, usamos algo llamado **Clases Abstractas**. Imagina que una clase abstracta es como un **contrato obligatorio** o una "plantilla" de la cual nadie puede crear un objeto directamente, pero que obliga a todas las clases hijas a tener ciertos métodos sí o sí.

Para hacerlo, Python nos pide importar una herramienta del sistema llamada `abc` (_Abstract Base Classes_).

### 💻 Mira la sintaxis básica en código:

Imagina que estás diseñando un sistema para diferentes tipos de **Bases de Datos** (PostgreSQL, MySQL, etc.). Todas las bases de datos se deben conectar y desconectar, pero cada una lo hace con código interno muy diferente. Creamos la plantilla abstracta:

![[Pasted image 20260616093723.png]]

> ⚠️ **Regla de oro de la Abstracción:** Si tú intentas hacer `db = BaseDeDatos()`, Python te va a lanzar un tremendo error en la terminal. Las clases abstractas **no se pueden instanciar** (no puedes crear objetos de ellas). Solo sirven para ser heredadas.

## 🐣 Obligando a las clases hijas a cumplir el contrato

Ahora, si creas la clase para **PostgreSQL**, estás obligado a escribir los métodos `conectar` y `desconectar`. Si se te olvida poner alguno, Python va a bloquear el programa y no te va a dejar avanzar. Esto asegura que tu código sea ultra ordenado y que nunca se te pase programar una función vital.

![[Pasted image 20260616093750.png]]


## 🔍 ¿Qué demonios significa cada parte?

En Python, cada vez que corres un archivo, el sistema crea unas variables ocultas por detrás. Una de ellas se llama `__name__` (con doble guion bajo).

Esta variable guarda el nombre de **cómo se ejecutó el archivo**. Hay dos sopas:

### 1. Si corres el archivo directamente en tu terminal (`python mi_script.py`)

Python dice: _"Ok, el usuario le dio play directamente a este archivo"_. Por lo tanto, de forma automática, le asigna el valor de `"__main__"` (que significa "principal") a esa variable oculta.

- La condición se cumple: `__name__ == "__main__"` es **Verdadero** (True) y todo lo que esté adentro de ese `if` **se ejecuta**.

### 2. Si IMPORTAS el archivo dentro de otro (`from mi_script import MiClase`)

Imagina que mañana estás programando un juego principal y traes tus consolas importando el archivo. Python dice: _"Ojo, este archivo solo lo están usando como biblioteca o pieza de rompecabezas, no lo corrieron directamente"_. Por lo tanto, el valor de `__name__` ya no es `"__main__"`, sino el nombre del archivo (ej. `"consolas_abstraccion"`).

- La condición **NO** se cumple y todo lo que esté adentro del `if` **se ignora por completo**.
    

## 💡 ¿Por qué es útil? (El problema que evita)

Imagina que en tu archivo de las consolas dejas las pruebas de `switch_jando.encender_consola()` sueltas hasta abajo, sin el `if`.

## 📝 El resumen para tus notas

- **¿Para qué sirve?** Para separar el código que define tus herramientas (clases, funciones) del código que hace las pruebas (crear objetos, prints).
    
- **¿Cuándo se ejecuta?** Solo cuando ejecutas ese archivo específico de forma directa en la consola.
    
- **¿Cuándo se ignora?** Cuando ese archivo es importado por otro script.
    

Es como el control de calidad de tus archivos, bro. Así mantienes tus clases reutilizables en cualquier parte de tu sistema sin arrastrar "basura" de prints viejos.


