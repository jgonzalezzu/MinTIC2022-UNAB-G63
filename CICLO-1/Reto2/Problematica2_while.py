print('Problematica2 - with WHILE loop')
#Variable de control de entrada
horas = 0
trabajadores = int(1)
#Declaración de variables
valor_hora = float(input('Ingrese el valor de la hora > '))
total_horas = int(0)
#Mensaje de interfaz
print('===============================================')
print('Para finalizar el registro de horas ingrese -1')
print('===============================================')
while horas != -1:
    horas = int(input('Ingrese las horas del trabajador >'))
    sueldo = valor_hora * horas
    total_horas += horas 
    trabajadores +=1
    print('horas del trabajador >', horas,'Sueldo del trabajador >', sueldo)
trabajadores -= 2
total_horas += 1
print('Número total de trabajadores                          > ', trabajadores)
print('Número total de horas trabajadas por los trabajadores > ', total_horas)
print('Costo total del del sueldo de los trabajaodres        > ', total_horas * valor_hora)