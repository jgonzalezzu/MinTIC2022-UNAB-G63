#Semana 3 - Clase 1 - Validación y captura de Excepciones - Ejercicio 3
'''
Usando el problema de detectar la paridad de un número ingresador por el usuario
'''
while True:
    try:
        number = int(input('Ingrese un número >'))
    except ValueError:
        print('Debe ingresar un número')
    else:
        break

if number%2 == 0:
    print(number, 'es PAR')
elif number%2 == 1:
    print(number, 'es IMPAR')
elif number == 1:
    print(number, 'es Impar')
else:
    print(number, 'es Cero')