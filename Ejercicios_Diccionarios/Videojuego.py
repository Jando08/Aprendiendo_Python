#crear el diccionario
espada = {
    'daño' : 50,
    'durabilidad' : 100,
    'elemento' : 'Fuego'
}

#pedirle al usuario que estadistica de la espada quiere consultar
consulta = input('Que propiedad de la espada desea conocer (Daño, Durabilidad o Elemento): ')
consulta = consulta.lower()
#variable para imprimir mensaje
mensaje = ''

if consulta in espada.keys():
    mensaje = f'El {consulta} de la espada es de: {espada[consulta]}'
else:
    mensaje = 'Esa estadistica no pertenece a esta arma'

print(mensaje)