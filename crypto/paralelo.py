
import random
def encriptar():
    """
    #es la formula de la multiplicacion de matrices
    resultado = [[sum([i][k] * B[k][j] for k in range(cols_A))
              for j in range(cols_B)]
             for i in range(filas_A)]
    i=0
    """
    

    
def matrizAleatoria(mensaje):
     #n=tamaño del mensaje
    sizeMessage=len(mensaje)
    #n*n
    encriptador=[[random.randint(1,10) for i in range(sizeMessage)]for x in range(sizeMessage)]
    return encriptador

def createArrayMensaje(mensaje):
    arrayMensaje=[]
    lower=mensaje.lower()
    for caracter  in lower:
        for i,valor in enumerate(alfabeto):
            print(f"\nindice:{i} Valor:{valor}")
            
            if caracter==valor:
                    arrayMensaje.append([i])

    
    return arrayMensaje

mensaje=input("Ingrese el mensaje que desea encriptar: ")
alfabeto=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
#Array mensaje
arrayMensaje=createArrayMensaje(mensaje)
matrizAleatoriav=matrizAleatoria(mensaje)
for filas in arrayMensaje:
     print(filas)

for filas in matrizAleatoriav:
     print(filas)
     
encriptar()

"""
[2, 8, 7, 2, 6, 6, 7], 
[5, 7, 2, 6, 4, 2, 4], 
[10, 6, 10, 6, 6, 4, 7], 
[4, 5, 7, 6, 2, 1, 5], 
[6, 8, 9, 6, 8, 9, 3], 
[6, 7, 1, 8, 5, 1, 8], 
[4, 1, 5, 7, 1, 5, 8]


"""