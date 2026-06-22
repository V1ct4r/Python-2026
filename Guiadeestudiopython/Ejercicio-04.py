"""
4. En fisica de particulas, la precisi ́on de los decimales es crıtica. Un sensor de presion

hidraulica en un laboratorio de la universidad entrega una medida de 1024.7689 Pascales 
como tipo float. Escribe un programa que realice lo siguiente:

a) Defina la variable con el valor del sensor. LISTO
b) Convierta dicho valor a un n ́umero entero (int), descartando los decimales, y
almac ́enelo en una variable nueva. LISTA
c) Utilice un metodo propio de Python para redondear el valor original del sensor a
exactamente 2 decimales y guarde el resultado en otra variable. LISTA
d) Imprima un mensaje comparativo que muestre por terminal: el valor original, el
valor truncado como entero y el valor redondeado."""

valor_sensor = 1024.7689
valor_sensor_entero = int(valor_sensor)
redondeado_valor_sensor = round(valor_sensor,2)

print(f"A continuacion se mostraran los valores que ha entregado el sensor \n Valor original(inicial): {valor_sensor} \n Valor del sensor en numero entero: {valor_sensor_entero} \n Valor del sensor redondeado: {redondeado_valor_sensor}")

""