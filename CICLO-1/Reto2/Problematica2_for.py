print('Problematica2 - with FOR loop')
#Declaración de variables
valor_hora = float(input('Ingrese el valor de la hora > '))
trabajadores = int(input('Ingrese el número de trabajadores > '))
total_horas = int(0)
for trabajador in range(1,trabajadores+1):
    horas = int(input('Ingrese las horas del trabajador >'))
    sueldo = valor_hora * horas
    total_horas = total_horas + horas  
    print('horas del trabajador >', trabajador,'Sueldo del trabajador >', sueldo)
print('Número total de trabajadores                          > ', trabajadores)
print('Número total de horas trabajadas por los trabajadores > ', total_horas)
print('Costo total del del sueldo de los trabajaodres        > ', total_horas * valor_hora)