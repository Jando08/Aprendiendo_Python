class RegistroServidor:
    def __init__(self, timestamp, codigo_estado, endpoint):
        self.timestamp = timestamp
        self.codigo_estado = int(codigo_estado)
        self.endpoint = endpoint

    
    @classmethod
    def desde_log_linea(cls, texto_linea):

        # limpiamos el texto
        texto_limpio = texto_linea.split("|")

        # guardamos los valores del texto en variables separadas
        timestamp = texto_limpio[0]
        codigo_estado = texto_limpio[1]
        endpoint = texto_limpio[2]

        # retornamos los valores
        return cls(timestamp, codigo_estado, endpoint)
    
if __name__ == "__main__":

    # tres líneas de log sucias que vienen del servidor web
    log_1 = "2026-06-17 12:30|200|/home"
    log_2 = "2026-06-17 12:32|404|/productos/ofertas"
    log_3 = "2026-06-17 12:35|500|/checkout/pagar"

    # hacemos los objetos con la funcion
    registro_1 = RegistroServidor.desde_log_linea(log_1)
    registro_2 = RegistroServidor.desde_log_linea(log_2)
    registro_3 = RegistroServidor.desde_log_linea(log_3)


    print("=== LOG INGESTION COMPLETED ===")

    #hacemos polimorfismo para ver cual codiog si es correcto
    todos_los_log = [registro_1, registro_2, registro_3]
    conteo_errores = 0

    # hacemos un ciclo para recorrer los log
    for log in todos_los_log:
        if log.codigo_estado >= 400:
            #mandar mensaje de error
            print(f"Alerta: Error detectado en la ruta {log.endpoint} con codigo {log.codigo_estado}")
            #sumamos 1 al contador de errores
            conteo_errores += 1
        else:
            print(f"Log exitoso en la ruta {log.endpoint} con codigo {log.codigo_estado} ")
        
    # Calcular la tasa de error (Métrica analítica básica)
    tasa_error = (conteo_errores / len(todos_los_log)) * 100
    print(f"\n📊 Tasa de error del servidor: {tasa_error:.2f}%")
