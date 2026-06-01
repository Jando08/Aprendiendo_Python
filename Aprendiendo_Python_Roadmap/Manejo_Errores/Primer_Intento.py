edad_usuario = 'Veinticinco'

try:
    edad_numero = int(edad_usuario)
    print(f'EL proximo a;o tendras {edad_numero + 1} a;os')
except:
    print(f'Error: Por favor, ingresa un numero valido en lugar de letras')

print('Fin del proceso')