import json
datos = dict()
datos={'nombre':'Julian','Apellido':'Gonzalez','edad':22}
with open('./datos.json','w') as archivo:
    json.dump(datos,archivo)