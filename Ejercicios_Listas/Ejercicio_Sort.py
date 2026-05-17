'''
Reto (Puntuaciones altas): En un videojuego se registraron los siguientes puntajes: puntajes = [450, 1200, 300, 890, 2000]. 
Ordena la lista de mayor a menor para poder mostrar el top de mejores jugadores en la pantalla.
'''

#crear la lista
puntajes = [450, 1200, 300, 890, 2000]

#orderar la lista de mayor a menor
#para orderar valores le tenemoe que pasar el parametro reverse
puntajes.sort(reverse=True)

#imprimir lista ordenada de mayor a menor
print(puntajes)