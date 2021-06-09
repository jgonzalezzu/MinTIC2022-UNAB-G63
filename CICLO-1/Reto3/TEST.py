# Versión de construcción del reto 3 de forma simplificada
estudiantes = []
definitivas = []
cantidad_estiantes = int(input('Ingrese la cantidad de estudiantes > '))
opcion_menu = 0
while opcion_menu != 8:
    print('Menú')
    try:
        opcion_menu = int(input('Ingrese la opción del menú'))
    except ValueError:
        print('Ingrese opción válida!')
    if opcion_menu == 1:
        sumar_notas = float(0)
        promedio = float(0)
        for estudiante in range(cantidad_estiantes):
            nombre = str(input('Ingrese nombre del alumno'))
            for nota in range(3):
                calificaion = float(input('Ingrese la nota del alumno > '))
                sumar_notas += calificaion
            promedio=sumar_notas/3
            definitivas.append(promedio)
    if opcion_menu == 2:
        for nota in definitivas:
            print(definitivas[nota])