import random
print('Este programa le pide al usuario que escoja un número al azar')
compra = float(input('Ingrese el valor de la compra: '))
pick = random.randrange(0,148,1)
print('Tu número aleatorio es:', pick)
if pick < 74:
    total=compra*0.75
    print('Felicitaciones! el descuento es del 15%, TOTAL: ', total)
else:
    total=compra*0.8
    print('Felicitaciones! el descuento es del 20%, TOTAL: ', total)