import json
with open('./datos.json') as archivo:
    datos = json.load(archivo)
    for key,value in datos.items():
        print(f'clave : {key} - value: {value} ')