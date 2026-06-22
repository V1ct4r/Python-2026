"""1. En el analisis de antenas y redes de telecomunicaciones, la impedancia de una linea de
transmision se compone de una parte real (resistencia) y una parte imaginaria (reac-
tancia). Un ingeniero necesita calcular la impedancia total sumando los componentes
de dos tramos de la red de fibra  ́optica de la universidad."""

# A) Defina la impedancia del Tramo 1 como un numero complejo con parte real 50 y
#       parte imaginaria 30 (50 + 30j).

#tramo 1
impedancia1 = 50 + 30j

# B) Defina la impedancia del Tramo 2 de la misma forma, con parte real 40 y parte
#    imaginaria −10 (40 − 10j).

#tramo 2
impedancia2 = 40 -10j

#suma de ambos tramos
sumaimpedancias = impedancia1 + impedancia2


#d) Muestre en pantalla la impedancia total, y luego imprima por separado solo la
#    parte real (convertida a numero entero int) y la parte imaginaria (convertida a
#      int) usando los atributos .real y .imag.

print(sumaimpedancias)

impedanciareal = int(sumaimpedancias.real)
print(impedanciareal)

impedanciaimag = int(sumaimpedancias.imag)
print(impedanciaimag)


