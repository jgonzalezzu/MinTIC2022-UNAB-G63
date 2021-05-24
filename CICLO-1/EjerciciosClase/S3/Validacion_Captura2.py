#Semana 3 - Clase 1 - Validación y captura de Excepciones - Ejercicio 1
#TODO: Se puede meter try y except dentro de while
try:
    numero = int(input('Ingrese uin número >'))
except ValueError:
    print('Ingrese un número entero')