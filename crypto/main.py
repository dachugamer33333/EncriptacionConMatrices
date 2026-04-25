
import random
def encriptar(matriz, mensaje):
    filas_A = len(matriz)
    columnas_A = len(matriz[0])
    filas_B = len(mensaje)
    columnas_B = len(mensaje[0])

    if columnas_A != filas_B:
         print("No se pueden multiplicar")
         return None
    
    resultado = [[0 for _ in range (columnas_B)] for _ in range (filas_A)]
    print(resultado)
    
    for i in range(filas_A):
         for j in range(columnas_B):
              for k in range(columnas_A):
                   resultado[i][j] += matriz[i][k] * mensaje[k][j]
                   #print(f"i:{i} j:{j} k:{k}")
                   
                  
            #mantenemos dentro del alfabeto 
              #resultado[i][j] = resultado[i][j] % len(alfabeto)
                 
     
    return resultado
            
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
print("""
     1)Encryptar
     2)Desencryptar

""")
option=int(input("Que desea realizar:"))





mensaje=input("Ingrese el mensaje que desea encriptar: ")
mensajeEncryptado=""
alfabeto=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
arrayMensaje=createArrayMensaje(mensaje)
matrizAleatoriav=matrizAleatoria(mensaje)



for filas in arrayMensaje:
     for valor in filas:
          mensajeEncryptado+=f"{str(valor)}-"
print(mensajeEncryptado)

for filas in matrizAleatoriav:
     print()
     
print(encriptar(matrizAleatoriav,arrayMensaje))

