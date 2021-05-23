print('Este programa calcula la compra con descuento de los clientes')
#TODO: los clientes con compras superiores a 100.000 reciben un descuento del 20%
valor_entrada = float(input('Ingrese el valor de la compra: '))
if valor_entrada >= 100000:
    total = valor_entrada*0.8
    print('TOTAL: ', total)
else:
    total = valor_entrada
    print('TOTAL: ', total)