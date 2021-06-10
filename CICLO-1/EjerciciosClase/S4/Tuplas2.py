# Semana 4 - Clase 4 - Tuplas - Ejercicio 2
# TODO: Usar unpacking para separar la tupla
tupla1 = (1, 'a', 2, 'b', 3, 'c', 3.14151698)
a,b,c,d,e,f,g = tupla1
print('El valor de a = ',a)
print('El valor de b = ',b)
print('El valor de c = ',c)
print('El valor de d = ',d)
print('El valor de e = ',e)
print('El valor de f = ',f)
print('El valor de g = ',g)
'''
IMPORTANTE: Al usar unpacking se seben asociar TODOS los índices, de lo contrario
habrá un error al desempaquetar

NOTA 1: Se pueden usar las herramientas de las listas
    Ejemplo: Imprimir la longitud de la tuplaö

NOTA 2: Para crear una tupla con un único elemento es necesario poner una coma
al final del elemento

NOTA 3: NO SE PUEDE reasignar elementos en las tuplas como se suele hacer con
las listas
    Ejemplo: tupla(1,2,3)
             tupla[1] = 'a'
        Resultado: 
'''
print(len(tupla1))

tupla2 = tuple('Casa')
# Resultado -> ('C', 'a', 's', 'a') 
print(tupla2)

tupla2 = tuple('Casa',)
# Resultado -> ('C', 'a', 's', 'a') 
print(tupla2)

tupla2 = ('Casa',)
# Resultado -> ('Casa',) 
print(tupla2)