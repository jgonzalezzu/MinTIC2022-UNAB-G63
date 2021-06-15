# Semana 5 - Clase 3 - Métodos de busqueda Iterativo  - Ejercicio 1
lista = [25,33,4,8,9,3,6,97,22,56,44]
buscar = 22
indice = 0
for dato in lista:
    if dato == buscar:
        print(f'El dato está en el índice » {indice}')
    indice += 1