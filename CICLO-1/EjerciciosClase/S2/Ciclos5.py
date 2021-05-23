#Semana 2 - Clase 4 - Ciclos - Ejercicio 5
#Este programa combina un ciclo indefinido con una interrupción EXPLÍCITA del comando braek
#Este programa imprime lo que ingrese el usuario hasta ingresar la palabra 'fin'
while True:
    linea = input('> ')
    if linea == 'fin':
        break
    else:
        print(linea)
print('He terminado') 