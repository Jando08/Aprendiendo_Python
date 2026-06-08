# crear funcion depositar saldo
def depositar_saldo(saldo, cantidad):
    return saldo + cantidad

def retirar(saldo, cantidad):
    if saldo >= cantidad:
        return saldo - cantidad
    else:
        print(f'Su saldo es insuficiente. Tu saldo actual es de {saldo}')
        return saldo

saldo = 0
saldo = depositar_saldo(saldo,500)
saldo = depositar_saldo(saldo, 200)
saldo = retirar(saldo, 300)
saldo = retirar(saldo, 999)

