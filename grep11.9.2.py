import re
cont=0
tot=0.0
f=0.0
# x=input ("Enter a regular expression: ")
fhand= open ('E:\TRAINING\Python_Coursera\Programming\mbox-short.txt')

for linea in fhand:
    linea=linea.rstrip()
    # Ojo x es una lista ( la funcion devuelve una lista y var ver si es nulo ocupo LEN
    x=re.findall('^New Revision: ([0-9.]+)',linea)
    if len(x)>0:
        # ahora debo pasar la lista a string (es solo un elemento)
        s=x[0]
        # Ahora paso el string a flotante
        f=float(s)+f
        cont=cont+1
print ('El promedio es: ',str(f/cont))
    
 
        
