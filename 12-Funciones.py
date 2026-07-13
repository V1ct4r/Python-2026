def multiplicacion (x):
    return x * 10
y = multiplicacion (2)
print(f"El resultado de la funcion es {y}")

def saludo(nombre):
    print(f"Hola, mi nombre es + {nombre}")

saludo("Tomás")
#Saluda: La llamada a la funcion, imprime hola


def suma(a,b):
    return a + b
# Llamada a la funcion con argumentos posicionales: 2 -> a, -> b
resultado = suma(2,3)# El orden sí importa a=2, b=3
print(resultado)




# Definicion de la funcion 'resta' con parámetros por defecto (b=5)
def resta (a,b=5):
    return a - b

resultado1 = resta(6)
print("Resultado 1 (b por defecto):", resultado1)

resultado2 = resta(4,4)
print("Resultado 2 (b personalizado):", resultado2)


