## 🔢 ¿Qué es NumPy y por qué es el rey de los Datos?

En Python normal, cuando quieres guardar una lista de datos (como las edades de 1 millón de clientes), usas una lista común: `[20, 25, 30]`. El gran problema es que las listas de Python son **muy lentas** y consumen mucha memoria RAM porque Python tiene que revisar, elemento por elemento, qué tipo de dato es.

NumPy introduce una estructura llamada **ndarray** (Arreglo Multidimensional o simplemente Arreglo). Los arreglos de NumPy tienen dos superpoderes que le vuelven la vida fácil a un Data Scientist:

1. **Velocidad Brutal:** Están programados en código C por debajo. Pueden hacer millones de operaciones matemáticas en un parpadeo.
    
2. **Vectorización (Operaciones en Bloque):** Olvídate de los ciclos `for`. Si tienes una lista de precios en NumPy y les quieres sumar un impuesto de `$5`, simplemente escribes `precios + 5` y NumPy se lo suma a todas las filas de un solo golpe.

## 📈 Siguiente paso con NumPy: Filtrado de Datos (Máscaras Booleanas)

Ya que sabes hacer operaciones matemáticas en bloque, la siguiente habilidad vital para un Data Scientist es **saber filtrar información sin usar `if` ni `for`**.

Imagina que de ese arreglo de pesos mexicanos (`[2700, 9000, 21600, 54000]`), tu jefe te dice: _"Alejandro, necesito que me extraigas únicamente los presupuestos que sean mayores a $10,000 pesos"_.

En NumPy esto se hace con algo llamado **Máscaras Booleanas**. Mira qué fácil:
![[Pasted image 20260618213814.png]]


## 📉 Siguiente nivel con NumPy: Estadísticas Rápidas

Ya sabes transformar datos en bloque y ya sabes filtrarlos. Ahora toca el tercer y último superpoder básico de NumPy que necesita un _Data Scientist_: **Las Funciones Estadísticas**.

Olvídate de hacer ecuaciones complejas a mano o bucles para sumar. NumPy ya trae funciones optimizadas en C para sacar métricas de tus arreglos en un milisegundo.

Mira estas cuatro herramientas que se usan del diario:

- `np.sum(arreglo)` -> Suma todos los elementos.
    
- `np.mean(arreglo)` -> Saca el promedio matemático (la media).
    
- `np.max(arreglo)` -> Encuentra el valor más alto.
    
- `np.min(arreglo)` -> Encuentra el valor más bajo.


## 🧭 Tu Algoritmo Mental para NumPy 

Para que cierres esta carpeta con broche de oro, guarda este acordeón rápido en tus notas. Cada vez que vayas a manipular datos numéricos con NumPy, acuérdate de estos tres pasos:

1. **Transformar (`Arreglo * X`):** Modificas millones de datos al mismo tiempo sin usar bucles.
    
2. **Filtrar (`Arreglo[Arreglo > X]`):** Creas una máscara de verdaderos/falsos para aislar solo los datos que te importan.
    
3. **Resumir (`np.sum()`, `np.mean()`):** Reduces todo tu volumen de datos a métricas clave que tu jefe pueda entender de un solo vistazo.


