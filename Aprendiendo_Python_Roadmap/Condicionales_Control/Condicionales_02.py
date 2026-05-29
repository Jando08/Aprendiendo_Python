"""
Crea una variable llamada saldo_disponible y asígnale 5000
Usa input() para preguntarle al usuario: "¿Cuánto dinero deseas retirar?:"
Regla 1: Si el monto_retirar es mayor al saldo_disponible "Fondos insuficientes".
Regla 2: Si el monto_retirar es menor o igual al saldo_disponible, el retiro es exitoso. 
El programa debe: Calcular el nuevo saldo (restando el monto retirado al saldo disponible).
Mostrar el mensaje: "Retiro exitoso. Has retirado $[monto_retirar]. Tu nuevo saldo es de $[nuevo_saldo]"
"""

# creando las variables
saldo_disponible = 5000
mensaje = ""

# preguntar al usuario el retiro
monto_retirar = float(input("¿Cuánto dinero deseas retirar?: "))

# mandar mensaje dependiendo la condicion
if monto_retirar > saldo_disponible:
    mensaje = 'Fondos insuficientes'
else:
    nuevo_saldo = saldo_disponible - monto_retirar
    mensaje = f'Retiro exitoso, Has retirado ${monto_retirar}. Tu nuevo saldo es de ${nuevo_saldo} '

print(mensaje)