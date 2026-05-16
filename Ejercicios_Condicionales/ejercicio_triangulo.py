#Clasificador de triangulos
#Pide al usuario la longitud de los tres lados de un triangulo (lados A, B y C)
#Si los tres lados son iguales, imprime "Equilatero"
#Si dos lados son iguales, imprime "Isoceles"
#Si los tres lados son iguales, imprime "Escaleno"

#pedimos al usuario que ingrese el valor de los 3 lados
print('Las medidas deben ser numero enteros')
lado_a = int(input('Ingrese la medida del lado a (cm): '))
lado_b = int(input('Ingrese la medida del lado b (cm): '))
lado_c = int(input('Ingrese la medida del lado c (cm): '))
mensaje = ''

#validamos
if lado_a == lado_b == lado_c:
    mensaje = 'El triangulo es Equilatero'
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    mensaje = 'El triangulo es Isoceles'
else:
    mensaje = 'El triangulo es Escaleno'

#imprimimos mensaje
print(mensaje)