import re
cont=0
suma=0

fhand= open (r'E:\TRAINING\Python_Coursera\Programming\b.txt')

for linea in fhand:
    linea=linea.rstrip()
    # print(linea)
    # Ojo x es una lista ( la funcion devuelve una lista, chequea nulo - ocupo LEN
    x=re.findall('([0-9]+)',linea)
    # print(x)
    if len(x)>0:
        i=0
        j=len(x)
        
              
        # ahora debo pasar la lista a string y kuego a entero( debo contar cuantos numeros tengo)
        for i in range(0,j,1) :
            s=x[i]
            # print (int(s))
            suma=int(s)+suma
            cont=cont+1
       
print ('La suma es : ',str(suma))
    
 
        
