largest = None
smallest = None

try: 
     
    while True:
        num = input("Enter a number: ")
        if num == "bob" : 
            print("Invalid input")
            continue
        if num == "done" : break
        if largest == None or smallest == None:
            largest=int(num)
            smallest=int(num)
        if int(largest)<int(num):
            largest=int(num)
        if int(smallest)>int(num):
            smallest=int(num)
        
        
        

#   Puedo imprimir aqui tambien print(largest)
#   print(smallest)

except:
    print("Value incorrect...")

print("Maximum is ", largest)
print("Minimum is ", smallest)
