'''
Reto: Crea un filtro de archivos de imagen. Pide al usuario el nombre de un archivo (ej: "foto.jpg" o "documento.pdf"). 
Si el archivo termina en ".jpg" o ".png", imprime "Archivo de imagen aceptado". 
De lo contrario, di "Formato no soportado".
'''

#pedir al usuario que ingrese el archivo
archivo = input('Ingrese el link del archivo: ')
mensaje = ''

#validad que los archivos terminen en .jpg o .png
if archivo.endswith('.jpg') or archivo.endswith('.png'):
    mensaje = 'Archivo de imagen aceptado'
else:
    mensaje = 'Formato no soportado'

#imprimir el resultado
print(mensaje)        