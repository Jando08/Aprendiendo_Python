# 📁 Manejo de Archivos (`.txt`) 
Permite la persistencia de datos, es decir, guardar la información de manera permanente en el disco duro. 
## ✍️ Escribir Archivos con `with open()`
Usamos la estructura moderna `with` para que Python cierre el archivo automáticamente al terminar y no se corrompa. * El modo `"w"` (*Write*) crea el archivo o sobrescribe todo su contenido. * El comando `\n` se usa para hacer saltos de línea (un Enter).

```python
 with open("mvp_lakers.txt", "w") as archivo: archivo.write("Jugador: Kobe Bryant\n") archivo.write("Premios: 5 veces Campeón de la NBA")