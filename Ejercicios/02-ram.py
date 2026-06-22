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