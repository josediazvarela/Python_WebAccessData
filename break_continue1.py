largest = None
smallest = None
cnt = 0
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    elif(num == ""):
         print("InValid num")
         break
    try :
        val = int(num)
        #print(val)
        #break
    except ValueError:
        val = -1
        print("Invalid input")
        continue


    if cnt == 0 :
        largest = val
        smallest = val
    elif val > largest :
        largest = val
    elif val < smallest :
        smallest = val

    cnt = cnt +  1  




print("Maximum is",largest)
print("Minimum is",smallest)