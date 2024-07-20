# Count how many emails each persona has sent to me. I'm gonna use mbox-short.txt
# Ojo!! te saca ademas el maximo valor y la correspondiente clave del diccionario
import operator
import string
fname = input('Ingresa el nombre de archivo: ')
try:
    fhand = open(fname)
except:
    print('El archivo no se puede abrir:', fname)
    exit()
counts = dict()
for line in fhand:
    # remove blanks for right and left side
    line = line.rstrip()
    # I'm gonna identify each line that starts with from
    if line.startswith('From '):
        # I'm gonna convert the line in a  list named words separated by blank
        words = line.split()
        print(words)
        # Now, I search each word in the list named words
        if words[1] not in counts:
            counts[words[1]]=1
        else:
            counts[words[1]]=counts[words[1]]+1

# a_dictionary = {"a": 1, "b": 2, "c": 3}
print("Imprimo los claves-valor del dictionario: ",counts)

print ("El valor maximo del diccionario correspomde al correo (usuario): ", max(counts.items(), key=operator.itemgetter(1))[0])
all_values = counts. values()
max_value = max(all_values) 
print("Y el numero de veces que ha interactuado es: ",max_value)            

