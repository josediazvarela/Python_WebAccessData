# 
man_a = open('E:\TRAINING\Python_Coursera\Programming\mbox-short.txt')
for linea in man_a:
    # remove last charcater in each line
    linea = linea.rstrip()
    if linea.startswith('From:'):
        print(linea)
