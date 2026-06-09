usuarios = {
    "alejandro12": {
        "nombre": "Alejandro",
        "plan": "Premium",
        "artistas_favoritos": ["Frank Ocean", "Brent Faiyaz"]
    },
    "carlos_sf": {
        "nombre": "Carlos",
        "plan": "Gratuito",
        "artistas_favoritos": ["Kanye West", "Joji"]
    }
}

# pedirle el usuario
username = input('Ingrese el nombre de su usuario: ')

# buscar el usuario en la lista
cuenta_encontrada = usuarios.get(username)

if cuenta_encontrada == None:
    print(f'Error!, ese nombre de usuario no existe')
else:
    # el diccionario de usuario se convierte en mi variables cuenta_encontrada
    print(f'Bienvenido de vuelta {cuenta_encontrada['nombre']} \n')
    print(f"Tu estatus actual de cuenta es: Plan {cuenta_encontrada['plan']}.\n")
    print(f"Tu primer artista favorito en la lista es: {cuenta_encontrada['artistas_favoritos'][0]}")

