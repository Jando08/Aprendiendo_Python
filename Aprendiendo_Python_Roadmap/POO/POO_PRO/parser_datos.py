class AnalisisUsuario:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = int(edad)  # Nos aseguramos de que sea entero para estadísticas
        self.carrera = carrera

    # 🚨 Convertimos este método en una FÁBRICA de objetos
    @classmethod
    def desde_texto_sucio(cls, texto_linea):
        """
        Recibe un string tipo: 'Nombre-Edad-Carrera'
        Lo limpia, lo separa y crea el objeto automáticamente.
        """
        # .split("-") rompe el texto por los guiones y crea una lista
        datos_limpios = texto_linea.split("-")
        
        nombre = datos_limpios[0]
        edad = datos_limpios[1]
        carrera = datos_limpios[2]
        
        # 🟢 'cls' manda a llamar al constructor de arriba (__init__)
        # Esto equivale a hacer: AnalisisUsuario(nombre, edad, carrera)
        return cls(nombre, edad, carrera)


# ==========================================
# 🛠️ SECCIÓN DE PRUEBAS (Directo en Kitty)
# ==========================================
if __name__ == "__main__":
    # 1. Imagina que estos datos te llegaron de un archivo de texto desordenado
    registro_api_1 = "Jando-20-DataScience"
    registro_api_2 = "Milan-22-Software"

    # 2. Usamos el @classmethod para crear los objetos DIRECTAMENTE desde el texto sucio
    usuario_1 = AnalisisUsuario.desde_texto_sucio(registro_api_1)
    usuario_2 = AnalisisUsuario.desde_texto_sucio(registro_api_2)

    # 3. Comprobamos que los datos ya están estructurados y limpios
    print("=== 📊 DATA INGESTION COMPLETED ===")
    print(f"Usuario 1 -> Nombre: {usuario_1.nombre} | Edad: {usuario_1.edad} | Carrera: {usuario_1.carrera}")
    print(f"Usuario 2 -> Nombre: {usuario_2.nombre} | Edad: {usuario_2.edad} | Carrera: {usuario_2.carrera}")
    
    # Al ser enteros, ya podemos hacer matemáticas con las edades
    promedio_edad = (usuario_1.edad + usuario_2.edad) / 2
    print(f"📈 Edad promedio de la muestra: {promedio_edad} años")