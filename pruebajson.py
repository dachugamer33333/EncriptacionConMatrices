import json

matriz=[[x for x in range(10)] for x in range (10)]
matrizMensaje=[[1]for x in range(7)]
for fila in matriz:
    print(fila)

print(matrizMensaje)

almacen={
    "matriz":matriz,
    "matrizMensaje":matrizMensaje
}

with open("/hola/matrices.json","w") as archivo:
    json.dump(almacen,archivo,indent=1)