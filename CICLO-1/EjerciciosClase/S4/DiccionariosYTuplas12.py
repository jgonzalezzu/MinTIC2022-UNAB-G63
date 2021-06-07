# Semana 4 - Clase 2 - Diccionarios y tuplas - Ejercicio 12
# TODO: Diccionario con el número como clave y el apellido como valor de la seleccion colombia
jugadores = {}
option = 0
print('1. Ingresar jugadores')
print('2. Mostrar jugadores')
print('-1. Salir del programa')
while option != -1:
    try: 
        option = int(input('ingrese opción del menú > '))
    except ValueError:
        print('Ingrese una opción válida')

    if option == 1:
        jugador = str(input('Ingrese el nombre del jugador'))
        num_jugador = int(input('Ingrese el número característico del jugador'))
        valor = {jugador:num_jugador}
        jugadores.update(valor)

    if option == 2:
        if len(jugadores) == 0:
            print('Error! Lista de jugadores vacía')
        else:
            # print(jugadores)
            # TODO: Se puede usar un for para poder imprimir la lista de forma más organizada
            for clave in jugadores:
                print(clave,' - ', jugadores[clave])

print('====================')
print('  FIN DEL PROGRAMA  ')
print('====================')