class Organizador:
    def __init__(self, bloque_nota):
        self.bloque_nota = bloque_nota
        self.lista_tareas = []
        self.total_completadas = 0

    def agregar_tarea(self, nombre_tarea):
        self.lista_tareas.append(nombre_tarea)
        print(f"Tarea agregada: '{nombre_tarea}'")

    def completar_tarea(self, nombre_tarea):
        if nombre_tarea in self.lista_tareas:
            self.lista_tareas.remove(nombre_tarea)
            self.total_completadas += 1
            print(f"Felicidades! Completaste: {nombre_tarea}")
        else:
            print(f"La tarea {nombre_tarea} no esta registrada")

    def resumen_actual(self):
        tareas_pendientes = len(self.lista_tareas)
        print("\n--- 📊 RESUMEN DEL ORGANIZADOR ---")
        print(f"📋 Tareas pendientes: {tareas_pendientes}")
        print(f"🏆 Tareas completadas: {self.total_completadas}")
        print("-----------------------------------\n")




# 1. Creamos el organizador para las materias
mis_notas = Organizador("Tareas Computacion Ubicua")

# 2. Agregamos pendientes
mis_notas.agregar_tarea("Programar el Semaforo Social")
mis_notas.agregar_tarea("Configurar tuberia CI/CD")

# 3. Completamos una tarea
mis_notas.completar_tarea("Programar el Semaforo Social")

# 4. Vemos cómo quedó nuestro tablero
mis_notas.resumen_actual()