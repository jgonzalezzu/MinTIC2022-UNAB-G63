#Semana 2 - Clase 3 - Condicionales - Ejercicio 2
# Este programa le pide una contraseña al usuario:
master_ps = 'Misiontic2022'
guest_ps = 'jk45jk'
password = input('Input password: ')

if password == master_ps:
    print('===============')
    print('ACCESS COMPLETE')
    print('===============')
elif password == guest_ps:
    print('==============')
    print(' GUEST ACCESS')
    print('==============')
else: 
    print('==============')
    print('ACCESS DENIED')
    print('==============')