# Librerías]
import json
import os
import time
import io
# Superusuario
root_user = str('julian.gonzalez2')
root_pswd = str('julian.gonzalez2')

# Definición de funciones 
def cls():
    if os.name == "posix":
        var = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    return os.system(var)
    
def login():
    file_usuarios = open('.\\usuarios.json','r')
    content = file_usuarios.read()
    credenciales = json.loads(content)
    contador_intentos = 1
    max_intentos = 3
    while contador_intentos <= max_intentos:
        try:
            x = str(input('     Ingrese el usuario >   '))
            y = str(input('     Ingrese contraseña >   '))
            if (x == root_user) and (y == root_pswd):
                print('        × ACCESO ROOT » OK ×')
                menu_control_usuarios()                

            elif y == credenciales[x]:
                print('        × ACCESO CONCENIDO ×')
                file_usuarios.close()
                time.sleep(1)
                cls()
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
        except KeyError:
            print('Usuario no existe!')
            time.sleep(1)
            cls()
        
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
    print('| × Exportar notas   |    8   |')
    print('| × Salir            |    0   |')
    print('_______________________________')
    print()
    menu_option = input_validation_type(1,'Ingrese una opción del menú » ')
    return menu_option

def ingreso_notas(lista_notas):
    cant = input_validation_type(1,'Ingrese la cantidad de notas > ')
    for i in range(cant):
        x = input_validation_type(2,'Ingrese nota > ')
        if (x>0) and (x<=5):
            lista_notas.append(x)
            print('Nota registrada = ',x)
        elif (x>5) and (x<=50):
            x=x/10
            lista_notas.append(x)
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

def guardar_notas(file_name):
    print('Función en construcción')

def menu_control_usuarios():
    print('1. Ver usuarios y contraseñas')
    print('2. Agregar usuario')
    print('3. Eliminar usuario')
    print('0. Salir')
    root_opcion = int(input('Ingrese opción » '))
    return root_opcion;

def root_menu():
    opcion_root = menu_control_usuarios()
    while opcion_root != 4:
        if opcion_root == 1:
            print('Ver usuarios y contraseñas')
        elif opcion_root == 2:
            print('Agregar usuario')
        elif opcion_root == 3:
            print('Eliminar usuario')
        else:
            exit()