print('Este programa determina la paridad del número ingresado')
number = int(input('Ingrese un número: '))
if number%2 == 0:
    print('PAR')
elif number%2 == 1:
    print('Impar')
elif number == 1:
    print('Impar')
else:
    print('Cero')