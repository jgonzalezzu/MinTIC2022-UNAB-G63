# Semana 6 - Clase 1 - Métodos de busqueda Iterativo - Ejercicio 1 - Modulo para script 1
'''
Ejemplos de módulo empleados anteriormente: limpiar pantalla, raíz cuadrada.

Def: Es un código que almacenta datos, que permiten su reutilización
'''

def suma(x,y):
    print('Sa suma de los números es = ',x+y)

def resta(x,y):
    print('La resta de los números es = ',x-y)

def producto(x,y):
    print('El producto de los números es = ',x*y)

def division(x,y):
    try:
        resultado = x/y
        print('La división de los números es = ', resultado)
    except ZeroDivisionError:
        print('No puedes dividir por cero')
    except Exception as unknowError:
        print('Ha ocurrido el error -> ',unknowError)