# Definicion de Variables
nombre = "Victor" 
apellido = "Saldivia"
edad = 18

# Esto es un comentario de una linea 

""" Esto es un comentario multilinea porque sigo hacia abajo """

# Formas de Imprimir Texto 

# Formas 1: Clásica separando variables y textos por comas 
print ("Mi nombre es", nombre, "y mi apellido es", apellido, "y tengo", edad, "años")


# Forma 2: Utilizando f-strings 
print (f"Mi nombre es",{nombre}, "y mi apellido es", {apellido}, "y tengo", {edad}, "años") # Utilizar esta 

# Forma 3: Concatenación (utilizando el operador +)
# La función str () transforma el valor a Cadena de texto
print ("Mi nombre es", + nombre + "y mi apellido es", + apellido +  "y tengo", + str  (edad) +  "años")


# Utilizando el método Input
carrera = input ("¿Qué carrera estudias?")
print (f"Yo estudio la carrera de: {carrera}")



