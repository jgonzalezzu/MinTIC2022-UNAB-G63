# Semana 7 - Clase 2 - JSON  - Ejercicio 2
archivo = open('texto.txt','r')
datos = archivo.readlines()
archivo.close()
contador = 1
for linea in datos:
    print(f'línea de texto #{contador} » {linea}')
    contador +=1