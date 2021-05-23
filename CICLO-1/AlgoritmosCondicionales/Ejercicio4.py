print('Este programa determina el mayor de tres números ingresados: ')
n1 = float(input('Ingrese el número 1: '))
n2 = float(input('Ingrese el número 2: '))
n3 = float(input('Ingrese el número 3: '))
if n1 > n2 and n1 > n3:
    print(n1)
    # if n2 > n3:1.1
    #     print(n2)
    # else:
    #     print(n3)
elif n3 > n2:
    print(n3)
    # print(n2)
    # print(n1)
else:
    print(n2)
    # print(n3)
    # print(n1)