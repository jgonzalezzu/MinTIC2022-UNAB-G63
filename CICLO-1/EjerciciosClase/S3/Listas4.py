#Semana 3 - Clase 2 - Listas - Ejercicio 4
#TODO: Agregar elementos a las listas
lista = ['Adrian','Natalia','Carlos','Octavio']
lista2 = lista+['Andres']
print(lista)
print(lista2)
#TODO: Agregar elementos usando append - trabaja sobre la lista sin crear nuevas variables
lista3 = lista
lista3.append('María')
print(lista3)
#TODO: Eliminar elementos de las listas usando pop(), si los paréntesis elimina el último elemento
print(lista3.pop())
print(lista3.pop(1))
removido = lista3.pop()
print(removido)
del lista2[1:2]
print('lista 2 usando del >', lista2)
lista2.insert(1,'nuevo dato')
print('lista 2 usando insert >', lista2)
lista2.remove('nuevo dato')
print('lista 2 usando remove >', lista2)