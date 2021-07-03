# Semana 7 - Clase 2 - JSON  - Ejercicio 1
'''
Operaciones básicasL
    - Crear un archivo
    - Abrir un archivo
    - Cerrar un archivo
    - Extender un archivo
Modos de 
'''
cadena_texto = 'MisionTIC 2021 - Unab \n linea creada con el código'
archivo = open('texto.txt','w')
# r+ permite hacer lectura y escritura con un solo modo
archivo.write(cadena_texto)
archivo.close()