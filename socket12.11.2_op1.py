import socket
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
misock.send(cmd)
while True:
    datos = misock.recv(32)
    if len(datos) == 32:
        print ('******Esto es 32 caracteres*******')
    elif len(datos)<1 : break
    
    print(datos.decode(),end='')
misock.close()
