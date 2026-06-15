# clase padre
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_pago(self):
        return self.salario_base



class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, bono_proyecto):
        super().__init__(nombre, salario_base)

        self.bono_proyecto = bono_proyecto

    
    # metodo que calcular el sueldo base mas bono
    def calcular_pago(self):
        # 🟢 Le pedimos el cálculo al padre y lo guardamos en una variable
        pago_base_padre = super().calcular_pago()

        # 🟢 Sumamos el bono a lo que sea que el padre haya calculado
        sueldo_final = pago_base_padre + self.bono_proyecto
        return sueldo_final
    

# creamos a los empleados
empleado_1 = Empleado('Milan', 3500)
empleado_2 = Empleado('Jando', 8000)
desarrollador_1 = Desarrollador('Midudev', 20000, 3000)
desarrollador_2 = Desarrollador('Torvalds', 50000, 8900)

# probar metodos
print(f"Pago del empleado {empleado_1.nombre}: ${empleado_1.calcular_pago()}") 

print(f"Pago de {empleado_2.nombre}: ${empleado_2.calcular_pago()}")

# lista para polirmofismo
nomima_quincenal = [empleado_1, empleado_2, desarrollador_1, desarrollador_2]

# ciclo para recorrer la lista
total_nomina = 0
for empleados in nomima_quincenal:

    total_nomina += empleados.calcular_pago()


print(f"El total de dinero gastado en la quincena por la empresa fue ${total_nomina}")