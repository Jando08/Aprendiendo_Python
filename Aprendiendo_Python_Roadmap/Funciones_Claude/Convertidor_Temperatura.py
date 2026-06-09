def convertir(temperatura, escala):
    if escala == 'C':
        return (temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9


print(convertir(100, "C"))  # → 212.0  (100°C en Fahrenheit)
print(convertir(32, "F"))   # → 0.0    (32°F en Celsius)
print(convertir(0, "C"))    # → 32.0