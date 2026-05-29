intentos_fallidos = [2, 1, 6, 0, 12, 4, 8]

alerta_criticas = 0

for intento in intentos_fallidos:
    if intento >= 5:
        print(f'ALERTA: Usuario con {alerta_criticas} intentos fallidos.')
        alerta_criticas += 1


print(f'Reporte terminado. Total de alertas críticas detectadas: {alerta_criticas}')