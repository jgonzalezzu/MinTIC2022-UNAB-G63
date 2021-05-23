print("Ejercicio 9")
'''
   Calcular la candidad de segundos que están incluidos en el
   número de horas y minutos ingresados por el usuario
'''
print('Este programa calcula la cantidad de segundos en un tiempo ingresado')
t_hora = (int(input('Ingrese la cantidad de horas: ')))*3600
t_min = (int(input('Ingrese la cantidad de minutos: ')))*60
total = t_hora + t_min
print('La cantidad de segundos en el tiempo ingresado es:',total)