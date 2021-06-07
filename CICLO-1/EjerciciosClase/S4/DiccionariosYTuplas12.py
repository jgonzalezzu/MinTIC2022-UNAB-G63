# Semana 4 - Clase 2 - Diccionarios y tuplas - Ejercicio 12
# TODO: Diccionario con el número como clave y el apellido como valor de la seleccion colombia
import os
import time
def clear(): 
    os.system('clear') #on Windows System
clear()
jugadores = {}
option = 0
while option != 3:
    try:
        print('1. Ingresar jugadores')
        print('2. Mostrar jugadores')
        print('-1. Salir del programa')
        option = int(input('ingrese opción del menú > '))
    except ValueError:
        print('Ingrese una opción válida')


    if option == 1:
        clear()
        jugador = str(input('Ingrese el nombre del jugador > '))
        num_jugador = int(input('Ingrese el número característico del jugador > '))
        valor = {jugador:num_jugador}
        jugadores.update(valor)

    elif option == 2:
        if len(jugadores) == 0:
            print('Error! Lista de jugadores vacía! ')
            time.sleep(2)
            clear()
        else:
            clear()
            # print(jugadores)
            # TODO: Se puede usar un for para poder imprimir la lista de forma más organizada
            for clave in jugadores:
                print(clave,' - ', jugadores[clave])
                time.sleep(1)
    
    elif option == 3:
        exit_confirmation = str(input('Desea salir del programa S/N > '))
        if exit_confirmation == 'N':
            print('OK')
            time.sleep(2)
            clear()
            option = 0
        elif exit_confirmation == 'S':
            clear
            break
        else: 
            print('Ingrese una opción válida')

    else:
        print('Error! Ingrese una opción válida')
        time.sleep(2)
        clear()


print('====================')
print('  FIN DEL PROGRAMA  ')
print('====================')