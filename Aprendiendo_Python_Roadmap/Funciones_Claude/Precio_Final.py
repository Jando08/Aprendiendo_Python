def precio_final(precio, descuento, impuesto):
    precio_con_descuento = precio - (precio * descuento / 100)
    precio_con_impuesto = precio + (precio * impuesto / 100)
    return precio_con_descuento, precio_con_impuesto

print(precio_final(1000, 10, 16))  
print(precio_final(500, 20, 8))    
print(precio_final(200, 5, 15))  