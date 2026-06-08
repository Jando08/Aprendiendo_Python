def aplicar_descuento(precio, descuento):
    descuento_calculado = precio * descuento / 100
    return precio - descuento_calculado

print(aplicar_descuento(200, 10)) 
print(aplicar_descuento(500, 25))  
print(aplicar_descuento(100, 50))  