# Count words (week-day) in a mbox-short.txt

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
        if words[2] not in counts:
            counts[words[2]]=1
        else:
            counts[words[2]]=counts[words[2]]+1
print(counts)
