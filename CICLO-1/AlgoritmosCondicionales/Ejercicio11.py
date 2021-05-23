print('Este programa calcula el valor total de la compra de las llantas')
cant = int(input('Ingrese cantidad de llantas: '))
if cant >= 5:
    total=cant*180000
    print('Total compra es:',total)
else:
    total = cant*150000
    print('Total compra es:',total)