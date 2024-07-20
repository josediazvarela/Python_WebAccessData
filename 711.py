# Program 7.11 from book. It reads line by line a file with upper
try:
    man_file=open("E:\TRAINING\Python_Coursera\Programming\mbox-short.txt")
except:
    print("An error have ocurried ...")
archivo=man_file
for i in archivo:
    print (i.upper())

