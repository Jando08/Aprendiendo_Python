# =====================================================================
# MÓDULO: conversor.py
# Responsabilidad: Contener únicamente funciones de conversión matemática
# =====================================================================

def celsius_a_fahrenheit(celsius):
    """
    Toma los grados Celsius (int o float) y regresa su equivalente en Fahrenheit.
    """
    resultado = (celsius * 9 / 5) + 32
    return resultado

