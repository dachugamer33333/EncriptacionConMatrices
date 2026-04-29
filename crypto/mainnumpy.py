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
    while(len(mensaje) == 0):
         mensaje=input("Cual es el mensaje que desea encriptar?")
    arrayMensaje=createArrayMensaje(mensaje,alfabeto)
    
    print(f"Arreglo del mensaje:\n{arrayMensaje}")
    encriptador=matrizAleatoria(mensaje)
    print(f"Arreglo Aleatorio nxn:\n{encriptador}")
    clavePublica=createclavePublica(arrayMensaje,encriptador)
    print(f"Matriz Encryptada(Mensaje):\n{clavePublica}")
    almacen={
        "encryptador":encriptador.tolist()
    }
    almacen_c={
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
        json.dump(almacen_c, archivo, indent=1)
   

    
    
    
    

def desencriptar(alfabeto):
    arrayMensaje=[]
    mensaje=""
    alfabeto=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    try:
        clavePublica=input("Brindame la clave Publica: ")
        with open(clavePublica) as archivo:
            clavePublica=json.load(archivo)
        clavePublica=np.array(clavePublica["clavePublica"])
        print(f"Clave pública cargada:\n{clavePublica}")
        encryptador=input("Brindame el encriptador: ")
        with open(encryptador) as archivo:
            encryptador=json.load(archivo)
        encryptador=np.array(encryptador["encryptador"])
        print(f"Encryptador cargado:\n{encryptador}")
        inversaEncryptador=np.linalg.inv(encryptador)
        print(f"Inversa del encryptador:\n{inversaEncryptador}")
        MensajeFinal= inversaEncryptador @ clavePublica
        print(f"Mensaje final (sin redondear):\n{MensajeFinal}")
        MensajeFinal=np.round(MensajeFinal).astype(int)
        MensajeFinal=MensajeFinal.tolist()
        print(f"Mensaje final (redondeado):\n{MensajeFinal}")
        for caracter in MensajeFinal:
                for caracter2 in caracter:
                

                    for i,valor in enumerate(alfabeto):
                    
                    
                        if i==caracter2:
                                arrayMensaje.append([valor])
        for filas in arrayMensaje:
            for fila2 in filas:
                mensaje+=fila2
        print(f"||Resultado|| \n mensaje: {mensaje}")
    except FileNotFoundError:
     print("Error: no se encontró el archivo, verifica la ruta")
    except json.JSONDecodeError:
        print("Error: el archivo no tiene formato JSON válido")
    except KeyError as e:
        print(f"Error: no se encontró la clave {e} en el JSON")
    except np.linalg.LinAlgError:
        print("Error: la matriz no tiene inversa")
   

    



alfabeto=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

while True:
    print("""
        ||Programa encryptador||
        
        1)Encryptar
        2)Desencryptar
        3)salir
        """)
    op=int(input("Que desea realizar:"))
    match op:
        case 1:
            encriptar()
        case 2:
            desencriptar(alfabeto)
        case 3:
            print(">>>>>>>")
            break
            
            
        



