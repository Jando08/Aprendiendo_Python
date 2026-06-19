# importar libreria
import numpy as np

# crear lista
gastos_clientes = np.array([1200, 4500, 800, 15000, 3200])

# crear una mascara para saber que clientes gastaron mas de 4000 pesos
mascara = gastos_clientes > 4000

#filtramos los clientes VIP a traves de la mascara 
clientes_vip = gastos_clientes[mascara]

#imprimos la lista de los que gastaron mas de 4000 (clientes vip)
print(clientes_vip)