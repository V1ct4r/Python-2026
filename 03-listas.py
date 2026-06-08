# LISTAS 

# Primera forma de Declaración de Listas (lista Mixta)
lista1 = {"Víctor", 12, true }
ramos = [] # Lista vacía 
# Segunda forma de Declaración de Listas (lista Númerica)

n = list(1,2,3,4,5)


# Método para las listas 

# 01 - Cont() - contar la cantidad de concurrencias de un elemento 
print (lista1.count("Víctor"))

print (lista1.count(32))
print = (ramos)

# Agregar un elemento al final de la lista
ramos.append('Química')
print (ramos)

ramos.append('Habilidades Comunicativas')
print (ramos)

ramos.append('Programación')
print (ramos)

# Otra forma de insertsr un elemento a la lista (De forma específica)
ramos.insert (0, 'Introducciónn a la Matemática')
print (ramos)

# Modificar un elemento en especifíco de una lista 
ramos [2] = 'Habilidades Comunicativas para Ingenieros/as'
print (ramos)

# Eliminar el último elemento de la lista 
ramos.pop() 
print (ramos)

# Ordenar los elementos de una lista de forma descendente a ascendente 
# print (ramos.sort())
ramos.sort()
print(ramos)

n.sort ()
print (n)

# Ordenar elementos de una lista según la cantidad de caracteres de cada elemento
ramos.sort (key=len)
print (ramos)

# Extender una lista a partir de otra
ramos_segundo_semestre = ['Ciudadanía', 'Algebra', 'Introducción a la Física ']
print (ramos_segundo_semestre)

ramos.extend(ramos_segundo_semestre)
print(ramos)


# Aplicando metodo index 
print(ramos_segundo_semestre.index('Algebra'))

