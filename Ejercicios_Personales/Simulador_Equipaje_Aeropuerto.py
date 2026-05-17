# Pedirle el nombre al usuario y normalizarlo
nombre = input('Ingrese su nombre por favor: ')
nombre = nombre.capitalize()
print(f'Bienvenido {nombre}\n')

# Pedirle datos sobre boleto y peso de la maleta
tipo_boleto = input('Ingrese su tipo de boleto (Ejecutivo, Economico): ')
# Usamos capitalize para asegurar que empiece con Mayúscula siempre
tipo_boleto = tipo_boleto.capitalize()

peso_maleta = float(input('Ingrese el peso de su maleta en (KG): '))

mensaje = ''

# VALIDACIÓN PRINCIPAL
if tipo_boleto == 'Ejecutivo':
    if peso_maleta <= 32:
        mensaje = '¡Equipaje Ejecutivo aprobado sin costo extra!'
    else:
        mensaje = 'Maleta rechazada. Excede el peso máximo permitido para vuelo (32 kg).'

elif tipo_boleto == 'Economico': # CORREGIDO: Ya no dice 'Ecomico'
    if peso_maleta <= 23:
        mensaje = '¡Equipaje Economico aprobado sin costo extra!'
    # CORREGIDO: Usamos 'and' para que el peso deba cumplir AMBAS condiciones a la vez
    elif peso_maleta > 23 and peso_maleta <= 30:
        mensaje = 'Equipaje con sobrepeso. Debe pagar una tarifa de $50 USD.'
    else:
        mensaje = 'Maleta rechazada. Excede el límite de sobrepeso para clase económica.'

else:
    # Este es nuestro paracaídas si no escriben ni Ejecutivo ni Economico
    mensaje = 'Ingrese un tipo de boleto permitido por favor (Ejecutivo o Economico).'

print("\nResultado:", mensaje)