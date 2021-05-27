#Semana 3 - Clase 2 - Listas - Ejercicio 1
#Propiedades de las listas
lista = [1,2,3,4,5]
print(lista)
lista = ['Adrian','Carlos','Cristian','Daniela','Juan']
print(lista)
lista = ['Adrian',1,2,3.5,'Carlos','Cristian','Daniela','Juan']
print(lista)
#Se pueden mezclar datos
#También se puede imprimir el elemento que está en el i-ésima posición [i]
print(lista[0], 'índice 0')
print(lista[1], 'índice 1')
print(lista[2], 'índice 2')
print(lista[3], 'índice 3')
print(lista[4], 'índice 4')
print(lista[5], 'índice 5')
print(lista[6], 'índice 6')
print(lista[7], 'índice 7')
#Se puede acceder de orden inverso ingresando con el [-i]
print(lista[-0], 'índice -0')
print(lista[-1], 'índice -1')
print(lista[-2], 'índice -2')
print(lista[-3], 'índice -3')
print(lista[-4], 'índice -4')
print(lista[-5], 'índice -5')
print(lista[-6], 'índice -6')
print(lista[-7], 'índice -7')
#imprimir el tamaño de la lista
size = len(lista)
print(size)
#Se pueden aplicar funciones como cadena de texto  e imprimir la longitud
cadena = 'Hola mundo'
print(len(cadena))
#Puedo imprimir una porción de cadena siendo la sintaxis de la forma [posición inicial: posición finál]
print(cadena[5:9])
#Se pueden imprimir por pasos siendo la sintaxis de la forma [posición inicial: posición finál : pasos]
print(cadena[:10:2])