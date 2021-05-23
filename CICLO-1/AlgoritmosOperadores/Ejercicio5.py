print("ejercicio 5")
'''
    calcular el nuevo salrio de un empleado si obtuvo un in_
    cremento del 10%.
'''
print('este programa calcula el incremento del salario')
salario = float(input('ingrese el valor del salario: '))
incremento = float(input('ingrese el porcentaje de incremento (0-100): '))
salariofinal = salario * ((incremento/100)+1)
print('el salario con el incremento de ', incremento, '%, es de: ', round(salariofinal,2))