# Este es otro ejemplo de como manejar data de un json desde disco.
import json
suma=0.0
with open(r'E:\TRAINING\Python_Coursera\Programming\c.json') as json_file:
    data = json.load(json_file)

print(data)

# Ahora si quiero extraer un dato en particular por ejemplo el precio de la bicicleta
print (data['store']['bicycle']['price'])
# Si quiero extraer un dato de arreglo jason ( o lista en python )
print(data['store']['book'][1]['title'])

# Ahora si quiero sumar los precios de todos libros hago
for i in data['store']['book']:
    print (i['price'])
    suma=float(suma)+ float(i['price'])
print ('Toatal suma de libros es: ', suma)

# Puedo usar un condicional dentro de in lazo asi:
books = data['store']['book']
for book in books:
    if book['price'] <= 10.00:
        print(book)
