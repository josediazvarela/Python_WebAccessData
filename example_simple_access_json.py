# Es es un ejemplo simple ara accesar un archivo json
import json

myfile='E:/TRAINING/Udemy/PowerBI/OtherDataSources/data1.json'
str_data=open(myfile).read()
json_data=json.loads(str_data)
cont=0

for a in json_data:
    # print (a)
    print (a["transactions"][0])
    #print('name' in entry)
    #cont=cont+1
    #print (cont)
    
