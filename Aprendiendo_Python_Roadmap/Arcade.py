"""
Pídele al usuario su edad usando input() y conviértela a un número entero.edad.
Pídele al usuario su tipo de boleto usando input()"Ingresa tu tipo de boleto (VIP / General): ".tipo_boleto.
Escribe una estructura condicional que evalúe lo siguiente:
Regla 1 (Menores de edad): Si la edad es menor a 18, no importa qué boleto tenga, el acceso está denegado. Debe imprimir: "Lo siento, eres menor de edad. Acceso denegado."
Regla 2 (VIP): Si es mayor o igual a 18 y su tipo_boleto es igual a "VIP", debe imprimir: "¡Bienvenido a la Zona VIP, Alejandro! Disfruta del show."
Regla 3 (General): Si es mayor o igual a 18 y su tipo_boleto es igual a "General", debe imprimir: "Acceso concedido. Bienvenido a la Zona General."
Regla 4 (Boleto inválido): Si es mayor de edad pero escribió cualquier otra cosa en el boleto (por ejemplo, "gratis" o un error de dedo), debe imprimir: "Boleto no válido. Por favor, revisa tu ticket."
"""

# Preguntar la edad al usuario y su tipo de boleto
nombre = input("Ingrese su nombre por favor: ")
edad = int(input("Ingrese su edad por favor: "))
tipo_boleto = input("Ingresa tu tipo de boleto (VIP / General): ")
mensaje = ''

# Mandar mensaje dependiendo de la condición
if edad < 18:
    mensaje = 'Lo siento, eres menor de edad. Acceso denegado'
elif tipo_boleto == 'VIP':
    mensaje = f'!Bienvenido a la zona VIP {nombre}! Disfruta del show'
elif tipo_boleto == 'General':
    mensaje = 'Acceso concedido. Bienvenido a la Zona General.'
else:
    mensaje = 'Boleto no válido. Por favor, revisa tu ticket.'



# Imprimir mensaje dependiendo del resultado
print(mensaje)
