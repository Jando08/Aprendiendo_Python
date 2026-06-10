# =====================================================================
# SCRIPT PRINCIPAL: main.py
# Responsabilidad: Interactuar con el usuario y orquestar el programa
# =====================================================================

# Importamos la función específica desde nuestro módulo local
from conversor import celsius_a_fahrenheit
from Seguridad import validad_largo
from logistica import calcular_envio
from limpiador import formatear_usuario

# EJERCICIO
entrada_usuario = input("Ingrese los grados Celsius que desea transformar: ")
grados_c = float(entrada_usuario)
grados_f = celsius_a_fahrenheit(grados_c)
print(f"El equivalente de {grados_c}°C es igual a: {grados_f}°F")

# EJERCICIO 2
password = input("Ingrese su contraseña por favor: ")
if validad_largo(password):
    print(f"Contraseña segura")
else:
    print("Contraseña insegura")

# EJERCICIO 3
total_carrito = float(input("Ingrese el total de su compra: "))
costo_envio = calcular_envio(total_carrito)
print(f'El total de su coste de envio es {costo_envio}')

# EJERCICIO 4
usuario = input("Ingrese su nombre de usuario: ")
nombre_limpio = formatear_usuario(usuario)
print(f"Tu nuevo nombre de usuario es: {nombre_limpio}")