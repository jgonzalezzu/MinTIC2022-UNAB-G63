#Semana 2 - Clase 3 - Condicionales - Ejercicio 1
'''
Este programa calcula el promedio y evalua la aprobbación
Si el promedio    
'''
nota_1 = float(input('Ingrese nota 1: '))
nota_2 = float(input('Ingrese nota 2: '))
nota_3 = float(input('Ingrese nota 3: '))
mean = (nota_1+nota_2+nota_3)/3

if mean >= 7:
    print('Usted ha APROBADO')
elif mean >=4:
    print('Usted está en nivel REGULAR')
elif mean >= 2:
    print("Usted estám en nivel BAJO")
else:
    print('Usted está REPROBADO')

