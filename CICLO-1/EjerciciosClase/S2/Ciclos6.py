#Semana 2 - Clase 4 - Ciclos - Ejercicio 6
#Este prorama se  usa para validar la entrada del ususario
while True:
    linea = input('> ')
    if linea[0] == '#': #Verifica que el primer caracter sea la almohadilla y continúa con el ciclo
        continue
    if linea == 'fin':
        break
    print(linea)
print('Terminado')