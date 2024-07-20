# This program enters a fioe name from keyboard and it counts number of lineas
# when it finds the word "Subject:"

narchivo=input("Enter path for the flat file to work:> ")
try:
    man_a=open (narchivo)
except:
    print ('Do not open a file that not exist ..')
    exit()
    
contador=0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador=contador+1
print("The number of lines that start witn Subject is: ",contador)

