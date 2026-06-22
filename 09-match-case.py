print("1.Hamburguesa")
print("2.Pizza")
print("3.Completos italianos")

opcion = input ("Por favor, elige una opcion (1-3):")

match opcion:
    case "1":
        print("Has elegido una Hamburguesa. Precio: $5000")
    case "2":
        print ("Has elegido Pizza. Precio $7500")
    case "3":
        print ("Has elegido Completo. Precio $2500")
    case _:
        print ("Opción no válida. Por favor, elige entre el 1 y 3 ")

mes = 4        # abril
match mes:
    case 12 | 1 | 2:
        print ("Verano")
    case 3| 4 | 5:
        print ("Otoño")
    case 6 | 7 | 8:
        print ("Invierno")
    case 9 | 10 | 11:
        print ("Primavera")
    case _:
        print ("Mes inválido")

# Ejemplo Saludo según hora del día
hora = 18 # formato 24 horas 
match hora:
    case h if 0 <= h < 6:
        print ("Buenas noches")
    case h if 6 <= h < 12:          
        print ("Buenos días")
    case h if 12 <= h < 18:
        print ("Buenas tardes")
    case h if 18 <= h < 24:
        print ("Buenas noches")
    case _:
        print ("Hora inválida")


x = [1, 2, 3]
match x:
    case [a, b, c]:  # desagrupando valores de la lista x
        print (f"Elementos de la lista x: {a}, {b}, {c}")
datos = {
    'nombre': 'Víctor',
    'edad': 31
}
match datos:
    case {'nombre': n, 'edad': e}:
        print (f"Nombre: {n}, Edad: {e}")
    

# Guards
# Ejemplo: Saber si un número es par o impar
valor = 6
match valor:
    case v if v % 2 == 0: # x toma el valor de cualquier variable
        print (f"{valor} es un número par")
    case v if v % 2 != 0:
        print (f"{valor} es un número impar")