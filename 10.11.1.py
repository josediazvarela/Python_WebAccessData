# Programa buenaso trabaja con listas, tuplas, diccionarios y ordenamientos
# Este trabaja con horas pero es basicamente los mismo que el 10.11.1-JD

import string 
f_hand = open ('mbox-short.txt')
lista= list()
dic = dict()
for linea in f_hand:
    linea=linea.rstrip()
    # Analizo aqui las lineas que empiezan con From
    if not linea.startswith ('From '):
        continue
    # genero la "lista" de palabras separadas por blanco para cada linea 
    palabras=linea.split()
    # escoges la sexta palabra correspondiente a la hora ( sin minutos ni segundos)
    # Ojo palabra[5]= es el campo o palabra hora, [0:2]= es la hora ( sin minutos ni segundos de ese campo) o se substring
    print (palabras[5][0:2])
    # Voy a generar el diccionario contando los mas repetidos "clave-valor"
    if palabras[5][0:2] not in dic:
        dic[palabras[5][0:2]]=1
    else:
        dic[palabras[5][0:2]]=dic[palabras[5][0:2]]+1
print(dic)
print (" =========== TENGO EL OBJETIVO DEL PROGRAMA =========")
# Ahora voy hacer del diccionario "dic" una tupla y lo voy a poner en una lista "lista"
# Tambien ordenare la lista de acuerdo al valor y no a la clave (orden ascendente)
for clave,valor in list(dic.items()):
    # Ojo genero una lista con 2 parametros
    lista.append((clave,valor))
lista.sort()
# Ahora voy a imprimir cada hora en una linea separada y sin comillas
for hora in lista:
    s=hora
    print (str(s[0])+' '+str(s[1]))

                         
