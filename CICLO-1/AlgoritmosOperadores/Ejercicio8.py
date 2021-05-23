print("ejercicio 8")
'''
    un alumno desesa saber cuál será su calificación final en
    la materia.
    |Primer corte   | 30 %|
    |Segundo corte  | 30 %|
    |Parcial final  | 40 %|
'''
Primer_corte = (float(input('Ingrese la nota del primer corte')))*0.3
Segundo_corte = (float(input('Ingrese la nota del segundo corte')))*0.3
Parcial = (float(input('Ingrese la nota del Parcial final')))*0.4
Def = Primer_corte + Segundo_corte + Parcial
print('La definitiva es: ', Def)