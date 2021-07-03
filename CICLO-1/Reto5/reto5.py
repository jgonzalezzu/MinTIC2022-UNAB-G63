print('========================================')
print('           Problemática 1')
print('========================================')
# Librerías
import os
import time
import statistics
import reto_mod as rm
import json

# Variables de control
opcion = 10
validacion_entrada_notas = True

# Variables de operación        
# estudiantes = {} #varible de almacenamiento de datos

# Ejecución del programa
rm.login()
archivo = open('.\\estudiantes.json','r+')
contenido = archivo.read()
estudiantes = json.loads(contenido)
while opcion != 0:
    opcion = rm.menu()
    if opcion ==1:
        rm.cls()
        cant_estudiantes = rm.input_validation_type(1,'Ingrese la cantidad de estudiantes »» ')
        for alumno in range(cant_estudiantes):
            codigo = str(input('Ingrese código del alumno » '))
            if codigo not in estudiantes:
                estudiante = {}
                Nombre = str(input('Ingrese nombre » '))
                Apellido = str(input('Ingrese Apellido » '))   
                Edad = int(input('Ingrese edad del estudiante »'))
                Grado = int(input('Ingrese grado del estudiante »'))
                notas = []
                nota = rm.ingreso_notas(notas)
                rm.cls()
                definitiva = round(statistics.mean(notas),1)   
                datos_estudiante = {"Nombre":Nombre,"Apellido":Apellido,"Edad":Edad,"Grado":Grado,"Notas":notas,"Definitiva":definitiva}
                estudiante = {codigo:datos_estudiante}
                estudiantes.update(estudiante)
            else:
                print('===========================================')
                print('Estudiante ya existe, intentelo nuevamente')
                print('===========================================')
                time.sleep(2)
                rm.cls()            

    elif opcion ==2:
        print(' × Ver notas ×')
        if len(estudiantes)!=0:
            rm.cls()
            print(
                'Apellido','\t',
                'Nombre','\t',
                'Edad','\t',
                'Grado','\t',
                'Notas','\t',
                'Definitivas','\t',
            )
            
            for estudiante in estudiantes:
                print(
                    estudiantes[estudiante]['Apellido'],'\t',
                    estudiantes[estudiante]['Nombre'],'\t',
                    estudiantes[estudiante]['Edad'],'\t',
                    estudiantes[estudiante]['Grado'],'\t',
                    estudiantes[estudiante]['Notas'],'\t',
                    estudiantes[estudiante]['Definitiva']
                    )
                time.sleep(0.2)
        else:
            print('Notas vacías! Debe ingresar estudiantes y notas primero')
            time.sleep(2)
            rm.cls()

    elif opcion ==3:
        print(' × PROMEDIO ×')
        time.sleep(1)
        rm.cls()
        definitivas = []
        definitivas.clear()
        if len(estudiantes)!=0:
            for estudiante in estudiantes:
                print(estudiantes[estudiante]['Apellido'],'\t',estudiantes[estudiante]['Nombre'],'\t',estudiantes[estudiante]['Definitiva'])
                nota = estudiantes[estudiante]['Definitiva']
                definitivas.append(nota)

            print('--------------------------------------------------------')
            print('     El promedio del grupo es = ', round(statistics.mean(definitivas),2))
            print('--------------------------------------------------------')

        else:
            print('Notas vacías! Debe ingresar estudiantes y notas primero')
            time.sleep(2)
            rm.cls()

    elif opcion ==4:
        print(' × Extremos ×')
        time.sleep(1)
        mayor = None
        menor = None
        rm.cls()
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
            rm.cls()

    elif opcion ==5:
        print(' × APROBADOS ×')
        time.sleep(1)
        aprobados = int(0)
        N = len(definitivas)
        rm.cls()
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
            rm.cls()

    elif opcion ==6:
        print(' × REPROBADOS ×')
        time.sleep(1)
        reprobados = int(0)
        N = len(definitivas)
        rm.cls()
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
            rm.cls()

    elif opcion ==7:
        print('limpiar listas')
        if rm.action_confirmation('Desea eliminar las listas? S/N > ') == True:
            estudiantes.clear()
            definitivas.clear()
            print('las listas se han LIMPIADO!!')
            time.sleep(2)
            rm.cls()
        else:
            print('Listas no serán limpiadas')
            time.sleep(2)
            rm.cls()

    elif opcion == 8:
        print('Guardas las notas a un archivo json')
        file_name = str(input('Nombre para el archivo json »'))
        archivo = open(f'.\\{file_name}.json','w')
        dict_json = json.dumps(estudiantes, indent=4)
        archivo.write(dict_json)
        archivo.close()
        
    elif opcion ==0:
        if rm.action_confirmation('Desea cerrar el programa? S/N > ') == True:
            break
        else:
            print('No se ejecutará la salida del programa')
            time.sleep(1)
            rm.cls()
            rm.m  
    else:
        print('Ingrese una opción válida!')
        time.sleep(1)
        rm.cls()
        
rm.cls()
print('======================')
print('   FIN DEL PROGRAMA   ')
print('======================')