def revisar_intento(secreto, intento):
    if intento == secreto:
        return 'Correcto! Adivinaste el numero'
    elif intento > secreto:
        return 'Muy alto, intenta un numero mas bajo'
    else:
        return 'Muy bajo, intenta mas alto'
    

print(revisar_intento(7, 3))   
print(revisar_intento(7, 10))  
print(revisar_intento(7, 7))