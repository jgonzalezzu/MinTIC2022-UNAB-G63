# Semana 5 - Clase 2 - Recursividad  - Ejercicio 2
#TODO: programa que calcula el n! (factorial) de un valor dado con recursividad

def factorial(numero):
    print('Valor inicial -> ', numero)
    if numero > 1:
        numero=numero*factorial(numero-1)
    print('Valor final -> ', numero)
    return numero

print(factorial(5))