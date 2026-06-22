"""

3. El Departamento de Admision de la Universidad requiere un script basico para registrar
correos institucionales. El programa debe solicitar al usuario que ingrese su nombre
completo por terminal. Debido a que los usuarios pueden escribir con may ́usculas y
minusculas desordenadas o con espacios de mas, el programa debe estandarizar el texto.
Escribe un programa que:
a) Solicite por terminal el nombre del estudiante. LISTA
b) Remueva los espacios sobrantes de los extremos. LISTA
c) Convierta todo el texto a minusculas. LISTA
d) Reemplace los espacios intermedios por puntos (.) para simular la estructura de
un correo electronico. LISTA
e) Muestre en pantalla el resultado final con el texto @alumnos.ulagos.cl concatenado
al final. LISTO

""

nombre_estudiante = input("Usuario ingrese su nombre completo, separando nombres y apellidos por un espacio intermedio ")

nombre_estudiante = nombre_estudiante.strip()
nombre_estudiante = nombre_estudiante.lower()
nombre_estudiante = nombre_estudiante.replace(" ",".")


print(nombre_estudiante + "@alumnos.ulagos.cl")


"""
