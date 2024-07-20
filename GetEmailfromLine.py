fname = input("Enter file name: ")

# I wil get 0 because it isn't open yet.
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
   # print(line)
    wds = line.split()
   # print(wds)
    if len(wds)==7 and wds[0]=='From':
        print(wds[1])
        count=count+1

print("There were", count, "lines in the file with From as the first word")
