"""En una subestación eléctrica se representan algunas señales mediante números complejos. Un técnico necesita calcular la señal total combinando dos mediciones obtenidas en distintos puntos de la red.

a) Defina la señal A como 25 + 15j.
b) Defina la señal B como 10 - 5j.
c) Calcule la señal total sumando ambas.
d) Muestre la señal total y luego imprima por separado su parte real e imaginaria convertidas a int."""

señal_A = 25 +15j 
señal_B = 10-5j 
señal_total = señal_A + señal_B
print (señal_total)
print (f"La parte real es: \ n {señal_A} | La parte imaginaria es : \ n {señal_B}")

"""" El sistema de inventario de una empresa
 recibió un código de producto con errores de formato:
   " AB-123-XY ". Antes de almacenarlo en la base de datos, es necesario limpiarlo.

a) Guarde el código en una variable string.
b) Elimine los espacios en blanco de los extremos.
c) Elimine los guiones (-).
d) Calcule el largo del código limpio e imprímalo junto al resultado final."""

codigo_inicial = " AB-124-XY "
codigo_inicial = codigo_inicial.strip()
codigo_inicial = codigo_inicial.replace ("-","")

largo = len(codigo_inicial)
print (codigo_inicial)
print ("Largo:",largo)

""""La universidad desea automatizar la creación de correos institucionales.
 Para ello, el programa debe transformar
   correctamente el nombre ingresado 
   por el estudiante.

a) Solicite el nombre completo por teclado.
b) Elimine espacios innecesarios de los extremos.
c) Convierta el texto a minúsculas.
d) Reemplace los espacios por guiones bajos (_).
e) Agregue @ulagos.cl al final.
f) Muestre el correo generado."""


nombre_estududiante = input("Ingrese su nombre completo, seperando nombres y apellidos por un espacio intermedio:")
nombre_estududiante = nombre_estududiante.strip()
nombre_estududiante = nombre_estududiante.lower()
nombre_estududiante = nombre_estududiante.replace(" ",".")
print (nombre_estududiante + "@ulagos.cl")

""""Un sensor de laboratorio registró una temperatura de 37.85642 °C. El encargado necesita visualizar el dato con distintos niveles de precisión.

a) Guarde el valor en una variable.
b) Conviértalo a entero.
c) Redondee el valor original a 3 decimales.
d) Muestre el valor original, el entero y el redondeado."""

temperatura_inicial = 37.85642
temperatura_a_entero = int(temperatura_inicial)
redondeado = round(temperatura_inicial,3)
print("Original:", temperatura_inicial)
print("Entero:", temperatura_a_entero)
print("Redondeado:", redondeado)

"""""Un administrador de red necesita analizar tres mediciones de velocidad de descarga obtenidas durante el día.

a) Solicite tres velocidades (float).
b) Guárdelas en una lista llamada velocidades.
c) Calcule el promedio utilizando los índices de la lista.
d) Obtenga la velocidad máxima y mínima.
e) Calcule la diferencia entre ambas.
f) Muestre un reporte completo."""""

velocidad_1 = float(input("Ingrese la primera velocidad: "))
velocidad_2 = float(input("Ingrese la segunda velocidad: "))
velocidad_3 = float(input("Ingrese la tercera velocidad: "))

velocidades = [velocidad_1, velocidad_2, velocidad_3]
promedio = (velocidades[0] + velocidades[1] + velocidades[2])/3
velocidad_maxima = max (velocidades)
velocidad_minima = min (velocidades)
diferencia = velocidad_maxima - velocidad_minima
print ("Velocidades:", velocidades)
print ("Promedio:",promedio)
print ("Maxima", velocidad_maxima)
print ("Minima", velocidad_minima)
print ("Diferencia", diferencia)

""""Una aplicación educativa necesita realizar distintas operaciones sobre el texto "Programacion en Python" para generar diferentes formatos de salida.

a) Muestre la cantidad de caracteres.
b) Convierta el texto a mayúsculas.
c) Convierta el texto a minúsculas.
d) Reemplace la palabra Python por Java."""

texto_inicial = "Programacion en Python"
print ("Cantidad de caracteres:", len(texto_inicial))
print ("Mayusculas:", texto_inicial.upper())
print ("Minusculas:", texto_inicial.lower())
print ("Reemplazo a Java:", texto_inicial.replace("Python", "Java"))

"""Un docente almacenó las siguientes notas en una lista: [5.5, 6.2, 4.8, 7.0]. Necesita obtener información estadística básica.

a) Calcule el promedio.
b) Determine la nota más alta.
c) Determine la nota más baja.
d) Calcule la diferencia entre ambas."""""

notas = [5.5, 6.2, 4.8, 7.0 ]
promedio = sum(notas) /len(notas)
mayor = max(notas)
menor = min (notas)
diferencia = mayor - menor
print ("Notas:", notas)
print ("Promedio:", promedio)
print ("Mayor:", mayor)
print ("Menor:", menor)
print ("Diferencia:", diferencia)

""""Durante la lectura de información desde un archivo, el número 250 fue almacenado como texto. Es necesario convertirlo para poder realizar operaciones matemáticas.

a) Defina numero = '250'.
b) Convierta el string a entero.
c) Convierta el entero a float.
d) Multiplique el resultado por 4.
e) Muestre el valor final y el tipo de dato de cada variable usando type()."""

numero = "250"
entero = int(numero)
decimal = float(entero)
resultado = decimal * 4 
print ("String;", numero, type(numero))
print ("Entero:",entero, type(entero))
print ("Float:", decimal, type(decimal))
print ("Resultado:", resultado,)


# Ejercicio 1
corriente_A = 25 + 15j
corriente_B = 10 -5j
corriente_total = corriente_A + corriente_B
print (corriente_total)
print(corriente_A)
print(corriente_B)
# Ejercicio 2
valor = 37.85642
entero = int(valor)
redondeo = round(valor,3)
print ("Valor:", valor)
print ("Entero:", entero)
print ("Redondeo:", redondeo)
# Ejercicio 3
texto = "Programacion en Python" 
print ("Cantidad de caracteres:", len(texto))
print ("Texto a mayuscula:", texto.upper())
print ("Texto a minuscula:", texto.lower())
print ("Reemplazar a Java:", texto.replace("Python","Java"))

# Ejercicio 4
asignaturas =["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje" ]
print (asignaturas)

