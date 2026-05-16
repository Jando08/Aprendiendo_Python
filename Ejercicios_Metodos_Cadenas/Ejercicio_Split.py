'''
Reto: Pide al usuario que ingrese su fecha de nacimiento en formato DD/MM/AAAA (ej: "15/08/2000"). 
Usa el separador adecuado para dividir el texto y luego imprime únicamente el año de nacimiento.
'''

#pedir al usuario fecha de nacimiento
fecha_nacimiento = '08/10/2005'

#convertir la fecha
fecha_convertida = fecha_nacimiento.split('/')

#imprimir solo el anio de nacimiento
print(fecha_convertida[2])

#OJO: para que funcione el split, debe ser una sola cadena de texto unida por diagonales
#ya sea escrita manualmente o user input()