"""En la asignatura de Programación de la carrera de Ingeniería Civil en Informática,
un estudiante ha rendido sus primeras 3 calificaciones de tareas prácticas de
laboratorio. La aprobación de la asignatura exige calcular una nota final basada
en los siguientes pesos o ponderaciones para cada laboratorio

Laboratorio 1: 40% de la nota final 
Laboratorio 2: 40% de la nota final 
Laboratorio 3: 20% de la nota final 

Se solicita construir un programa en Python que realice las siguientes acciones:
1.Solicitar al usuario por terminal el ingreso de las 3 notas individualmente
(estas notas deben n incluir decimales).

2.Almacenar las 3 notas dentro de una estructura de datos de tipo lista.

3.Calcular el promedio ponderado final. Para esto, debes extraer las notas
directamente desde la lista utilizando sus índices (posiciones) y multiplicarlas
por sus respectivos porcentajes antes de sumarlas.

4.Mostrar en la terminal un reporte con todas las notas y el promedio final"""""




nota_1 = float(input("Usuario ingrese la nota número 1:"))
nota_2 = float(input("Usuario ingrese la nota número 2:"))
nota_3 = float(input("Usuario ingrese la nota número 3:"))

almacenar_notas = list[nota_1, nota_2, nota_3]
print(almacenar_notas)


almacenar_notas = [nota_1 + nota_2 + nota_3/3]
print(almacenar_notas)