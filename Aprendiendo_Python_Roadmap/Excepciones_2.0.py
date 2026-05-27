try:
    gasto_total = float(input("Ingresa el gasto total de tu viaje: $ "))
    numero_amigos = int(input("Ingresa el número total de amigos que realizaron el viaje: "))

    # Cálculo de cuota individual
    cuota_individual = gasto_total / numero_amigos
    mensaje = f"A cada persona le toca pagar ${cuota_individual} pesos."

except ValueError:
    mensaje = "Error: Debes ingresar valores numéricos válidos."

except ZeroDivisionError:
    mensaje = "Error: El número de amigos no puede ser cero."

# Imprimir mensaje final
print(mensaje)