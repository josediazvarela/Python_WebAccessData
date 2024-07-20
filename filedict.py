
# Ojo dar el path completo sin comillas

fname = input('Ingresa el nombre de archivo: ')
try: fhand = open(fname)
except:
    print('El archivo no se puede abrir:', fname)
    exit()
# I initialize my dictionary 
counts = dict()
# I'll take the file line by line
for line in fhand:
    # I'll split each line in words separated by blank and I'll put in a list called words
    # It's automatically
    words = line.split()
    # I'll take word from the list called words
    for word in words:
        if word not in counts:
            counts[word] = 1
        else: counts[word] += 1
print(counts)

