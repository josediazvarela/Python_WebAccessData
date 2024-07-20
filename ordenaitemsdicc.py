name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
listaacu=list()
listatemp=list()
dicc=dict()
for linea in handle:
    if linea.startswith('From '):
        listatemp=linea.split()
        listaacu.append(listatemp[5][0:2])
# print (listaacu)

listaacu.sort()
for i in listaacu:
    if i not in dicc:
        dicc[i]=1
    
    else:
        dicc[i]=dicc[i]+1

for clave, valor in list(dicc.items()):
    print(str(clave)+ ' '+str(valor)) 


