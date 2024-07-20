# http://py4e-data.dr-chuck.net/comments_42.json - resp: 2553


#ste es un ejemplo con un archivo json leido desde la website s traves de un url
# El archivo al cual puedo accesar es:  http://py4e-data.dr-chuck.net/comments_42.json
import json
import urllib.request, urllib.parse, urllib.error
suma=0
jsonfile= input('Enter json file from a wersite here: ')
jf=urllib.request.urlopen(jsonfile).read()
info=json.loads(jf)
# Con estos dos prints de prueba verifico que los datos estan cargandose, no este vacio y el tipo de dato
# print ('total: ',len(info))
#print (info)
# print (type(info))

for item in info['comments']:
    #print(item['count'])
    suma=suma+item['count']
print(suma)    


