print('Este programa calcula el descuento total de las camisetas')
count = int(input('Ingrese la cantidad de camiestas: '))
# valor = float(input('Ingrese el valor de la camiseta'))
valor = float(1.0)
if count >= 3:
    total = (count*valor)*0.8
    print('El valor total de la compra es: ',total,'$')

else:
    total = (count*valor)*0.9
    print('El valor total de la compra es: ',total,'$')