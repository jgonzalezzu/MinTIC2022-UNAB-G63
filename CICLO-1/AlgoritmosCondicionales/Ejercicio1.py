print('Este programa evalua la nota final de tres calificaciones')
#TODO: Este programa calcula el promedio de tres notas ingresadas por el usuario
nota_1 = float(input('Ingrese nota 1: '))
nota_2 = float(input('Ingrese nota 2: '))
nota_3 = float(input('Ingrese nota 3: '))
mean = (nota_1 + nota_2 + nota_3)/3
if mean >= 3.5:
    print('Usted ha APROBADO con: ', round(mean,1))
else:
    print('Usted ha REPROBADO con: ', round(mean,1))