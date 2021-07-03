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