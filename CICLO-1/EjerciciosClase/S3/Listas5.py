#Semana 3 - Clase 2 - Listas - Ejercicio 5 Extra: Métodos de cadenas
cadena = 'Bienvenido a MisionTic 2022'
#TODO: Longitud de la cadenas
tamano = len(cadena)
print('longitud de cadena >',tamano)
#TODO: Buscar dentro de la cadena
buscar = cadena.find('2022')
print('Índice de inicio de la busqueda >',buscar)
buscar = cadena.find('Nombre')
print('Índice de inicio de la busqueda >',buscar)
#El resultado -1 implica que el elemento que se busca no está presente
#TODO: reemplazar elementos de la cadena
cadenan = cadena.replace('2022','UNAB')
print(cadenan)
#En el comando replace (argumento a buscar, argumento a reemplazar)