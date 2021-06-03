# Semana 4 - Clase 2 - Diccionarios y tuplas - Ejercicio 10
#TODO: Acceder a los elementos del diccionario
diccionairo = {'four':'cinco'}
diccionairo1 = {'one':'uno', 'two':'dos'}
# Cuando de busca un valor existente este va a retornar el valor asociado a ese valor, de lo contrario imprime 'not está'
dato = diccionairo1.get('one','no está')
print('el dato es',dato)
dato = diccionairo1.get('three','no está')
print('el dato', dato)