# este programa te permite obtener el maximo de un diccionario construido previante de un archivo
name = input("Enter file:")
if len(name) < 1 : name = "E:\TRAINING\Python_Coursera\Programming\mbox-short.txt"

# try:
fhand = open(name)
# except:
#    print ('The file can not be opened')
#    exit()
 
lista=list()
dicc=dict()
for linea in fhand:
        # hago de linea una lista de palabras y la pongo en la variable lista
    if linea.startswith('From '):
            lista=linea.split()
            if lista[1] not in dicc:
                dicc[lista[1]]=1
            else:
                dicc[lista[1]]=dicc[lista[1]]+1

# paso a lista y listo con esta funcion
inverse = [(value, key) for key, value in dicc.items()]
# print(dicc)

print (max(inverse)[1], max(inverse)[0])
 
