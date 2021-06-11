# Semana 5 - Clase 1 - Métodos de ordenamiento Iterativo  - Ejercicio 3 - Ejercicio 1
# Método burbuja
def ordenamiento_upper_lower(x):
    size = len(x)
    for i in range(size):
        for j in range(size):
            print(f'Lista i :{x[i]} - lista j {x[j]}')
            if x[i]>x[j]:
                variable_temporal = x[i]
                x[i] = x[j]
                x[j] = variable_temporal
    for elemento in x:
        print(elemento)

def ordenamiento_lower_upper(x):
    size = len(x)
    for i in range(size):
        for j in range(size):
            print(f'Lista i :{x[i]} - lista j {x[j]}')
            if x[i]<x[j]:
                variable_temporal = x[i]
                x[i] = x[j]
                x[j] = variable_temporal
    for elemento in x:
        print(elemento)

lista = []
cant_datos = int(input('Cuántos valores desesa ingresar? >'))
for i in range(cant_datos):
    #TODO: Se usa la f para poder ingresar variables entre llaves
    dato = int(input(f'Ingrse un valor #{i}> '))
    lista.append(dato)

for i in lista:
    print(i)

print('''
\n ORDENAMIENTO DE VARIALBES 
--------------------------------
1. Ordenar de menor a mayor
2. Ordenar de mayor a menor
-------------------------------
''')
try:
    opcion = int(input('Ingrese su opción > '))
except TypeError:
    print('Ingrese solo números enteros')
    
if opcion == 1:
    ordenamiento_lower_upper(lista)
elif opcion == 2:
    ordenamiento_upper_lower(lista)
else:
    print('Ingrese una opción válida')

