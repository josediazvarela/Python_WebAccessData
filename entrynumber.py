# This program read numbers until you entry 'fin'.
# The program gets total, average, media
# This program can be done easier, but for practicing is made this way

def entrynumber ():
    contador=0.0
    total=0.0
    prom=0.0
    media=0.0
    indice=0
    val=0.0
    maxi=0.0
    mini=0.0
  
    try:
        while True:
            val = input ('Entry number:> ')
            if  val!='fin':
                total=float(val)+float(total)
                contador=float(contador)+1
                prom=float(total)/float(contador)
                media=float(total)/2
                if float(maxi)<float(val):
                    maxi=float(val)
                else:
                    if float(mini)>val:
                        mini=val
            else:
                break
        print('Total: ', total)
        print('Average: ',prom)
        print('Media: ', media)
        print('Maximo: ',maxi)
        print('Minimo: ',mini)
    except:
         print('You entry a wrong value, It accepts numbers only...')            


entrynumber()
