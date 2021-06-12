# Semana 5 - Clase 2 - Recursividad  - Ejercicio 3 - Ejercicio 1 - Busqueda binaria
'''
DEF: La recursión es un concepto matemático
'''
#TODO: Función recursiva que NO retorne un valor para que no se ejecute de forma indefinida
def conteo(numero):
    numero-=1
    if numero > 0:
        print(numero)
        conteo(numero)
    else:
        print('Fin del conteo')

conteo(5)
'''
SALIDA:
4
3
2
1
Fin del conteo
'''