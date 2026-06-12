class PerfilUsuario:
    def __init__(self, nombre_usuario, edad):
        self.nombre_usuario = nombre_usuario
        self.__edad = edad

    # metodo GETTER
    def obtener_edad(self):
        return self.__edad
    
    # metodo SETTER
    def modificar_edad(self, nueva_edad):
        if nueva_edad > 0 and nueva_edad < 120:
            self.__edad = nueva_edad
            print(f"La nueva edad {nueva_edad} ha sido guardada con exito!")
        else:
            print(f"Error! La edad proporcionada ({nueva_edad}) no es valida")

    

# creamos objetos para probar la clase
usuario_1 = PerfilUsuario('Jando', 20)

# imprimimos edad inicial del usuario
print(f"La edad inicial del usuario {usuario_1.nombre_usuario} es {usuario_1.obtener_edad()} anos")

# modificamos la edad
usuario_1.modificar_edad(40)
print(f"La nueva edad del usuario es {usuario_1.obtener_edad()} anos")

# intentamos meter un dato basura para probar el filtro de seguridad
usuario_1.modificar_edad(-5)
usuario_1.modificar_edad(150)

