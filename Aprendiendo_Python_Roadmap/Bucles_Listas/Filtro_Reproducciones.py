"""
Usa un ciclo for para recorrer la lista reproducciones. Recuerda inventar una variable temporal en singular (por ejemplo: for reproduccion in reproducciones:).
Aquí viene lo nuevo: Dentro del bucle (con su debida indentación), mete un condicional if que evalúe si la reproducción actual es mayor a 100 (> 100).
Si la canción cumple con la condición, imprime un mensaje usando un f-string que diga: "Canción destacada: X reproducciones". (Si no cumple, no imprimas nada para esa canción).
"""

reproducciones = [45, 120, 85, 300, 150]

for reproduccion in reproducciones:
    if reproduccion > 100:
        # Metemos el print aquí adentro con 8 espacios de sangría
        print(f"Canción destacada: {reproduccion} reproducciones")