'''
 En vez de copiar los datos a la pantalla conforme va funcionando el programa,
 vamos a guardar los datos en una cadena, remover la cabecera,
 y después guardar los datos de la imagen en un archivo 
'''


import socket
import time
SERVIDOR = 'data.pr4e.org'
PUERTO = 80
acum=0
# It is preparing to use the socket
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect((SERVIDOR, PUERTO))
misock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
contador = 0
# Here I say that imagen variable must be stored as binary object ( or bytes). It hasa been inicialized with ""
imagen = b""
while True:
       datos = misock.recv(1000)
       acum=acum+len(datos)
       if acum ==3000:
              print("********SO FAR THERE'S A BLOCK OF 3000 BYTES------")
              time.sleep(10)  # I'll wait for 10 sec to see this message
       if len(datos) < 1: break
       #time.sleep(0.25)
       contador = contador + len(datos)
       print(len(datos), contador)
       imagen = imagen + datos
misock.close()
# Búsqueda del final de la cabecera (2 CRLF)
pos = imagen.find(b"\r\n\r\n")
print('Header length', pos)
print(imagen[:pos].decode())

# Ignorar la cabera y guardar los datos de la imagen (Ojo la imagen esta como binario or bytes)
imagen = imagen[pos+4:]

fhand = open("cosa.jpg", "wb")
fhand.write(imagen)
fhand.close()
