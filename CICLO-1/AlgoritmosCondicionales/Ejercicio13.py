print('Este programa calcula el valor final de la venta de la moto')
'''
Una distribuidora de motocicletas tiene una promoción de fin de año que consiste
en lo siguiente. Las motos marca Honda tienen un descuento del 5%, las marcas
Yamaha del 8% y la Suzuki 10%, las otras marcas 2%, calcule el valor del descuento
dependiendo de la marca de la moto escogida.
'''
print('Seleccione la marca de la moto: ')
print('Marca | # | Descuento|')
# print('----------------------')
print('Honda | 1 |     5%   |')
print('Yamaha| 2 |     8%   |')
print('Suzuki| 3 |     10%  |')
print('Otras | 4 |     2%   |')
price = float(input('Ingrese el valor del automotor: '))
brand = int(input('Ingrese la marca de la moto (1-4): '))
if brand == 1:
    total=price*0.95
    print('El valor final es: ',total, '$')
elif brand == 2:
    total=price*0.92
    print('El valor final es: ',total, '$')
elif brand == 3:
    total=price*0.9
    print('El valor final es: ',total, '$')
else:
    total=price*0.98
    print('El valor final es: ',total, '$')