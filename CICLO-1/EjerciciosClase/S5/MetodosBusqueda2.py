# Semana 5 - Clase 3 - Métodos de busqueda Iterativo  - Ejercicio 2

def crear_lista():
    size = int(input('Cuántos elementos tiene la lista? » '))
    lista = []
    for elemento in range(size):
        elemento = int(input('Ingrese elemento de lista » '))
        lista.append(elemento)
    return lista


def biseccion(valor_buscado,lista):
    inicio = 0
    fin = len(lista)
    while inicio <= fin:
        mitad = (inicio+fin)//2
        if valor_buscado == lista[mitad]:
            return mitad
        elif valor_buscado > lista[mitad]:
            inicio=mitad+1
        elif valor_buscado < lista[mitad]:
            fin = mitad+1
    return None

lista = crear_lista()
# lista_ordenada = lista.sort()
# print(lista_ordenada)
print(lista)