
# Diccionarios
diccionario = {"azul" : "blue", "rojo" : "red"}
del(diccionario["rojo"])
print(diccionario)

diccionario2 = {"Victor":{"Edad": 19, "Estatura": 1.71}, "Emilia": {"Edad": 18, "Estatura": 1.52}}
print(diccionario2)


# Bucle While (mientras)

import math

numero = int(input("Usuario ingrese un numero:  "))

while numero<0:
    print("Error -> Debe ser un número positivo")
    numero = int(input("Digite un numero:  "))

print (f"\nSu raiz cuadrada del numero es: {(math.sqrt(numero)) :.2f}")


# Bucle while 
i = 0

while i<10:
    print("Hola Mundo")
    i += 1
# Bucle for 

for i in [1,2,3,4,5]:
    print("Hola mundo")



coleccion = "Victor"
for i in coleccion:
    print(f"{i}", end = " ")