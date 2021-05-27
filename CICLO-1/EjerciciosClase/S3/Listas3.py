#Semana 3 - Clase 2 - Listas - Ejercicio 3
#TODO: el comando list permite generar listas
a = list(range(0,5))
b = list(range(0,5))
c = a
d = b[:]
e = a + b
f = b[:1]
g = b[0]
c[0] = 100
d[0] = 200
e[0] = 300
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)