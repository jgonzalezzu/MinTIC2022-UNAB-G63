# Semana 4 - Clase 1 - Listas dentro de listas - Ejercicio1
import pprint
M = [[1,2,3],[2,12,6],[1,0,-3],[0,-1,0]]
# Usando pprint de la liibrería pprint para imprimir de for más estética los datos
# pprint.pprint(M)
print('Imprimiendo el elemento [1][2] de M ')
print(M[1][2])
print('Imprimiendo la matriz con ciclo for')
for fila in M:
    print(fila)

print('Imprimiendo las columnas fila[i=2] de la matriz con ciclo for')
for fila in M:
    print(fila[2])