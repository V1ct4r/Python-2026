# nombre
name = "Victor" # name es una variable donde esta guardado un dato 
# Impresion de nombre 
print (name)
print (f"Hola, mi nombre es {name}") 
# f-string = colocar entre llaves el identificador de la variables { }

 # Solicitando datos por teclado/terminal
nombre = input("Ingrese su nombre: ")
print (f"Hola  mi nombre es: {nombre}")

# Numeros enteros (int)
edad = 18
birth_year = 2007
# Impresion de datos
print (f"Hola tengo {edad} y naci en el año {birth_year}")

## Numeros flotantes (float)
estatura= 1.70
peso = 65.1

# Impresion de datos
print (f"Mi estatura es de {estatura} cm y peso {peso} kg ")

# Numeros complejos (complex)
num_complejo = 1 + 4j # declarando e inicializando un numero complejo
otro_complejo = complex (1,2) # segunda forma de declarar numeros complejos

# Formatear salida de numeros
Euler = 2.71828
# utilizando f-string
print (f"El valor de euler es aproximadamente :{Euler:.2f}")

# min y max 
numeros = [2,5,8,10]
print(numeros) 
print (max(numeros))
print (min(numeros))  

# Funcion round
num = 32.4567889 
print (round(32.4567889, 1))

# Elevar un numero a una potencia
resultado = pow (4,2)
print (resultado)

# devolver la suma de numeros
numeros = [2,4,6,6,7,]
resultado = sum(numeros)
print (resultado)

carrera = "Ingenieria Civil en Informatica"
institucion = "Universidad de los lagos"
descripcion = "El ramo de programcion se imparte en el 1er semestre de la carrera "

# Concatenar
frase_1 = "Hola"
frase_2 = "Mi nombre es Victor"
resultado = frase_1 + " " + frase_2
print (resultado)

### Otra forma
palabra= "Hola"
resultado = palabra * 4
print(resultado)

### Split funcion
equipo_de_futbol = "Colo Colo"
print(equipo_de_futbol.split())

### len ()
texto = "Hola Mundo"
print (len(texto))

### str ()
edad = 18
mensaje = "Tengo " + str(edad) + " años"
print (mensaje)

### upper ()
texto_original = "hola mundo"
texto_mayusculas = texto_original.upper()
print (texto_mayusculas)

##     lower ()
texto_1 = "HOOOLA MUNDO"
texto_2 = texto_1.lower()
print (texto_1)

### join ()
palabras = ["Hola", "mundo", "en", "Python"]
resultado = " ".join(palabras)
print(resultado)

## replace()
texto = "Hola Mundo"
print(texto.replace(" Mundo", ""))

### Funcion strip 
texto = "   Hola,Mundo    "
limpio = texto.strip()
print(limpio) 

### Booleanos
ampolleta = False 
interruptor = True
print(ampolleta,interruptor)

#### Listas
estudiantes = ['Victor', 'Eduardo', 'Victor','Victor']
print (estudiantes.count('Victor'))


# append ()
# Crear una lista
colores = [ "rojo", "blanco", "negro"]

#  Agregar un nuevo elemento a la lista con append
colores.append("morado")
print (colores)

## insert()
mi_lista = ["manzana", "uva", "pera"]
mi_lista.insert(1,'naranja')
print(mi_lista)

## extend()
lista_01 =  [1, 2, 3]
lista_02 =  [4, 5, 6]
lista_01.extend(lista_02)
print(lista_01)

# remove ()
colores = ["rojo", "azul", "verde", "naranjo"]
colores.remove("verde")
print(colores)

# pop ()
frutas = ["manzana","platano","pera"]
ultimas = frutas.pop()

primera = frutas.pop(0)
print (ultimas)
print (primera)

### sort ()
numeros = [5, 10, 1, 12, 0, 20]
numeros.sort()
print(numeros)

## sorted ()
letras = ['a', 'y', 'b']
letras_ordenadas =sorted(letras)
print(letras_ordenadas)

## clear ()
mi_dict ={1, 2, 3}
mi_dict.clear()
print(mi_dict)


""" En el analisis de antenas y redes de telecomunicaciones, la impedancia de una linea de
transmision se compone de una parte real (resistencia) y una parte imaginaria (reac
tancia). Un ingeniero necesita calcular la impedancia total sumando los componentes
de dos tramos de la red de fibra optica de la universidad.
a) Defina la impedancia del Tramo 1 como un numero complejo con parte real 50 y
parte imaginaria 30 (50 + 30j).
b) Defina la impedancia del Tramo 2 de la misma forma, con parte real 40 y parte
imaginaria −10 (40 − 10j).
c) Calcule la impedancia total sumando ambos tramos.
d) Muestre en pantalla la impedancia total, y luego imprima por separado solo la
parte real (convertida a numero entero int) y la parte imaginaria (convertida a
int) usando los atributos .real y .imag """""





# a) 
impedancia_tramo_1 = 50 + 30j

# b)
impedancia_tramo_2 = 40 - 10j

# c) 
suma_de_impedancias = impedancia_tramo_1 + impedancia_tramo_2

# d)
print (suma_de_impedancias)

impedancia_real = (suma_de_impedancias.real)
print (impedancia_real)

impedancia_imaginaria = (suma_de_impedancias.imag)
print (impedancia_imaginaria)


