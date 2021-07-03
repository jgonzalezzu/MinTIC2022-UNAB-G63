print('========================================')
print('           Problemática 1')
print('========================================')
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

==========================
USUARIO : 1234
CONTRASEÑA : 1234
==========================

Notas:
    - Las notas del estudiante va de 0 a 5.
    - La nota aprobada es 3
    - Recuerde validar los datos y controlar las excepciones
    - En el desarrollo del programa se deben implementar al menos dos funciones en la solución
'''
# Librerías
import os
import time
import statistics

# Variables de control
opcion = 10
validacion_entrada_notas = True
user = str('1234')
passwrd = str('1234')

# Variables de operación
estudiantes = {} #varible de almacenamiento de datos
notas=[] # Variable para almacenar las notas de cada estudiante
definitivas = [] # Variable para almacenar las definitivas

# Definición de funciones 
def cls():
    if os.name == "posix":
        var = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    return os.system(var)
    
def login():
    contador_intentos = 1
    max_intentos = 3
    while contador_intentos <= max_intentos:
        x = str(input('     Ingrese el usuario >   '))
        y = str(input('     Ingrese contraseña >   '))    
        if (x == user) and (y == passwrd):
            print('        × ACCESO CONCENIDO ×')
            break
        else:
            print('Usuario o contraseña incorrectos! Tiene', max_intentos - contador_intentos, ' intentos de ', max_intentos)
            contador_intentos += 1        
            if contador_intentos == max_intentos+1:
                cls()
                print('Ha exedido el máximo de intentos')
                time.sleep(2)
                cls()
                print('=============================================')
                print('   FIN DEL PROGRAMA POR MAXIMO DE INTENTOS  ')
                print('=============================================')
                exit()      
    return;

def input_validation_type(type,message):
    # Usar 1 para validad enteros
    # Usar 2 para validad flotantes
    error_time_delay = 2
    control_int = 1
    control_float = 1    
    if type == 1:
        while control_int == 1:
            try:
                value = int(input(message))
                control_int = 0
            except ValueError:
                print('Error de tipo / Opción inválida')
                time.sleep(error_time_delay)
                # cls()
            except TypeError:
                print('Error de tipo / Opción inválida')
                time.sleep(error_time_delay)
                # cls()
            except Exception as error_detectado:
                print('Error detectado! -> ', error_detectado)

    elif type == 2:
        while control_float == 1:
            try:
                value = float(input(message))
                control_float = 0
            except ValueError:
                print('Error de tipo / Opción inválida')
                time.sleep(error_time_delay)
                cls()
            except TypeError:
                print('Error de tipo / Opción inválida')
                time.sleep(error_time_delay)
                cls()
            except Exception as error_detectado:
                print('Error detectado! -> ', error_detectado)
    else:
        print('El valor ingresado no se puedes comprobar')
    
    return value;

def menu():
    print('_______________________________')
    print('| × Función          | Opción |')
    print('| × Agregar nota     |    1   |')
    print('| × Ver nota         |    2   |')
    print('| × Promedio         |    3   |')
    print('| × Extremos         |    4   |')
    print('| × Aprobados        |    5   |')
    print('| × Reprobados       |    6   |')
    print('| × Limpiar listas   |    7   |')
    print('| × Salir            |    0   |')
    print('_______________________________')
    print()
    menu_option = input_validation_type(1,'Ingrese una opción del menú » ')
    return menu_option

def ingreso_notas():
    cant = input_validation_type(1,'Ingrese la cantidad de notas > ')
    for i in range(cant):
        x = input_validation_type(2,'Ingrese nota > ')
        if (x>0) and (x<=5):
            notas_estudiante.append(x)
            print('Nota registrada = ',x)
        elif (x>5) and (x<=50):
            x=x/10
            notas_estudiante.append(x)
            print('Nota registrada = ',x)
        else:
            print('Error! Ingrese una nota entre 0 y 5')
    print('------------------------------------')
    print('Notas registradas satisfactoriamente')
    print('------------------------------------')
    time.sleep(1)
    cls()

def action_confirmation(message):
    action = bool()
    x = str()
    validation_control = 0
    while validation_control == 0:
        try:
            x = str(input(message)) 
            validation_control = 1           
        except TypeError:
            print('Error de tipo')
            validation_control = 0
        except Exception as error_detectado:
            print('Error detectado -> ', error_detectado)
            validation_control = 0           
        
        if (x=='s') or (x=='S'):
            action = True
        elif (x=='n') or (x=='N'):
            action = False
        else:
            print('Ingrese una opción válida')
        validation_control = 1
    return action;

# Ejecución del programa
login()
while opcion != 0:
    opcion = menu()
    if opcion ==1:
        cls()
        cant_estudiantes = input_validation_type(1,'Ingrese la cantidad de estudiantes > ')
        for i in range(cant_estudiantes):
            notas_estudiante=[]
            estudiante = str(input('Ingrese el nombre del estudiante > '))
            if estudiante not in estudiantes:
                entrada_notas = ingreso_notas()
                notas.append(notas_estudiante)
                entrada = {estudiante:notas_estudiante}
                estudiantes.update(entrada)
                cls()
            else:
                print('===========================================')
                print('Estudiante ya existe, intentelo nuevamente')
                print('===========================================')
                time.sleep(2)
                cls()

    elif opcion ==2:
        print(' × Ver notas ×')
        if len(estudiantes)!=0:
            cls()
            for key in estudiantes:
                print(key, '\t', estudiantes[key])
                time.sleep(0.2)
        else:
            print('Notas vacías! Debe ingresar estudiantes y notas primero')
            time.sleep(2)
            cls()

    elif opcion ==3:
        print(' × PROMEDIO ×')
        time.sleep(1)
        cls()
        definitivas.clear()
        if len(estudiantes)!=0:
            for i in notas:
                promedio_alumno = round(statistics.mean(i),1)
                definitivas.append(promedio_alumno)

            contador_def = 0 #Usado para enumerar las definitivas   
            for i in definitivas:
                contador_def +=1
                print(f'Definitiva #{contador_def} = ',i)
            print('--------------------------------------------------------')
            print('     El promedio del grupo es = ', round(statistics.mean(definitivas),2))
            print('--------------------------------------------------------')

        else:
            print('Notas vacías! Debe ingresar estudiantes y notas primero')
            time.sleep(2)
            cls()

    elif opcion ==4:
        print(' × Extremos ×')
        time.sleep(1)
        mayor = None
        menor = None
        cls()
        # leer lista para promedio
        if len(definitivas) != 0:
            for valor in definitivas:
                if mayor is None or valor > mayor:
                    mayor = valor
            for valor in definitivas:
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

    elif opcion ==5:
        print(' × APROBADOS ×')
        time.sleep(1)
        aprobados = int(0)
        N = len(definitivas)
        cls()
        if len(definitivas) != 0:
            for i in range(N):
                if definitivas[i] >= 3:
                    aprobados+=1
            print('===========================')
            print('Alumnos APROBADOS > ',aprobados)
            print('===========================')
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()

    elif opcion ==6:
        print(' × REPROBADOS ×')
        time.sleep(1)
        reprobados = int(0)
        N = len(definitivas)
        cls()
        if len(definitivas) != 0:
            for i in range(N):
                if definitivas[i] < 3:
                    reprobados+=1
            print('===========================')
            print('Alumnos REPROBADOS > ',reprobados)
            print('===========================')
        else:
            print('Notas vacías. Debe ingresar la notas primero, seleccione op. 1 >')
            time.sleep(3)
            cls()

    elif opcion ==7:
        print('limpiar listas')
        if action_confirmation('Desea eliminar las listas? S/N > ') == True:
            estudiantes.clear()
            notas.clear()
            definitivas.clear()
            print('las listas se han LIMPIADO!!')
            time.sleep(2)
            cls()
        else:
            print('Listas no serán limpiadas')
            time.sleep(2)
            cls()
        
    elif opcion ==0:
        if action_confirmation('Desea cerrar el programa? S/N > ') == True:
            break

    else:
        print('Ingrese una opción válida!')
        time.sleep(1)
        cls()
        
cls()
print('======================')
print('   FIN DEL PROGRAMA   ')
print('======================')