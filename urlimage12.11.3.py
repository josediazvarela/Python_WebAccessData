import time
import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
man_a = open('portada.jpg', 'wb')
tamano = 0
acum=0
while True:
    info = img.read(1000)
    acum=acum+len(info)
    if acum==3000:
        print ('*******SO FAR I HAVE 3000 CHARACTERS***********')
        time.sleep(10)
    if len(info) < 1:
        break
    tamano = tamano + len(info)
    print('El tamano cambio a: ',tamano)
    man_a.write(info)
print(tamano, ' Total caracteres copiados.')
man_a.close()
