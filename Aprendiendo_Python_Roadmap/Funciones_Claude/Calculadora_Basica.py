# Crea una funcion calcular(a, b, operacion) que realice
# suma, resta, multiplicacion y division segun el 3er parametro

def calcular(a, b, operacion):
    match operacion:
        case 'Suma':
            return a + b
        case 'Resta':
            return a - b
        case 'Multiplicacion':
            return a * b
        case 'Division':
            return a / b
        case _:
            return 'NO existe esa operacion'
        
print(calcular(19, 5, 'Suma'))
print(calcular(23, 8, 'Resta'))
print(calcular(9, 5, 'Multiplicacion'))
print(calcular(20, 5, 'Division'))