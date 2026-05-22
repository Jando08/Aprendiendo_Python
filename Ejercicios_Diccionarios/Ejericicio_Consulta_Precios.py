#crear diccionario
frutas = {
    'manzana' : 25,
    'platano' : 15,
    'mango' : 30
}

#pedir al usuario que escriba una fruta
fruta = input('Por favor ingrese una fruta(Manzana, Platano o Mango): ')
fruta = fruta.lower()

#obtener el precio de la fruta con el metodo .get(clave a buscar, valor por defecto)
resultado = frutas.get(fruta, 'No disponible')

#imprimir resultado final
print(f'El precio de la fruta {fruta}: {resultado}')

print('Hola amigos de youtube')
