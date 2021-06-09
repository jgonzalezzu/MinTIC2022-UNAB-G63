# Variables de control
opcion_menu = 0
# Variables a operar 
estudiantes = []
notas = []

while opcion_menu != 3:
    print('1. Ingresar notas ')
    print('2. Leer notas ')
    print('3. Salir del programa')
    try:
        opcion_menu = int(input('Seleccione un opción del menú > '))
    except TypeError:
        print('Error! Ingrese opción válida!')
    if opcion_menu == 1:
        try:            
            cantidad_estudiantes = int(input('Ingrese la cantidad de estudiantes > '))
        except TypeError:
            print('Error! Ingrese números enteros!')

        for i in range(cantidad_estudiantes):
            estudiante = str(input('Ingrese el nombre del estudiante >'))
            cantidad_notas = int(input('Ingrese cantidad de notas >'))
            estudiantes.append(estudiante)
            for j in range(cantidad_notas):
                nota = float(input('Ingrese nota > '))
                notas.append(nota)

    elif opcion_menu == 2:
        if len(estudiantes)==0:
            print('Error! lista vacía - No ha ingresado estudiantes')
        else:
            for i in range(cantidad_estudiantes):
                print(estudiantes[i],'\t',notas[i])

    elif opcion_menu == 3:
        exit
    else:
        print('Ingrese una opción válida!')

print('×× Fin del programa ××')