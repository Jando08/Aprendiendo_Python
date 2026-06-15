class Notificacion:
    def __init__(self, usuario):
        self.usuario = usuario
    
    def enviar(self):
        print("Enviando notificacion generica")
    

class NotificacionEmail(Notificacion):

    def enviar(self):
        print(f"Email enviado a {self.usuario}: !Tu cuenta ha sido verificada!")


class NotificacionSMS(Notificacion):

    def enviar(self):
        print(f"SMS envado a {self.usuario:} Tu codigo de verificacion es 4030")



# 1. Creamos la lista polimórfica con notificaciones mezcladas
alertas_pendientes = [
    NotificacionEmail("Alejandro"),
    NotificacionSMS("Carlos"),
    NotificacionEmail("Mariana"),
    NotificacionSMS("Milan")
]

print("=== 🚀 ENVIANDO ALERTAS DEL SISTEMA ===")

# 2. ¡Aplica el Polimorfismo aquí!
for alerta in alertas_pendientes:
    # Invoca el método correspondiente con sus paréntesis ()
    alerta.enviar()
    print("-" * 40)