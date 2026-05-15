cadena1 = 'hola,soy,jando'


resultado = cadena1.upper()  # Convierte toda la cadena a mayúsculas
resultado2 = cadena1.lower()  # Convierte toda la cadena a minúsculas
resultado3 = cadena1.capitalize()  # Convierte la primera letra de la cadena a mayúscula
resultado4 = cadena1.title()  # Convierte la primera letra de cada palabra a mayúscula
resultado5 = cadena1.find('jando')  # Busca la posición de la subcadena 'jando' en la cadena original
# y devuelve el índice de donde encontro el parametro. Si no se encuentra, devuelve -1.
resultado6 = cadena1.index('jando')  # Similar a find, pero si no encuentra la subcadena, lanza una excepción ValueError.
resultado7 = cadena1.isnumeric() # Verifica si la cadena está compuesta únicamente por caracteres numéricos. Devuelve True o False.
resultado8 = cadena1.isalpha() # Verifica si la cadena está compuesta únicamente por caracteres alfabéticos. Devuelve True o False.
resultado9 = cadena1.count('o') # Cuenta cuántas veces aparece el carácter 'o' en la cadena. Devuelve un número entero.
resultado10 = len(cadena1) # Devuelve la longitud de la cadena, es decir, el número de caracteres que contiene.
resultado11 = cadena1.startswith('h') # Verifica si la cadena comienza con la subcadena 'hola'. Devuelve True o False.
resultado12 = cadena1.endswith('ando') # Verifica si la cadena termina con la subcadena 'ando'. Devuelve True o False.
resultado13 = cadena1.replace('jando', 'mundo') # Reemplaza todas las apariciones de la subcadena 'jando' por 'mundo' en la cadena original. 
resultado14 = cadena1.capitalize() 
resultado15 = cadena1.split(',') # Divide la cadena en una lista de palabras utilizando la coma como separador. Devuelve una lista de cadenas.



#resultados de los ejercicios
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print(resultado9)
print(resultado10)
print(resultado11)
print(resultado12)
print(resultado13)
print(resultado14)
print(resultado15[1])
