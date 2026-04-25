import json

datos=[];
with open("matrices.json") as archivo:
    datos=json.load(archivo)
matriz=datos["matriz"]

for fila in matriz:
    print(fila)
