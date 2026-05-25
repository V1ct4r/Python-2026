

# DATOS NÚMERICOS - 07 DE MAYO 2026

# Números enteros 
edad = 18

# Números Flotantes (Reales)
estatura = 1.75 # el decimal se utiliza punto y no coma

# Números complejos 
num_complejo = 4 + 2j           # primera forma de crear un número complejo
otro-complejo = complex (4,2)   # segunda forma de crear un número complejo


print (num_complejo)
print (otro_complejo)

# Operación  Básica (Área de un Triángulo)
base = 8
altura = 12.5

   
área = (base * altura) / 2

print = área 
print (f"El área el triángulo es de {área} cm")



# Formatos de Salida de Números
print(f"El número PI tiene un valor de {PI: .4f}")


# El método de Redondeo
print (round(área))
print (f"El área del triángulo es de {round(área)} cm")

# Transformaciones de Números
print (float(edad))


# Cadenas de Texto (Strings)
carrera = "Ingeniería Civil en Informática"
institución = "Universidad de los Lagos"
print ("------CADENAS DE TEXTO (STRING)-------")


print (carrera[0])

# Aplicando Método Split

print (carrera.split())           # se divide la cadena en subcadenas
print (institución.split())       # Se para la cadena en subcadenas 



# Imprimir la posición del  caracter 
print (carrera[o]) # se imprime la primera letra
print (carrera[o]) # se imprime la última letra

print ("Hola" * 4.5)  # multiplicación de un string por un entero       

print(carrera[1])      # Imprime la posición del caracter en la cadena de texto (n), ya que la posición inicia en 0
print(carrera[-1])     # Imprime el último caracter de la cadena de texto (a), utilizando un índice negativo

print("hola" * 4)  # Multiplicaicon de una cadena de texto, repitiendo la palabra "hola" 4 veces

print(carrera[0:10])   # Imprime un rango de caracteres desde la posición 0 hasta la posición 9 (Ingenieria)

# Metodo len() permite conocer la cantidad de caracteres que tiene una cadena de texto (ademas de coontar los espacios)

# ARREGLOS (LISTAS)
print("---------- ARREGLOS (LISTAS) ----------")
colores = ["azul", "rojo", "verde", "amarillo"]  # Arreglo de stings
numeros = [1,2,3,4,5]                            # Arreglo númerico

print(colores[0])   # Imprime el primer elemento de la lista de colores (azul)  
print(numeros[-1])  # Imprime el último elemento de la lista  de números (5)


# Booleanos (Lógicos)

luz_electrica = True 
interruptor = False 

print  ("---- Booleanos-----")

print (luz_electrica)
print ( interruptor)

# Método Type que permite saber el tipo de dato de una variable
print (f" El tipo de dato es {type (num_complejo)}")


print ("----EVALUANDO DATOS BOOLEANOS-----")

print (bool(1))
print (bool(0))
print (bool(True))
print (bool(4000))

# EVALUANDO NÚMEROS CON OPERADORES DE COMPARACIÓN 
print (100 > 50)
print (10 == 10)
print (20 < 0)