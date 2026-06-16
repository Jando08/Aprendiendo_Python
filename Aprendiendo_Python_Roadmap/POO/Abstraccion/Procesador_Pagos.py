from abc import ABC, abstractmethod

class MetodoPago(ABC):
    def __init__(self, monto_compra):
        self.monto_compra = monto_compra

    @abstractmethod
    def procesar_pago(self):
        pass


class PagoTarjeta(MetodoPago):
    def __init__(self, monto_compra, numero_tarjeta):
        super().__init__(monto_compra)
    
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self):
        print(f"Procesando pago con tarjeta {self.numero_tarjeta} por un total de ${self.monto_compra}... Aprobado!!!")   

        
class PagoPaypal(MetodoPago):
    def __init__(self, monto_compra, correo):
        self.correo_electronico = correo
        super().__init__(monto_compra)

    def procesar_pago(self):
        print(f"Conectando con Paypal... Pago de ${self.monto_compra} autorizado para la cuenta de {self.correo_electronico}... Aprobado!!!") 




if __name__ == "__main__":

    compra_1 = PagoTarjeta(2500, "1111-2222-3333-4444") 
    compra_2 = PagoPaypal(3000, "alejandroleyva.0805@gmail.com")

    carritos_compra = [compra_1, compra_2]

    print("=== Procesando la caja de la tienda")

    for pago in carritos_compra:
        pago.procesar_pago() 
    