'''
Reto (Lista de invitados): Tienes una lista inicial de invitados a tu fiesta: invitados = ["Luis", "Ana", "Carlos"]. 
El usuario quiere registrar a un nuevo amigo. 
Pídele el nombre con un input() y agrégalo al final de la lista. 
Al final, imprime la lista completa.
'''

#crear la lista de invitados
invitados = ['Luis', 'Ana', 'Carlos']

#pedirle al usuario que ingrese al nuevo invitado
nuevo_invitado = input('Ingresa el nombre del nuevo invitado: ')

#anadir el nuevo invitado a la lista
resultado = invitados.append(nuevo_invitado)

#imprimir resultado
print(invitados)
print(f'El nuevo invitado a la fiesta a sido {nuevo_invitado}')