import urllib.request, urllib.parse, urllib.error
import re
import ssl
import socket
# Ignorar errores de certificado SSL
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
url = input('Introduzca la url: ')
# convierto a lista la direccion web separado por '/'
lista=url.split('/')
# i'm gonna look for the host(server)
print(lista)
try:
       if len(lista)>=3 and (lista[0].strip()=='http:' or lista[0].strip()=='https:') \
          and lista[1].strip() ==''  and lista[2].strip() != None:
              s=lista[2].strip()
              print (s)
       elif len(lista) >=1  and lista[0].strip() !='http:' and lista[0].strip() !='https:':
              s=lista[0].strip()
              print (s)
       else:
              
              print('Un error en la escritura de la direccion ha ocurrido... revise')
    
except:
       print(' Error: Un error en la escritura de la direccion ha ocurrido... revise')

misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect((s, 80))

# cmd = '\'GET http://'+ s+'/romeo.txt'+ ' HTTP/1.0\r\n\r\n\''+str('.encode()')
cmd = 'GET http://'+s+'/romeo.txt'+ ' HTTP/1.0\r\n\r\n'
print(cmd)
print('Ojo verifico si esta como string o bytes? ',type(cmd))
# Tengp que enviar como bytes no como str
cmd1=cmd.encode()
print(cmd1)
print('Verifico que sea bytes si no es asi no prodria enviar: ',type(cmd1))

misock.send(cmd1)
# misock.send('\'GET http://'+ y1+'/romeo.txt'+ ' HTTP/1.0\r\n\r\n\''+str('.encode()'))
while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(),end='')
misock.close()

