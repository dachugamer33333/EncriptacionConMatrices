
import random
mensaje=input("Ingrese el mensaje que desea encriptar: ")
alfabeto=[" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
arrayMensaje=[]
for i,valor in enumerate(alfabeto):
    print(f"\nindice:{i} Valor:{valor}")
    for caracter in mensaje:
        if caracter==valor:
            arrayMensaje.append(i)

print(f"array mensaje={arrayMensaje}")
"""
diccionario={letra: i for i, letra in enumerate(alfabeto) }

print("||ENCRYPTADOR||")
#n*1
vector=[[[diccionario][letra]for letra in mensaje ]
# comparandado cada letra con un numero (es ineficiente)
#entonces cual es la otra manera de hacerlo

"""




def encriptar():
    #n=tamaño del mensaje
    sizeMessage=len(mensaje)
    #n*n
    encriptador=[[random.randint(1,10) for i in range(4)]for x in range(4)]
    print(encriptador)
    """
    #es la formula de la multiplicacion de matrices
    resultado = [[sum([i][k] * B[k][j] for k in range(cols_A))
              for j in range(cols_B)]
             for i in range(filas_A)]
    i=0
    """

encriptar()