"""2. Al desarrollar sistemas inform´aticos, los usuarios suelen ingresar datos con espacios
accidentales o formatos incorrectos. El sistema de la biblioteca de la ULagos recibi´o el
RUT de un estudiante, pero viene “sucio” con espacios al inicio, al final y con puntos
intermedios: “ 19.543.872-K ”...
Escribe un programa que:
a) Guarde el RUT original en una variable de tipo string.
b) Utilice el m´etodo propio de Python para eliminar los espacios en blanco de los
extremos.
c) Utilice un m´etodo propio de Python para eliminar los puntos (.).
d) Calcule el largo total del RUT ya limpio (sin espacios ni puntos) y muestre el
resultado por pantalla junto al RUT con su nuevo formato"""

# a) 
rut = "19.543.872-k" 

# b) 
rut_sin_espacio = rut.strip ()

# c)
rut_final = rut_sin_espacio.replace(".","")

# d)

largo_final = len (rut_final)
print(f"largo del rut: {largo_final} | rut: {rut_final}")

""" 3. El Departamento de Admisi´on de la Universidad requiere un script b´asico para registrar
correos institucionales. El programa debe solicitar al usuario que ingrese su nombre
completo por terminal. Debido a que los usuarios pueden escribir con may´usculas y
min´usculas desordenadas o con espacios de m´as, el programa debe estandarizar el texto.
Escribe un programa que:
a) Solicite por terminal el nombre del estudiante.
b) Remueva los espacios sobrantes de los extremos.
c) Convierta todo el texto a min´usculas.
d) Reemplace los espacios intermedios por puntos (.) para simular la estructura de
un correo electr´onico.
e) Muestre en pantalla el resultado final con el texto @alumnos.ulagos.cl concatenado
al final """

# a) 

nombre_estudiante = input( "Ingrese su primer nombre, separando el nombre y apellidos por un espacio intermedio:")

# b)

nombre_estudiante = nombre_estudiante.strip()

# c)

nombre_estudiante = nombre_estudiante.lower()

# d)

nombre_estudiante = nombre_estudiante.replace (" ", ".")

# e)

print(nombre_estudiante + "@alumnos.ulagos.cl")


""""4. En f´ısica de part´ıculas, la precisi´on de los decimales es cr´ıtica. Un sensor de presi´on
hidr´aulica en un laboratorio de la universidad entrega una medida de 1024.7689 Pas
cales como tipo float. Escribe un programa que realice lo siguiente:
a) Defina la variable con el valor del sensor.
b) Convierta dicho valor a un n´umero entero (int), descartando los decimales, y
almac´enelo en una variable nueva.
c) Utilice un m´etodo propio de Python para redondear el valor original del sensor a
exactamente 2 decimales y guarde el resultado en otra variable.
d) Imprima un mensaje comparativo que muestre por terminal: el valor original, el
valor truncado como entero y el valor redondeado"""

# a)

valor_sensor = 1024.7689

# b)

valor_sensor_nuevo = int(valor_sensor)

# c)

valor_sensor_redondeado = round(valor_sensor,2)

# d)

print(f"A continuacion se mostraran los valores que ha entregado el sensor \n Valor original(inicial): {valor_sensor} \n Valor del sensor en numero entero: {valor_sensor_nuevo} \n Valor del sensor redondeado: {valor_sensor_redondeado}")



""""5. Una plataforma web de la Universidad de Los Lagos mide la velocidad de respuesta
de su servidor de asignaci´on de asignaturas. Se han tomado 3 muestras de tiempo de
respuesta (en milisegundos) de forma manual. Escribe un programa en Python que:
a) Solicite al administrador de la plataforma ingresar por terminal los 3 tiempos de
respuesta (los cuales pueden contener decimales, tipo float).
b) Almacene los 3 valores ingresados dentro de una lista de Python que debe tener
por nombre tiempos respuesta.
c) Acceda por medio de sus ´ındices ([0], [1], [2]) a los elementos de la lista para
calcular el tiempo promedio de respuesta del servidor.
d) Encuentre el tiempo m´as r´apido (m´ınimo) y el tiempo m´as lento (m´aximo) utili
zando las funciones propias de Python.
e) Calcule la “brecha de rendimiento”, que corresponde a la resta entre el tiempo
m´aximo y el m´ınimo.
f ) Imprima en pantalla la lista completa de datos y el reporte con el promedio y la
brecha calculada"""


# a)
toma_tiempo_1 = float(input("Administrador ingrese muestra de tiempo 1:"))
toma_tiempo_2 = float(input("Administrador ingrese muestra de tiempo 2:"))
toma_tiempo_3 = float(input("Administrador ingrese muestra de tiempo 3:"))

# b)

tiempo_de_respuesta = []
tiempo_de_respuesta.append(toma_tiempo_1)
tiempo_de_respuesta.append(toma_tiempo_2)
tiempo_de_respuesta.append(toma_tiempo_3)
 
# c)

promedio_tiempos = (tiempo_de_respuesta[0] + tiempo_de_respuesta[1] +tiempo_de_respuesta[2] ) / len(tiempo_de_respuesta)

# d)

min_tiempo = min(tiempo_de_respuesta)
max_tiempo = max(tiempo_de_respuesta)

# f)

brecha_de_tiempo = (max_tiempo - min_tiempo)
print(f" A continuacion la lista completa de los tiempos de respuesta y datos: \n Tiempos de respuesta: {tiempo_de_respuesta} \n Promedio: {promedio_tiempos} \n Brecha de tiempo: {brecha_de_tiempo}")
# Ejercicios para practicar 
