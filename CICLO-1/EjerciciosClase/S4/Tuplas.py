# Semana 4 - Clase 4 - Tuplas - Ejercicio 1
'''
DEF: Una tupla es una secuencia de valores similar a las listas, pero a diferencia de estas, la tuplas contienen
VALORES INMUTABLES, indexados por números enterose i.e. [0], [1], [2], ... , [N]; siendo N un número entero.
Estos elementos están contenido entre paréntesis '('  ')' y están separados por comas , - IMPORTANTE-
'''
tupla = 1, 2, 3, 4, 5, 6
print('Tupla con valores int > ',tupla)
#TODO: Al imprimir se obtiene » (1, 2, 3, 4, 5, 6)
tupla1 = 1, 'a', 2, 'b', 3, 'c', 3.14151698
print('Tupla con valores mixtos > ', tupla1)
#TODO: Se puede definir la tupla con el constructor tuple(), IMPORTANTE: Uso del doble paréntesis
tupla_con_constructor = tuple((1,2,3,4,5,6))
print('Tupla usando el constructuor tuple > ', tupla_con_constructor)
#TODO: La tupla se puede declarar con paréntesis ()
tupla2=()