import numpy as np


def createArrayMensaje(mensaje,alfabeto):
    arrayMensaje=[]
    mensajeLow=mensaje.lower()
    for caracter  in mensajeLow:
        for i,valor in enumerate(alfabeto):
            print(f"\nindice:{i} Valor:{valor}")
            
            if caracter==valor:
                    arrayMensaje.append([i])
    return arrayMensaje



alfabeto=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
print("""
      1)Encryptar
      2)Desencryptar
      """)
op=int(input("Que desea realizar"))
match op:
    case 1:
         i=0
    case 2:
        print("Desencriptar mensaje")
       
        
    case 3:
        print("Salir del programa")
        



mensaje=input("Ingresa tu mensaje")
print(createArrayMensaje(mensaje,alfabeto))
