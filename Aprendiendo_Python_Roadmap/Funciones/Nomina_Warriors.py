def calcular_gasto_total(lista_salarios):
    suma_salarios = 0

    for salario in lista_salarios:
        suma_salarios += salario

    if suma_salarios > 100:
        suma_salarios *= 1.10

    return suma_salarios

salarios_warriors = [50,40,20]

total_nomina =  calcular_gasto_total(salarios_warriors)

print(f'El total a pagar de nomina con impuestos es {total_nomina} millones')