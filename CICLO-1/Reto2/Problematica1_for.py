print('Problematica 1 - with FOR loop')
print('Ingrese el valor de las compras, para detener el ingreso escriba 0 >')
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
# Control de entradas
N = int(input('Ingrese el número de ventas >'))
# Control de ventas
total50 = float(0)
total_50_100 = float(0)
total100 = float(0)
# Cantidad de ventas
control_total50 = 0
control_total100 = 0
control_total_50_100 = 0
total_ventas = 0
for ventas in range(1, N+1):
    venta = float(input('Ingrese el valor de la venta >'))
    total_ventas += venta
    if venta <= 50:
        total50 += venta
        control_total50 += 1
    elif (venta > 50) and (venta <= 100):
        total_50_100 += venta
        control_total_50_100 += 1
    elif venta > 100:
        total100 += venta
        control_total100 += 1
    else:
        print('No ha ingresado venta!')
# Eliminar el conteo del codigo de finalización
print('| Total de ventas                    >',ventas, '| con valor total de >', total_ventas)
print('| Ventas mayores a $100.000          >',control_total100, '| con valor total de >',total100)
print('| Ventas entre $50.000 y $100.000    >',control_total_50_100, '| con valor total de >', total_50_100)
print('| Ventas menores o iguales a $50.000 >',control_total50, '| con valor total de >', total50)
