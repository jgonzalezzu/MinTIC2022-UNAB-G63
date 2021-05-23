import random
print('Este programa calcula el ')
'''
En una tienda de descuento se efectúa una promoción en la cual se hace un
descuento sobre el valor de la compra total según el color de la bolita que el cliente
saque al pagar en caja. Si la bolita es de color BLANCO no se le hará descuento alguno,
si es VERDE se le hará un 10% de descuento, si es AMARILLA un 25%, si es AZUL un 50% y
si es ROJA un 100%. Se sabe que solo hay bolitas de los colores mencionados. Realice
un programa que calcule el valor del descuento y el valor total de la compra.
|Bolita     |Descuento|
|Blanco     |   0     |
|Verde      |   10    |
|Amarila    |   25    |
|Azul       |   50    |
|Roja       |   100   |

'''
#TODO: Generar el color aleatorio de la bolita:
colours = ['Blanco','Verde','Amarilla','Azul','Roja']
compra = float(input('Ingrese el valor de la compra: $'))
bolita = random.choice(colours)
print('El color de tu bolita es: ', bolita)
if bolita == 'Roja':
    total = 0
    print('El valor de tu compra es: ', total, 'Felicitaciones!!')
elif bolita == 'Azul': 
    total = compra * 0.5
    print('El valor de tu compra es: ', total, 'Felicitaciones!!')
elif bolita == 'Amarilla':
    total = compra * 0.75
    print('El valor de tu compra es: ', total, 'Felicitaciones!!')
elif bolita == 'Verde':
    total = compra * 0.9
    print('El valor de tu compra es: ', total, 'Felicitaciones!!')
else:
    total = compra
    print('El valor de tu compra es: ', total, 'Sigue participando')
