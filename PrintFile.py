# Im gonna use words.txt in the directory 'E:\TRAINING\Python_Coursera\Programming\'
# Use words.txt as the file name
fname = input("Enter file name: ")
# a = "c:\ResumeSanJose\" + fname
fh = open( fname)
for linea in fh:
   linea=linea.rstrip()
   print(linea.upper())
    
