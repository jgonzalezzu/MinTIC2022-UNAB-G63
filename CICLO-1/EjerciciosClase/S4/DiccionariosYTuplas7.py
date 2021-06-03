# Semana 4 - Clase 2 - Diccionarios y tuplas - Ejercicio 7
#TODO: con la función .clear se limpia el diccionario
diccionario = {'one':'uno','two':'dos','three':'tres'}
# diccionario.clear()
lista = ['Color', 'Talla', 'Marca']
# TODO: Crear un diccionario con la lista Color, Talla y Marca. Con valores por defecto igual a vacío
diccionario=diccionario.fromkeys(lista,'vacío')
for clave,valor in diccionario.items():
    print(clave,' - ', valor)