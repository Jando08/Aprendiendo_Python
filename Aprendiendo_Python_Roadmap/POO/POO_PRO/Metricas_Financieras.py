class MetricasFinancieras:
    def __init__(self, producto, precio, estado):
        self.producto = producto
        self.precio = float(precio)
        self.estado = estado

    @classmethod
    def desde_csv_linea(cls, texto_linea):

        # le pasamos el parametro a otra variable para limpiarlo
        datos_limpios = texto_linea.split('-')

        # agarramos los valors como si estuvieran en un array
        producto = datos_limpios[0]
        precio = datos_limpios[1]
        estado = datos_limpios[2]

        # retornamos esos valores
        return cls(producto, precio, estado)


if __name__ == "__main__":

    registro_producto_1 = "Escoba-300-Vendido"
    registro_producto_2 = "Trapeador-130-Cancelado"
    registro_producto_3 = "Jabon-80-Vendido"

    # creamos objetos a traves del @classmethod o funcion
    producto_1 = MetricasFinancieras.desde_csv_linea(registro_producto_1)
    producto_2 = MetricasFinancieras.desde_csv_linea(registro_producto_2)
    producto_3 = MetricasFinancieras.desde_csv_linea(registro_producto_3)
        

    print("=== DATA INGESTION COMPLETED ===")
    print(f"Producto 1 - > Nombre: {producto_1.producto} | Precio: {producto_1.precio} | Estado: {producto_1.estado}")
    print(f"Producto 2 - > Nombre: {producto_2.producto} | Precio: {producto_2.precio} | Estado: {producto_2.estado}")
    print(f"Producto 3 - > Nombre: {producto_3.producto} | Precio: {producto_3.precio} | Estado: {producto_3.estado}")


    print("\n=== 📈 REPORTE ANALÍTICO GENERAL ===")
    
    # 1. Calcular los ingresos totales de la muestra
    ingresos_totales = producto_1.precio + producto_2.precio + producto_3.precio
    print(f"Ventas brutas totales intentadas: ${ingresos_totales}")

    # 2. Filtrar y sumar solo lo que SÍ se vendió con éxito
    ingresos_reales = 0
    productos_analizados = [producto_1, producto_2, producto_3]

    for p in productos_analizados:
        if p.estado == "Vendido":
            ingresos_reales += p.precio

    print(f"Ingresos netos reales (Solo 'Vendido'): ${ingresos_reales}")
    
    # 3. Calcular la pérdida por cancelaciones
    perdida = ingresos_totales - ingresos_reales
    print(f"Capital perdido en cancelaciones: ${perdida}")
