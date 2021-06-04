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
    - Las notas del estudiante va de 0 a 5.
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

# Variables de control
opcion = 0
# Control de acceso
print('======================')
print('×       LOGIN        ×')
print('======================')

intentos = 3
contador_intentos = 1
ingreso_denegado = False
while contador_intentos <= intentos:
    usuario = str(input('Ingrese su usuario --> '))
    password = str(input('Ingrese su contraseña --> '))
    if (usuario == 'PROFESOR') and (password == 'PROFESOR'):
        print('Acceso concedido')
        break
    else:
        print('Usuario o contrasena erroneos!, intento > ', contador_intentos)
        contador_intentos += 1
        if contador_intentos == 3:
            ingreso_denegado = True

if ingreso_denegado == True:
    print('Ha excedido la cantidad de intentos')
    time.sleep(2)
    cls()
    opcion = -1

# Variables
lista = [] 
notas_finales = []
nombres = []
aprovados = int(0)
reprobados = int(0)
while opcion !=-1:
    try:
        opcion = menu()
    except ValueError:
        print('Error! Ingrese una opción válida')

    if opcion == 1:
        cls()
        nombres.clear()
        lista.clear()
        N = int(input('Ingrese la cantidad de estudiantes > '))
        m = int(input('Ingrese la cantidad de notas > '))
        for i in range(N):            
            lista.append([])
            print('====================================================')
            nombre = input('Ingrese NOMBRE DEL ESTUDIANTE > ')
            print('====================================================')
            nombres.append(nombre)
            for j in range(m):        
                try:
                    nota = float(input('Ingrese nota del estudiante > '))
                    print('Nota registrada')
                    if nota > 5:
                        nota = nota/10
                        lista[i].append(nota)
                    elif (nota > 0) and (nota <= 5):
                        lista[i].append(nota)
                    else:
                        print('Ingrese una nota entre 0 y 5')
                except TypeError:
                    print('Ingrese números únicamente')
                except	ValueError:
                    print('Ingrese números únicamente')
        cls()

    elif opcion == 2:
        cls()
        print('| × Ver notas × | Se pueda visualizar todas las notas registradas |')
        print('Nombre del estudiante | promedio')
        if len(lista) != 0:     
            for i in range(N):
                print(nombres[i],'\t ',lista[i])
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()

    elif opcion == 3:
        cls()
        print('| × Promedio × | Se visualiza la nota promedio del grupo |')
        group_sum = float(0)
        avg = float(0)
        sumatoria = float(0)
        nota_lectura = float(0)
        #Leer cada columna por fila y hacer el promedio
        if len(lista) != 0:
            print('Nombre del estudiante | promedio')
            for j in range(N):
                for i in range(m):
                    nota_lectura = lista[j][i]
                    sumatoria +=nota_lectura
                avg = round(sumatoria/m,1)
                notas_finales.append(avg)
                group_sum += avg
                avg = float(0)
                sumatoria = float(0)
            for j in range(N):
                print(nombres[j],'\t |', notas_finales[j])
            group_mean = round(group_sum/N,2)
            print('========================================')
            print('El promedio del grupo es > ', group_mean)
            print('========================================')
                
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()

    elif opcion == 4:
        mayor = None
        menor = None
        cls()
        print('| × Extremos × | Visualiza la nota mayor y menor del grupo |')
        # leer lista para promedio
        if len(notas_finales) != 0:
            for valor in notas_finales:
                if mayor is None or valor > mayor:
                    mayor = valor
            for valor in notas_finales:
                if menor is None or valor < menor:
                    menor = valor
            print('============================')
            print('La nota mayor es > ', mayor)
            print('la nota menor es > ', menor)
            print('============================')        
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()

    elif opcion == 5:
        aprovados = int(0)
        cls()
        print('| × Aprobado × | Visualiza la cantidad de estudiantes que APROBARON del grupo |')
        if len(notas_finales) != 0:
            for i in range(N):
                if notas_finales[i] >= 3:
                    aprovados+=1
            print('===========================')
            print('Alumnos APROBADOS > ',aprovados)
            print('===========================')
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()

    elif opcion == 6:
        reprobados = int(0)
        cls()
        print('| × Reprobados × | Visualiza la cantidad de estudiantes que REPROBARON del grupo |')
        if len(notas_finales) != 0:
            for i in range(N):
                if notas_finales[i] < 3:
                    reprobados+=1
            print('===========================')
            print('Alumnos REPROBADOS > ',reprobados)
            print('===========================')
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