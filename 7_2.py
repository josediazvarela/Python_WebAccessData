# This program gets the average of the number each line in X-DSPAM in a file
# It reads a file by keyboard


# Read the file by keyboard
archivo=input ("Enter name of file its path complete:> ")
# Capture the manejador
try:
    fsal=open(archivo)
except:
    print("The filename is incorrect ... ")
    if archivo=="na na boo boo":
        print ("wtf SAY ...")
    exit()
acum=0.0
cont=0
a=len('X-DSPAM-Confidence:')

for linea in fsal:
    if linea.startswith('X-DSPAM-Confidence:'):
        l=linea[a:]
        acum= float(l)+float(acum)
        cont=cont+1

print("The average is :> ",acum/cont)
    


