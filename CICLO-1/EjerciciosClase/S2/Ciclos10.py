#Semana 2 - Clase 4 - Ciclos - Ejercicio 10
#TODO: Integrar None, vairalbe almacenada None -> Valor nulo o vacío
#Este programa calcula el mayor de los números dentro de un vector
mayor = None
print('Valor mayor inicial: ', mayor)
for valor in [3,41,12,9,74,15]:
    if mayor is None or valor > mayor:
        mayor = valor
    print('Valor en el bucle: ', valor, mayor)
print('El mayor elemento del vector es: ', mayor)