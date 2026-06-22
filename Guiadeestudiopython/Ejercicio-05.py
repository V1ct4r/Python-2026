"""5. Una plataforma web de la Universidad de Los Lagos mide la velocidad de respuesta
de su servidor de asignaci ́on de asignaturas. Se han tomado 3 muestras de tiempo de
respuesta (en milisegundos) de forma manual. Escribe un programa en Python que:"""

"""a) Solicite al administrador de la plataforma ingresar por terminal los 3 tiempos de
respuesta (los cuales pueden contener decimales, tipo float). LISTA
b) Almacene los 3 valores ingresados dentro de una lista de Python que debe tener
por nombre tiempos respuesta. LISTA""

c) Acceda por medio de sus  ́indices ([0], [1], [2]) a los elementos de la lista para
calcular el tiempo promedio de respuesta del servidor. LISTA

d) Encuentre el tiempo m ́as r ́apido (minimo) y el tiempo m ́as lento (maximo) utili-
zando las funciones propias de Python. LISTA

e) Calcule la “brecha de rendimiento”, que corresponde a la resta entre el tiempo
m ́aximo y el minimo. Lista

f) Imprima en pantalla la lista completa de datos y el reporte con el promedio y la
brecha calculada."""

toma_tiempo1 = float(input("Administrados ingrese el tiempo de respuesta numero 1: "))
toma_tiempo2 = float(input("Administrados ingrese el tiempo de respuesta numero 2: "))
toma_tiempo3 = float(input("Administrados ingrese el tiempo de respuesta numero 3: "))

tiempos_respuestas = []
tiempos_respuestas.append(toma_tiempo1)
tiempos_respuestas.append(toma_tiempo2)
tiempos_respuestas.append(toma_tiempo3)

promedio_tiempos = (tiempos_respuestas[0] + tiempos_respuestas[1] +tiempos_respuestas[2] ) / len(tiempos_respuestas)

min_tiempo = min(tiempos_respuestas) # mas rapido
max_tiempo = max(tiempos_respuestas) # mas lento

brecha_tiempo = (max_tiempo - min_tiempo)

print(f" A continuacion la lista completa de los tiempos de respuesta y datos: \n Tiempos de respuesta: {tiempos_respuestas} \n Promedio: {promedio_tiempos} \n Brecha de tiempo: {brecha_tiempo}")