# Programa buenaso trabaja con listas, tuplas, diccionarios y ordenamientos
# Este trabaja con letras de un archivo (lee, hace lista, remueve simbolos extranos, convierte en letras minusculas, hace diccionario y ordena

import string 
f_hand = open ('words.txt')
lista= list()
dic = dict()
for linea in f_hand:
    linea=linea.rstrip()
    # Aqui elimino simbolos extranos de puntuacion y hago minusculas todas la letras
    linea=linea.translate(linea.maketrans('','',string.punctuation))
    linea=linea.lower()
    # genero la "lista" de palabras separadas por blanco para cada linea 
    lista_palabras=linea.split()
    # a cada palabra de la lista necesito dividirla en letras para eso hago un diccionario de letras
    for palabra in lista_palabras:
        # descompongo cada palabra en letras (el item(palabra) pasa a ser un string)
        s=palabra
        for i in s[0:]:
            # Aqui elaboro el diccionario
            if i not in dic:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
# Ahora ya con el diccionario listo lo hago tupla y luego lista y ordeno ( en una sola instruccion
lista= list(dic.items())
# Recuerdo que os ordenamientos van solo en listas y tuplas (no en diccionarios)
lista.sort()
for  clave, valor in lista:
    print (str(clave)+' '+str(valor))

    
    
    




           
