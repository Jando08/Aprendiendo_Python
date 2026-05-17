'''
Reto (Cancelar suscripción): En tu plataforma hay una lista de usuarios premium: 
usuarios = ["juan99", "maria_dev", "pedro_g"]. El usuario "maria_dev" decidió cancelar su suscripción. 
Bórrala de la lista utilizando directamente su nombre (valor) e imprime la lista resultante.
'''

#crear la lista de usuario
usuarios = ['juan99', 'maria_dev', 'pedro_g']

#remover usuario
usuarios.remove('maria_dev')

#imprimir lista actualizada
print(usuarios)