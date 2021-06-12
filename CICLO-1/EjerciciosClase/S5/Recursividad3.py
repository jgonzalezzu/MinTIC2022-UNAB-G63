# Semana 5 - Clase 2 - Recursividad  - Ejercicio 3
#TODO: Hacer un juego que pregunte un color, preguntando de manera repetitiva hasta adivinar el color oculto

color_oculo = str('MAGENTA')

def pregunta_color():
    control_entrada = True
    color = str(input('Adivina el color » ')) 
    while control_entrada == True:
        if color == color_oculo:
            print('FELICITACIONES!! Has adivinado el color')
            control_entrada = False
            return control_entrada
        else:
            print('Ups! Ese no era')
            pregunta_color()
            control_entrada == True
            return control_entrada

pregunta_color()