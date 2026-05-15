#hacer un programa que ingrese su edad y el programa indique si es mayor
#de edad o no

#ingresas la edad
edad = int(input('Ingrese su edad:'))
mensaje = ''


#hacemos la condicion para que mande el mensaje
if edad >= 18:
    mensaje = 'Eres mayor de edad'
else:
    mensaje = 'Eres menor de edad'

#imprimos el mensaje
print(mensaje)