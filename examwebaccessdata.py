# Documento XML en la web a usar es:    http://py4e-data.dr-chuck.net/comments_42.xml
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
suma=0
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
# Este es el API KEY del Dr Chuck, y esta asociado a este service url
# sobre el cual montare la direccion del archivo xml.
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'

else :
    #Este else es tomado de otro ejemplo del Dr Chuck
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# aqui ingreso la direccion del xml file
address = input('Enter location: ')
if len(address) < 1:
    quit
# creo el diccionario para pasar la direccion del archivo xml

url=address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
# print('Retrieved', len(data), 'characters')

    
commentinfo = ET.fromstring(data)
results = commentinfo.findall('comments/comment')
# print('total ', len(results))

# Ahora tomo los datos que me interesan
for item in results:
    # print ('count: ',item.find('count').text)
    suma=suma+ int(item.find('count').text)
print (suma)

    
