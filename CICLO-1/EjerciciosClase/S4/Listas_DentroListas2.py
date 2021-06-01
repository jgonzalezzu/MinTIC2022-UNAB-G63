# Semana 4 - Clase 1 - Listas dentro de listas - Ejercicio 2 
# Matriz nula de 2 × 2
M = [[0,0],[0,0]]
print('Print a una lista')
print(M)
# Cambiando el elemento menor 0,1
M[0][1] = 10
print('Print a una lista modificada')
print(M)
# Usando una lista nula
M = [0]*6
print('Print a una lista nula')
print(M)
M = [0]*6
M = [M]*5
print('Creando una matriz usando el operador * con listas nulas')
print(M)