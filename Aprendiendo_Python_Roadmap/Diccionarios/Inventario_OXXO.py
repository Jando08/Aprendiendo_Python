inventario = {
    "papas": 22,
    "refresco": 18,
    "galletas": 15
}

busqueda = input('Ingrese el nombre del producto deseado: ')

precio = inventario.get(busqueda)

if precio == None:
    print(f'Lo sentimos, no manejamos {busqueda} en esta sucursal')
else:
    print(f'El precio de {busqueda} es igual a : ${precio}')
