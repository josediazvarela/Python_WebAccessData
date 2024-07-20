# Python para leer desde un archiv grabado en disco
# json file 
# C:\Users\JOSELUIS\AppData\Local\Programs\Python\d.json 
  
import json 
 
# Opening JSON file 
f = open(r'C:\Users\JOSELUIS\AppData\Local\Programs\Python\b.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 

for i in data['emp_details']: 
    print(i)
    print (i['email'])
f.close()

