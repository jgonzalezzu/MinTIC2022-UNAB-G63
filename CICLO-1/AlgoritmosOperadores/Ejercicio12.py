print("Ejercicio 12")
'''
    4 inversionistas crean una empresa y hacen un aporte a ca_
    pital, el programa debe obtener el porcentaje que le per_
    tenece a cada inversionista basado en el valor de la in_
    versión inicial.
'''
print('Este programa calcula el valor segun el porcentaje de inversion')
inv1 = float(input('Ingrese el valor del primer inversionista: '))
inv2 = float(input('Ingrese el valor del segundo inversionista: '))
inv3 = float(input('Ingrese el valor del tercer inversionista: '))
inv4 = float(input('Ingrese el valor del cuarto inversionista: '))
total = inv1 + inv2 + inv3 + inv4
P_inv1 = (inv1/total)*100
P_inv2 = (inv2/total)*100
P_inv3 = (inv3/total)*100
P_inv4 = (inv4/total)*100
print('El total invertido es: ', total)
print('El porcentaje del primer inversionista es: ', P_inv1)
print('El porcentaje del segundo inversionista es: ', P_inv2)
print('El porcentaje del tercer inversionista es: ', P_inv3)
print('El porcentaje del cuarto inversionista es: ', P_inv4)