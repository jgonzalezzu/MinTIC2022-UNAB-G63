import math
print("Ejercicio 13")
'''
    Realice un algoritmo que calcule el volumen y área de una
    esfera.
'''
print('Este programa calcula el volume y área de una esfera')
radius = float(input('Ingrese el radio de la esfera'))
vol = (3/4)*math.pi*math.pow(radius,3)
surface = 4*math.pi*math.pow(radius,2)
print('El volumen de la esfera es: ', vol, 'unidades cúbicas')
print('El área superficial de la esfera es: ',surface, 'unidades cuadradas')