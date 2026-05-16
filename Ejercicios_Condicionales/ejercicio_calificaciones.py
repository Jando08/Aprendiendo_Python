#realizar un ejercico en el cual el usuario debe ingresar su calificacion
#Si la calificacion fue entre 9-10 debe de imprimir 'Excelente (A)'
#Si la calificacion fue entre 7-8 debe de imprimir 'Bien (B)'
#Si la calificacion fue 6 debe de imprimir 'Suficiente (C)'
#Si la calificacion fue 5 o menor a 5 debe de imprimir 'Reprobado (F)'


#pedimos al usuario que ingrese su calificacion
puntuacion = int(input("Introduce tu puntuación (0 a 100): "))

#validamos que sea una calificacion valida
if puntuacion < 0 or puntuacion > 100:
    print("Puntuación no válida. Debe ser un número entre 0 y 100.")

elif puntuacion >= 90:
    print("Excelente (A)")
elif puntuacion >= 80:
    print("Muy bien (B)")
elif puntuacion >= 70:
    print("Bien (C)")
elif puntuacion >= 60:
    print("Suficiente (D)")
# 3. Si no cumple ninguna de las anteriores, significa que es menor de 60
else:
    print("Reprobado (F)")