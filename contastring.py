palabra=input ('Entry string: ')
letra1=input ('Entry letter to find: ')
def contastring (palabra, letra1) :
    #palabra='banana'
    contador=0
    for letra in palabra:
        if letra ==letra1:
            contador=contador+1
    print (contador)

contastring (palabra, letra1)
