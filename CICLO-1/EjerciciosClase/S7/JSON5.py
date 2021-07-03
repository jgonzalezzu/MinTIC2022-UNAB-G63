# Semana 7 - Clase 2 - JSON  - Ejercicio 5
archivo = open('texto.txt','r')
archivo.seek(2)
lectura = archivo.read(12)
print(lectura)
archivo.close()