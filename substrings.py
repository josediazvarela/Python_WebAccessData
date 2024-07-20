# Use the file name mbox-short.txt as the file name
# hay que averiguar como usar input con path, solo coge en el path de python

fname = input("Enter file name: ")
fh = open(fname)
n=0.0
cont=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
#    print(line)
    l=line
    cont=cont+1
#    print (float(l[20:]))
    n= float(l[20:]) + float(n)
    
# print("Done")
print ("Average spam confidence:", n/cont)
