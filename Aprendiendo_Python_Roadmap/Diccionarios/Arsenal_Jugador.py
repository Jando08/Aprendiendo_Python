arsenal = {
    "espada_laser": {
        "tipo": "Cuerpo a Cuerpo",
        "daño": 45,
        "mejoras": {
            "nivel": 2,
            "elemento": "Fuego"
        }
    },
    "blaster_pro": {
        "tipo": "Distancia",
        "daño": 30,
        "mejoras": {
            "nivel": 1,
            "elemento": "Electricidad"
        }
    }
}


# pedirle al usuario que busque el arma
arma = input('Ingrese el nombre del arma a buscar: ')

# confirmar que el arma existe
arma_encontrada = arsenal.get(arma)


if arma_encontrada == None:
    print('Error, esa arma no esta guardada en este arsenal')
else:
    print(f"El tipo de arma de {arma} es {arma_encontrada['tipo']}, y su daño base es {arma_encontrada['daño']} \n")
    print(f"El elemento de mejora es {arma_encontrada['mejoras']['elemento']} \n")
    arma_encontrada['mejoras']['nivel'] = arma_encontrada['mejoras']['nivel'] + 1
    print(f"El nuevo nivel de mejora es igual a {arma_encontrada['mejoras']['nivel']}")