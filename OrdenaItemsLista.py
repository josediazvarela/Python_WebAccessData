fname = input("Enter file name: ")
fh = open(fname)  # this is the handle of file
lst = list()  # initialize a list with null
s = list()
for line in fh:   # line is not a number. it is a line of text
    line.rstrip()
    l=line.split()   # it's a string y im gonna split in each word
    s=s+l
    # lst.append(l)    # add each line to the list "lst"
s.sort()    
# here remove repeared items
fin=[]
for i in s:
    if i not in fin:
        fin.append(i)


print (fin)
