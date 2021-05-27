lista1 = ['Adrian','Natalia','Carlos','Octavio']
lista2 = ['Fabian','Jose','Fernando']
#TODO: Concatenar las dos listas
nueva_lista = lista1 + lista2
print(nueva_lista)
#TODO: Emplear el operador *
nueva_lista = lista1 * 3
print(nueva_lista)
#TODO: Recortar las cadenas
lista3 = nueva_lista[2:4]
print(lista3)
lista3 = nueva_lista[2:5]
print(lista3)
#TODO: Modificar el contenido de la lista en el [i]-ésimo elemento
lista3 = lista2
print(lista3)
lista2[2] = 'Andrea'
lista3 = lista2
print(lista3)
lista2[2] = 4
lista3 = lista2
print(lista3)
lista2[2] = 5.3
lista3 = lista2
print(lista3)