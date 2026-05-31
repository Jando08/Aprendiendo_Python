precios = [15, 80, 45, 120, 30, 95]

gasto_total = 0

for precio in precios:
    if precio < 50:
        print(f'Artículo en oferta aprobado: ${precio} dolares')
        gasto_total += precio

print(f'El total a pagar por las ofertas: {gasto_total}')

