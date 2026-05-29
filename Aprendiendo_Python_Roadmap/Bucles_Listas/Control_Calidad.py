pixeles_muertos = [0, 4, 1, 5, 2, 3]

pantallas_defectuosas = 0

for pixel in pixeles_muertos:
    if pixel >= 3:
        print(f'Pantalla rechazada con {pixel} píxeles muertos.')
        pantallas_defectuosas += 1


print(f'Revisión terminada. Total de pantallas defectuosas: {pantallas_defectuosas}')