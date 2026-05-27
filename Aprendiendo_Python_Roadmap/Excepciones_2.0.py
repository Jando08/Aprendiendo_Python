"""
Abre un bloque try.
Dentro del try, pídele al usuario dos datos:
El gasto total del viaje float, guardado en gasto_total.
El número de amigos entre los que se va a dividir la cuenta int, guardado en numero_amigos.
Calcula dividiendo gasto_total / numero_amigos. Guarda una variable llamada cuota_individual.
Muestra: "A cada persona le toca pagar ${cuota_individual} pesos."
Manejo de Errores (Aquí viene lo nuevo): Vas a agregar dos bloques except seguidos para atrapar los dos posibles problemas:
except ValueError: Si el usuario mete letras en lugar de números, debe asignar al mensaje: "Error: Debes ingresar valores numéricos válidos."
except ZeroDivisionError: Si el usuario mete un 0 en el número de amigos, la matemática explota porque no se puede dividir entre cero."Error: El número de amigos no puede ser cero."
"""

try:
    gasto_total = float(input("Ingresa el gasto total de tu viaje: $ "))
    numero_amigos = int(input("Ingresa el numero total de amigos que realizaro el viaje: "))

    # Calculo de cuota individual
    cuota_individual = gasto_total / numero_amigos
    mensaje = f'A cada persona le toca pagar ${cuota_individual} pesos'
except ValueError:
    mensaje = 'Error: Debes ingresar valores numéricos válidos.'
    
    # Si ingresa 0 en cantidad amigos
except ZeroDivisionError:
    mensaje = 'Error: El número de amigos no puede ser cero.'


# Imprimir mensaje final
print(mensaje)