#This program find a substring in a file
man_a=open('E:\TRAINING\Python_Coursera\Programming\mbox-short.txt')
for linea in man_a:
    linea=linea.rstrip()
    if linea.find('@uct.ac.za')==-1:
        continue
    print(linea)
