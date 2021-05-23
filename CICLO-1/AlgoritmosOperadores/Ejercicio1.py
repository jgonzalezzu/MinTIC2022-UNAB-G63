import math
print("Ejercicio 1")
'''
    Sacar la hipotenusa de un triangulo rectángulo, pidiendo
    al usuario el valor de los dos catetos
'''
print('Este programa calcula la hipotenusa dados dos catetos por el usuario')
cateto_1 = float(input('Ingrese el primer cateto: '))
cateto_2 = float(input('Ingrese el segundo cateto: '))
hipotenusa = math.sqrt(cateto_1**2 + cateto_2**2)
print('la hipotenusa es: ', round(hipotenusa,3))    