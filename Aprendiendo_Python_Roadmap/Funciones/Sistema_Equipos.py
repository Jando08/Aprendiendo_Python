# Crear una funcion llamada guardar_por_equipo
def guardar_por_equipo(nombre, archivo_destino = 'lakers.txt'):
    nombre_limpio = nombre.strip().upper()
    with open(archivo_destino, 'a') as archivo:
        archivo.write(f'{nombre_limpio}\n')

        return f'{nombre_limpio} guardado con exito en {archivo_destino}'

guardar_por_equipo('Anthony Davis')
guardar_por_equipo('Sthepen Curry', 'warriors.txt')



