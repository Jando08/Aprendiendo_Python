# crea una funcion es_par(numero) que retorne true si el numero es par
# o false si es impar

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(es_par(4))
print(es_par(7))
