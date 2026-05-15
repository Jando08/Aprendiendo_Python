#realizar un ejercico para indicar si un numero es par o impar

#pedir el numero
numero = int(input('Ingrese un numero:'))
mensaje = ''

#validamos que el numero no sea negativo
if numero < 0:
    mensaje = 'El numero debe ser positivo'
#sino es negativo
elif numero % 2 == 0:
    mensaje = f'El numero {numero} es par'    
else:
    mensaje = f'El numero {numero} es impar'

#imprimir el mensaje
print(mensaje)
