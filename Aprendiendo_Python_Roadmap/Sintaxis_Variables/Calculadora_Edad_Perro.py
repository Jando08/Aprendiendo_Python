"""
Pídele al usuario la edad de su perro usando input().
Como el usuario ingresará un texto, convierte esa edad a un número decimal (float)
Calcula la edad equivalente en "años perrunos". 
La regla general dice que 1 año humano equivale a 7 años de perro.
Muestra el resultado final: "Tu perro tiene 2.0 años humanos, lo que equivale a 14.0 años perrunos."
"""

# Pedirle la edad del perro
nombre_perro = input("Ingrese el nombre de su perro: ")
edad_perro_humana = input("Ingrese la edad de su perro en años humanos: ")
edad_perro_humana = float(edad_perro_humana)

# Convertir los anios de humanos por anios de perro
edad_perro_canina = edad_perro_humana * 7


print(f'Tu perro {nombre_perro} tiene {edad_perro_humana}, lo que equivale a {edad_perro_canina} años perrunos')

