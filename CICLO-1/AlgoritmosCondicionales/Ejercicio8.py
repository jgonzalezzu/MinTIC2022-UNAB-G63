print('Este programa te pedirá que ingreses NOMBRE, EDAD Y SEXO')
#TODO: Este programa solo imprime si la persona es de sexo masculino y mayor de edad
name = input('Ingresar nombre: ')
sex = input('Ingrese sexo M o F: ').upper()
age = int(input('Ingrese edad: '))
if sex == 'M' and age >= 18:
    print('| Name |', name, '|')
    print('| Sex  |', sex, '|')
    print('| Age  |', age, '|')