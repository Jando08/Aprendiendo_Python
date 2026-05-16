'''
Reto: Solicita al usuario que escriba una frase larga. Luego, pídele que elija una letra. 
Usa el método para decirle en qué índice numérico aparece esa letra por primera vez. 
(Si no existe, deja que falle con el ValueError, ¡así ves cómo reacciona!).
'''

#pedir al usuario que ingrese una frase
frase_larga = input('Ingrese una frase de mas de 20 letras: ')
letra = input('Escoge una letra que hayas de cualquiera que este en la frase: ')


#ver en que posicion esta la letra
letra = frase_larga.index(letra)

#imprimir resultado
print(f'La posicion de la letra que escogio esta en la posicion: {letra}')