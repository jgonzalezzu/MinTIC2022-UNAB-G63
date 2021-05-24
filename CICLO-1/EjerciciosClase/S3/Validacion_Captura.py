#Semana 3 - Clase 1 - Validación y captura de Excepciones - Ejercicio 1
numero1 = int(input('Ingrese un  número: '))
numero2 = int(input('Ingrese un  número: '))
try:
    division = numero1/numero2
except ZeroDivisionError:
    print('No se puede realizar la división')
except TypeError:
    print('Error de valores')
except ValueError:
    print('No se puden dividir los valores')
except Exception as error:
    print('Error desconocido ->', error)
#finally: realiza la acción por defecto, siempre se está ejecutando
finally:
    print('Bloque finally')