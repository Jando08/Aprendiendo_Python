# 1. LISTA INICIAL
equipos = ["Lakers", "Warriors", "Celtics"]
print(f"Lista inicial de equipos: {equipos}")

# Tarea 1: Agrega a los "Suns" al final
equipos.append('Suns')

# Tarea 2: Mete a los "Bucks" en la posición 1
equipos.insert(1, 'Bucks')

# Tarea 3: 
print(f"Total de equipos en la liga: {len(equipos)}")

# Tarea 4: Corregido para que ordene de la A a la Z (alfabéticamente estándar)
equipos.sort()

# Tarea 5: Muestra la lista final ordenada 
print(f"Lista final ordenada: {equipos}")