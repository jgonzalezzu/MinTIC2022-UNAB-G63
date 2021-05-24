#Semana 2 - Clase 4 - Ciclos - Ejercicio 14
'''
Hacer un probrama que calcule la media de X números,se dajarán de solicitar
hasta que ingrese un cero
 '''
numero = 1
acumulado = 0
n = 0
#n es el número total de elementos
while numero != 0:
    numero = int(input('Ingrese valor: '))
    acumulado += numero
    n+=1
median = acumulado/n
print('La media aritmética es: ', round(median,1))