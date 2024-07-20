#This program add two lines to a file called escribir

fsal= open('E:\TRAINING\Python_Coursera\Programming\escribir.txt','w')
# print(fsal)
linea1="I do not give a damn \t if you wanna comunicate with me\n"
fsal.write(linea1)
linea2="But I miss you \t I have to acknowledge it..."
fsal.write(linea2)
fsal.close()

# Now I am gonna read it
fsal=open('E:\TRAINING\Python_Coursera\Programming\escribir.txt')
for linea in fsal:
    print (linea)






