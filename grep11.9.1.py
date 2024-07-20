import re
cont=0
x=input ("Enter a regular expression: ")
fhand= open ('E:\TRAINING\Python_Coursera\Programming\mbox-short.txt')
for linea in fhand:
    linea=linea.rstrip()
    if (re.search(x,linea)):
        cont=cont+1
    else:
        continue
print ('El archivo mbox-short tiene :' +str(cont) + ' lineas que coinciden')
        
