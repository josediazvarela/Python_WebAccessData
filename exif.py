# Program to deploy notes of students
# Poner esta intruccion afuera del procedimiento
# n = input ('note: ')
# Cuando llames al procedimiento correr como "notas (float(n))"
def notas (n):
    try:
        if n >= 0.9 and n <=1.0 :
            print("Excelent")
        elif n > 0.8 :
                print ("Notable")
        elif n >0.7 :
                print ("bien")
        elif n> 0.6 :
                print ("sufficient")
        elif n<=0.6 and n >=0.0 :
                print ("insufficient")             
        else :
            print ("Wrong parameter")
    except:
        print ("Perhaps you are intenting entry a value not correct...")
        
            
