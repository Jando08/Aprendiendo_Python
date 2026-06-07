# crea una funcion potencia(base, exponente = 2)
# que eleve la base al exponente. Si no se pasa el
# exponente, usa 2 por defecto

def potencia(base, exponente = 2):
    numero_potenciado = base ** exponente
    return numero_potenciado

print(potencia(2, 10)) 
print(potencia(3)) 