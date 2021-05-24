#Semana 2 - Clase 4 - Estructuras Iterativas - Ejercicio en clase 1
#TODO: For Cree un proograma que muestre n primeros números y los sume
n = int(input('Ingrese límite superior de la sumatoria: '))
sumatoria = 0
for i in range(0,n+1):
#range(limite superior, límite inferior, paso entre elementos)
    sumatoria+=i
    print(i)
print('El valor de la sumatoria: ', sumatoria) 