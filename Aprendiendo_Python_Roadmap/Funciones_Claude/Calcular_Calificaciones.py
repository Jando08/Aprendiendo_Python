def promedio(calificaciones):
    total_materias = len(calificaciones)
    promedio = sum(calificaciones) / total_materias
    return promedio

def aprobo(calificaciones):
    resultado = promedio(calificaciones)
    if resultado >= 60:
        return True
    else:
        return False
    
notas = [80, 90, 70, 60, 55]
print(promedio(notas))
print(aprobo(notas))

notas2 = [40, 50, 30, 45]
print(promedio(notas2))
print(aprobo(notas2))



