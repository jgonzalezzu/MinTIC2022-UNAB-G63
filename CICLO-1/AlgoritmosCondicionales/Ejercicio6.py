print('Este programa calcula el salario de un obrero')
horas = int(input('Ingrese las horas trabajadas'))
v_hora = int(6000)
v_extra = int(10000)
h_base = int(40)
if horas <= h_base :
    salario = horas * v_hora
    print('El salario es: ', salario)
else:
    base = h_base * v_hora
    extras = (horas - 40) * v_extra
    salario = base + extras
    print('El salario con extras es: ', salario)