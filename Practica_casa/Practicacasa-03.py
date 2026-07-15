nombre = "Victor"
edad = 18
print("Hola, mi nombre es", nombre, "y mi edad es", edad)

edad = 19 
print(edad)

colores = ['Rojo', 'Negro', 'Azul', 'Blanco']
print ("Primer color", colores [0])
print ("Último color", colores [3])

""""Nivel 1: Conceptos Iniciales (Variables e Impresión)
Este ejercicio se basa en la sintaxis básica y el uso de la función print()
.
Tarea: Declara una variable llamada nombre con tu nombre y otra llamada carrera.
 Luego, imprime un saludo que diga: "Hola, mi nombre es [nombre] y estudio [carrera]"
   utilizando el método de f-strings (cadenas literales entre llaves { })"""

nombre = "Víctor"
carrera = "Ingenieria civil en Informática"
print (f"Hola, mi nombre es", nombre, "y estudio", carrera, "en la universidad de los lagos, Castro")

"""Nivel 2: Interacción y Tipos de Datos
Basado en el uso de input() y datos numéricos
.
Tarea: Crea un programa que solicite al usuario su año de nacimiento por terminal. Convierte esa entrada (que llega como string) a un entero (int)
. Calcula su edad actual restando el año ingresado al año 2026 y muestra el resultado en pantalla"""""

año_de_nacimiento = int (input("Usuario ingrese su año de nacimiento:"))
edad = 2026 - año_de_nacimiento
print (f"Su edad actual es: {edad}")

""""Nivel 3: Manejo de Listas y Operaciones Matemáticas
Basado en el Ejercicio en Clases N°1 de las fuentes
.
Tarea: Un centro de investigación registró las temperaturas de los primeros 3 días de la semana: Lunes (12.5), Martes (14.2) y Miércoles (11.8)
.
Guarda estos valores en una lista
.
Utiliza la función sum() y len() para calcular el promedio de la semana
.
Encuentra la diferencia entre el día más caluroso y el más frío usando las funciones max() y min()"""

temperaturas = [12.5, 14.2, 11.8]

promedio_semana = (sum(temperaturas)) / (len(temperaturas))
diferencia = (max(temperaturas)) - (min(temperaturas))
print(promedio_semana)
print(diferencia)

""""Nivel 4: Monitoreo y Acceso por Índices
Basado en el Ejercicio en Clases N°2 sobre consumo de memoria RAM
.
Tarea: Crea un programa para monitorear el consumo de un servidor en 4 instantes (Mañana, Mediodía, Tarde y Noche):
Solicita los 4 consumos (en GB) por teclado y guárdalos en una lista como números decimales (float)
.
Accede a cada valor individualmente usando indexación (ej. lista) para guardarlos en variables independientes
.
Calcula y muestra el "Rango de Operación", que es la diferencia entre el consumo máximo y el mínimo"""


## Consumo de Ram 
manana = float (input("Ingrese el consumo de ram de manana: "))
print (manana)
mediodia = float (input("Ingrese el consumo de ram de mediodia: "))
print (mediodia)
tarde  = float (input("Ingrese el consumo de ram de tarde: "))
print (tarde)
noche = float (input ("Ingrese el consumo de ram de noche: "))
print (noche)

ram = [manana, mediodia, tarde, noche]
consumo_manana = ram [0]
consumo_mediodia = ram [1]
consumo_tarde = ram [2]
consumo_noche = ram [3]

consumo = (consumo_manana + consumo_mediodia + consumo_tarde + consumo_noche)
promedio = (consumo / 4)
print (f"El consumo de la ram promedio del dia es de {promedio}")

diferencia = max (ram) - min (ram)
print (f"La diferencia del maximo y minimo valor es de ¨{diferencia}")

"""""Nivel 5: Desafío de Ponderaciones (Reto Final)
Este es el Reto N°1 planteado en el curso para evaluar la integración de conocimientos
.
Tarea: Un estudiante tiene 3 notas de laboratorio con pesos distintos: Lab 1 (40%), Lab 2 (40%) y Lab 3 (20%)
.
Solicita las 3 notas al usuario e inclúyelas en una lista
.
Extrae las notas de la lista mediante sus índices y multiplícalas por sus respectivos porcentajes
.
Suma estos resultados para obtener el promedio ponderado final y muestra un reporte detallado en la terminal"""

