import numpy as np
import random as rd
import json
import os
def encriptar():

    def createArrayMensaje(mensaje,alfabeto):
        arrayMensaje=[]
        mensajeLow=mensaje.lower()
        for caracter  in mensajeLow:
            for i,valor in enumerate(alfabeto):
                print(f"\nindice:{i} Valor:{valor}")
                
                if caracter==valor:
                        arrayMensaje.append([i])
        arrayMensaje=np.array(arrayMensaje)
        return arrayMensaje
    def matrizAleatoria(mensaje):
        #n=tamaño del mensaje
        sizeMessage=len(mensaje)
        #n*n
        det=0
        while(det==0):
            encriptador=np.array([[rd.randint(1,10) for i in range(sizeMessage)]for x in range(sizeMessage)])
            det = np.linalg.det(encriptador)
            print(f"determinante:{det}")

        return encriptador
    alfabeto=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    def createclavePublica(arrayMensaje,encryptador):
        clavePublica= encriptador @ arrayMensaje
        return clavePublica
        
    print("||Encriptar mensaje||")
    mensaje=input("Cual es el mensaje que desea encriptar?")
    arrayMensaje=createArrayMensaje(mensaje,alfabeto)
    print(arrayMensaje)
    encriptador=matrizAleatoria(mensaje)
    print(encriptador)
    clavePublica=createclavePublica(arrayMensaje,encriptador)
    print(clavePublica)
    almacen={
        "encryptador":encriptador.tolist()
    }
    alamacen_c={
        "clavePublica": clavePublica.tolist()
    }

    ruta = input("Donde desea guardar (Enter para carpeta actual): ")

    if ruta == "":
        ruta = "encryptador.json"
        ruta2 = "clavePublica.json"
    else:
        ruta2 = ruta + "_clavePublica.json"
        ruta = ruta + "_encryptador.json"

    
    carpeta = os.path.dirname(ruta)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)

    with open(ruta, "w") as archivo:
        json.dump(almacen, archivo, indent=1)

    with open(ruta2, "w") as archivo:
        json.dump(alamacen_c, archivo, indent=1)
    
    
    
    

def desencriptar():
    
    print("Desencriptar mensaje")
    desencriptable=input("Ingresa el json de matriz mensaje: ")
    clave=input("Ingrese el json de la matriz clave: ")
    resultado= desencriptar()
    print(resultado)




print("""
      1)Encryptar
      2)Desencryptar
      """)
op=int(input("Que desea realizar"))
match op:
    case 1:
        encriptar()
    case 2:
        desencriptar()
    case 3:
        print("Salir del programa")
        



