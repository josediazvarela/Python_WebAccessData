# Programa buenaso trabaja con listas, tuplas, diccionarios y ordenamientos

import string 
f_hand = open ('mbox-short.txt')
lista= list()
dic = dict()
dicc=dict()
for linea in f_hand:
    linea=linea.rstrip()
    # Analizo aqui las lineas que empiezan con From
    if not linea.startswith ('From '):
        continue
    # genero la lista de palabras separadas por blanco para cada linea 
    palabras=linea.split()
    # escoges la segunda palabra correspondiente a correo
    print (palabras[1])
    # Voy a generar el diccionario contando los mas repetidos "clave-valor"
    if palabras[1] not in dic:
        dic[palabras[1]]=1
    else:
        dic[palabras[1]]=dic[palabras[1]]+1
print(dic)
print (" =========== TENGO EL OBJETIVO DEL PROGRAMA =========")
# Ahora voy hacer del diccionario "dic" una tupla y lo voy a poner en una lista "lista"
# Tambien ordenare la lista de acuerdo al valor y no a la clave (orden descendente)
for clave,valor in list(dic.items()):
    # Ojo genero una lista con 2 parametros
    lista.append((valor,clave))
lista.sort(reverse=True)
print (lista)