nota1 = float(input("Usuario ingrese su nota del primer lab, equivalente a un [40%]:"))
print (nota1)
nota2 = float(input("Usuario ingrese su nota del segundo lab, equivalente a un [40%]:"))
print (nota2)
nota3 = float(input("Usuario ingrese su nota del tercer lab, equivalente a un [20%]:"))
print (nota3)

notas =[ nota1, nota2, nota3]
print(notas)

ponderacion_nota1 = notas[0] * 0.40
ponderacion_nota2 = notas[1] * 0.40
ponderacion_nota3 = notas[2] * 0.20
promedio_final = ponderacion_nota1 + ponderacion_nota2 + ponderacion_nota3
print (promedio_final)




"""" Nivel 6: Gestión de Inventario Robusta (Diccionarios y Seguridad)
Este ejercicio pone a prueba el acceso seguro a datos y la actualización dinámica
.
Contexto: Tienes un inventario inicial: stock = {"Laptop": 5, "Mouse": 10}.
Tarea:
Crea un segundo diccionario con "nuevas llegadas": {"Mouse": 15, "Teclado": 8}.
Usa el método .update() para fusionarlos. Nota cómo el valor del "Mouse" se reemplaza, no se suma
.
Solicita al usuario el nombre de un producto para consultar. 
Usa obligatoriamente .get() para que, si el producto no existe,
 el programa muestre "Producto no catalogado" en lugar de fallar con un error
 """
inventario_inicial = {"Laptop": 5, "Mouse": 15, "Teclado":10}
nuevas_llegadas_inventario = {
    "Mouse": 15,
    "Teclado": 8,
}

inventario_inicial.update(nuevas_llegadas_inventario)
producto_buscado = input("Usuario ingrese producto que está buscando:")
cantidad_productos = inventario_inicial.get(producto_buscado,"Producto no catalogado")
print(f"Stock disponible para '{producto_buscado}':{cantidad_productos}")


""""Nivel 7: Control de Acceso y Unicidad (Sets)
Basado en las operaciones de teoría de conjuntos
.
Contexto: El Laboratorio A tiene una lista de alumnos: ["Juan", "Ana", "Luis", "Ana"]. El Laboratorio B tiene: ["Luis", "Marta", "Elena"].
Tarea:
Convierte ambas listas a sets para eliminar automáticamente los duplicados (como la segunda "Ana")
.
Muestra los alumnos que están inscritos en ambos laboratorios usando .intersection()
.
Muestra los alumnos que están en el Laboratorio A pero no en el B usando .difference()"""

laboratorio_A = ["Juan", "Ana", "Luis", "Ana"]
laboratorio_B = ["Luis", "Marta", "Elena"]
sets= set(laboratorio_A + laboratorio_B)
print(sets)

set_A = set(laboratorio_A)
set_B = set(laboratorio_B)

alumnos_inscritos = set_A.intersection(set_B)
print("En ambos laboratorios:", alumnos_inscritos)

solo_lab_A = set_A.difference(set_B)
print("Solo en el lab A:", solo_lab_A)

"""Nivel 8: Procesamiento de Datos Masivos (Filter y Map)
Este ejercicio utiliza las funciones de CPU e iterables para evitar bucles manuales
.
Contexto: Tienes una lista de ramos: ["Programación", "Física", "Cálculo", "Habilidades"].
Tarea:
Usa la función filter() con una función lambda para extraer solo los ramos que tengan más de 7 caracteres
.
A esa lista resultante, aplícale map() para convertir todos los nombres a mayúsculas usando .upper()
.
Convierte el resultado final de nuevo a una lista e imprímelo"""
ramos = ["Programación", "Física", "Cálculo", "Habilidades"]
ramos_filtrados = filter(lambda x: len(x) > 7, ramos)
ramos_mayus = map(lambda x : x.upper(), ramos_filtrados)
resultado = list(ramos_mayus)
print (resultado)
