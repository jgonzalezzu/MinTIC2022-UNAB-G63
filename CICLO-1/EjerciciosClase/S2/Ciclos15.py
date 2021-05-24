#Semana 3 - Clase 1 - Validación y captura de excepciones - Ejercicio 3
'''
Este programa le pide al usuario la clave con tres intentos permitidos
'''
#TODO: Usar while
contador = 1
while contador <=3:
    usuario = input('Ingrese le usuario: ').upper()
    password = input('Ingrese la clave: ')
    if usuario == 'NOMBRE' and password == '12345':
        print('Ingreso exitoso')
        break
    else:
        print('Acceso denegado, intento -> ', contador)
        contador+=1