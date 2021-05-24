#Semana 2 - Clase 4 - Estructuras Iterativas - Ejercicio en clase 1
#TODO:While Cree un proograma que muestre n primeros números y los sume
n = int(input('Ingrese el límite superior de la sumatoria: '))
suma = 0
number = 0
while number <= n:
    print(number)
    number+=1
    suma += number
print('La sumatoria es: ', suma)