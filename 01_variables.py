# variables 
'''
las variables en python se deben crear con el snake case
es decir, con letras minusculas y guiones bajos para separar palabras
'''
my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

#se le puede cambiar el tipo de dato a una  variable, poniendole el nuevo tipo de dato al inicio de la variable
my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_bool_variable = True
print(my_bool_variable)

# al momento de imprimir varias variables, se pueden separar por comas para poder imprimirlas todas juntas
# a esto se le llama concatenar variables, y se puede hacer con cualquier tipo de dato
print(my_string_variable, my_int_to_string_variable, my_bool_variable)
print("Esta es el valor de: ", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable)) # la función len nos devuelve la cantidad de caracteres que tiene la variable, incluyendo los espacios

# Variables en una sola linea !Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Alejandro", "Parra", "Andronova", 20
#el orden al momento de imprimir no importa, se puede cambiar
print("Me llamo: ",name, ", Mi apellido es: ", surname, ", Mi apodo es: ", alias, ", y tengo: ", age, "años") 


"""
#Inputs
name = input('¿Cuál es su nombre?: ')
age = input('¿Cuál es su edad?: ')

print(name)
print(age)
"""

#cambiamos el tipo de variable
name = 35
age = "Alejandro"
print(name)
print(age)

# forzamos el tipo?
address: str = 'Mi direccion es: '
address = 32
print(address)
#las variables en python toman el ultimo valor que se les asigna
#xd
