# This program looks for each line with the word "From"

man_a = open('E:\TRAINING\Python_Coursera\Programming\mbox-short.txt')
contador = 0
for linea in man_a:
    if linea.startswith('From:'):
        print(linea)


