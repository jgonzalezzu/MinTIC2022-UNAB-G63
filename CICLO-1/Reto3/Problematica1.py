import math
import os
print('Problematica 1')
'''
Realice un programa en python que permita registrar las N estudiantes de un grupo y con ellos realizar
distintas operacinoes las cuales están descritas a continuación.

El programa solicita un login para acceder al menú principal donde un usuario pueda reazlizar las
siguiente operaciones.

| × Agregar nota | El usuario pueda agregar una nota nueva                       |
| × Ver notas    | Se pueda visualizar todas las notas registradas               |
| × Promedio     | Se visualiza la nota promedio del grupo                       |
| × Extremos     | Visualiza la nota mayor y menor del grupo                     |
| × Aprobado     | Visualiza la cantidad de estudiantes que APROBARON del grupo  |
| × Reprobados   | Visualiza la cantidad de estudiantes que REPROBARON del grupo |

Notas:
    - Las ntoas del estudiante va de 0 a 5.
    - La nota aprobada es 3
    - Recuerde validar los datos y controlar las excepciones
'''
# libraries
import os
import time
# UX console clear
if os.name == "posix":
    var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls" 
#functions
def cls():
    os.system(var)
def menu():
    print('| × Función      | Opción |')
    print('| × Agregar nota |    1   |')
    print('| × Ver nota     |    2   |')
    print('| × Promedio     |    3   |')
    print('| × Extremos     |    4   |')
    print('| × Aprobados    |    5   |')
    print('| × Reprobados   |    6   |')
    print('| × Salir        |   -1   |')
    menu_option = int(input('Ingrese una opción >'))
    return menu_option
# Control de acceso
usuario = str('Admin')
contrasena = str('4dm1n')

# Variables de control
opcion = 0
# Variables
lista = []
notas_finales = []
while opcion !=-1:
    try:
        opcion = menu()
    except ValueError:
        print('Error! Ingrese una opción válida')
    if opcion == 1:
        cls()
        N = int(input('Ingrese la cantidad de estudiantes >'))
        m = int(input('Ingrese la cantidad de notas >'))
        for i in range(N):
            lista.append([])
            for j in range(m):
                nota = float(input('Ingrese nota del estudiante > '))
                print('Working on that')
                # if nota > 5:
                #     nota = nota/10
                #     lista[i].append(nota)
                # elif (nota > 0) and (nota <= 5):
                #     lista[i].append(nota)
                # else:
                #     print('Ingrese una nota entre 0 y 5')
        cls()
    elif opcion == 2:
        cls()
        print('| × Ver notas × | Se pueda visualizar todas las notas registradas |')
        if len(lista) != 0:
            for i in range(N):
                print(lista[i])
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()
    elif opcion == 3:
        cls()
        print('| × Promedio × | Se visualiza la nota promedio del grupo |')
        avg = 0
        #Leer cada fila y hacer el promedio
        if len(notas_finales) != 0:
            for i in range(N):
                print(notas_finales[i])
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()
    elif opcion == 4:
        cls()
        print('| × Extremos × | Visualiza la nota mayor y menor del grupo |')
        # leer lista para promedio
        if len(notas_finales) != 0:
            for i in range(N):
                print(notas_finales[i])
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()

    elif opcion == 5:
        cls()
        print('| × Aprobado × | Visualiza la cantidad de estudiantes que APROBARON del grupo |')
        if len(notas_finales) != 0:
            for i in range(N):
                print(notas_finales[i])
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()
    elif opcion == 6:
        cls()
        print('| × Reprobados × | Visualiza la cantidad de estudiantes que REPROBARON del grupo |')
        if len(notas_finales) != 0:
            for i in range(N):
                print(notas_finales[i])
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()
    elif opcion == -1:
        cls()
        break
    else:
        print('Ingrese una opción del menú')
        time.sleep(3)
        cls()
        
print('========================')
print('  × Fin del programa ×  ')
print('========================')