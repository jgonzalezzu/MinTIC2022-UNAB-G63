print("Ejercicio 10")
'''
    Se desea saber que porcentaje de hombres y qué porcentaje de
    mujeres hay en un salón.
'''
cant_hombres = int(input('Ingrese la cantidad de hombres: '))
cant_mujeres = int(input('Ingrese la cantidad de mujeres: '))
total = cant_hombres + cant_mujeres
P_hombres = (cant_hombres/total)*100
P_mujeres = (cant_mujeres/total)*100
print('El porcentaje de hombres es: ', P_hombres,'%')
print('El porcentaje de mujeres es: ', P_mujeres,'%')