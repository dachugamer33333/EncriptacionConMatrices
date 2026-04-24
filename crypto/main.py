
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

    for caracter  in mensaje:
        for i,valor in enumerate(alfabeto):
            print(f"\nindice:{i} Valor:{valor}")
            
            if caracter==valor:
                    arrayMensaje.append(i)

    
    return arrayMensaje

mensaje=input("Ingrese el mensaje que desea encriptar: ")
alfabeto=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
#Array mensaje
print(createArrayMensaje(mensaje))
print(f"Matriz Mensaje:{createArrayMensaje(mensaje)} \n Matriz aleatoria:{matrizAleatoria(mensaje)}")
encriptar()
