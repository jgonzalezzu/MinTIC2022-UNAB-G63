print('Problematica 1 - with WHILE loop')
print('=======================================================================')
print('Ingrese los valores de las compras, para detener el ingreso escriba 0 >')
print('=======================================================================')
'''
Variables:
    Control de número de ventas
        - control_total50: cuenta el número de ventas menores a $50.000
        - control_total100: cuenta el número de ventas superiores a $100.000
        - control_total_50_100: cuenta el número de ventas entre $50.000 y $100.000
    Control de las ventas por rangos
        - total50: Suma las ventas menores a $50.000
        - total100 Suma las ventas superiores a $100.000
        - total_50_100: Suma las ventas entre $50.000 y $100.000
''' 
#Control de entradas
N = 1
#Control de ventas
total50 = float(0)
total_50_100 = float(0)
total100 = float(0)
#Cantidad de ventas
control_total50 = 0
control_total100 = 0
control_total_50_100 = 0
control_ventas = 0
while N != 0:
    N = float(input('Ingrese el valor de la venta >'))
    control_ventas += 1
    if N <= 50.000:
        total50 += N
        control_total50 += 1
    elif (N > 50.000) and (N <= 100.000):
        total_50_100 += N
        control_total_50_100 += 1
    elif N > 100.000:
        total100 += N
        control_total100 += 1
    else:
        print('No ha ingresado venta!')

total_ventas = total50 + total100 + total_50_100
#Eliminar el conteo del codigo de finalización
control_ventas -= 1
control_total50 -= 1
print('| Total de ventas                    >', control_ventas ,'| con valor total de >',total_ventas)
print('| Ventas mayores a $100.000          >', control_total100, '| con valor total de >', total100)
print('| Ventas entre $50.000 y $100.000    >', control_total_50_100, '| con valor total de >', total_50_100)
print('| Ventas menores o iguales a $50.000 >', control_total50, '| con valor total de >', total50)