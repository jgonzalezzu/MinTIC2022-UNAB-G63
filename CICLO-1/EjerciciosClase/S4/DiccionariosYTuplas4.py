# Semana 4 - Clase 2 - Diccionarios y tuplas - Ejercicio 4
diccionario = {'one':'uno','two':'dos','three':'tres'}
#TODO: Extraer el contenido del diccionario en una lista
values = list(diccionario.values())
# Se usa two en lugar de dos
if 'two' in values:
    print('El elemento se encuentra en el diccionario')
else:
    print('El elemento no se encuentra en el diccionario')
