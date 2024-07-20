palabra = 'brontosaurio'
d = dict()
# Here it catch the index (c) or position de each letter
for c in palabra:
    if c not in d:
        d[c] = 1
        print ("it give you the letter into word ",c)
        print (d[c])
    else: d[c] = d[c] + 1
print(d)
