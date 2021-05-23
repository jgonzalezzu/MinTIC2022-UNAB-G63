#Semana 2 - Clase 3 - Condicionales - Ejercicio 3
#Ahora se usan los operadores booleanos
user = 'DevAccess'
master_pw = 'MisionTIC'
user_input = input('Usuario: ')
ps_input = input('Contraseña: ')
if user_input == user and ps_input == master_pw:
    print('==============')
    print('   ACCESS')
    print('==============')
else: 
    print('==============')
    print('ACCESS DENIED ')
    print('==============')
