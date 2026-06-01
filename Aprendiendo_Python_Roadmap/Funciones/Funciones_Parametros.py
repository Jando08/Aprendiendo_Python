# Crear funcion
def calcular_precio_final(precio_articulo, descuento = 0):
    precio_final = precio_articulo - descuento

    return precio_final

compra_sin_descuento = calcular_precio_final(80)
print(compra_sin_descuento)


compra_con_descuento = calcular_precio_final(150, 30)
print(compra_con_descuento)


def crear_jugador(nombre, equipo, puntos_promedio = 0, es_all_star = False):
    print(f'Jugador: {nombre} | Equipo: {equipo} | PPP: {puntos_promedio} | ¿Es all star?: {es_all_star}')


crear_jugador('Bronny James', 'Lakers')

crear_jugador('Stephen Curry', 'Warriors', 26.4, True)

crear_jugador('Jayson Tatum', 'Celtics', es_all_star=True)