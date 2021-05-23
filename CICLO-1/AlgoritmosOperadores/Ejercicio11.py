import math
print("ejercicio 11")
'''
    realice un algoritmo que calcule el volumen y área de un cubo.
'''
print('este programa calcula el volumen y el area de un cubo')
line = float(input('ingrese la longitud del cubo: '))
vol = math.pow(line,3)
surf_area=6*(line**line)
print('el volumen del cubo es: ', vol, ' unidades cúbicas')
print('el área superficial del cubo es: ',surf_area, ' unidades cuadradas')