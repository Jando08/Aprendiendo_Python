import pandas as pd

ventas_tecnologia = {
    "Dispositivo": ["Mouse Gamer", "Teclado Mecanico", "Monitor 4K", "Audifonos Wireless", "Tapete RGB"],
    "Precio": [850, 1200, 7500, 1100, 350],
    "Stock Disponible": [15, 8, 4, 25, 50]
}

df_ventas = pd.DataFrame(ventas_tecnologia)
print(df_ventas.shape)


mascara_premium = df_ventas["Precio"] > 1000
df_premium = df_ventas[mascara_premium]

print(df_premium[["Dispositivo", "Stock Disponible"]])


valor_inventario_total = (df_ventas["Precio"] * df_ventas["Stock Disponible"]).sum()
print("=== REPORTE FINANCIERO DE INVENTARIO ===")
print(f"El valor total de la mercancía en bodega es de: ${valor_inventario_total}\n")
print("=== ESTADÍSTICA DESCRIPTIVA DEL PRECIO ===")
print(df_ventas["Precio"].describe())