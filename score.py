score = input("Enter Score: ")
try:
    if float(score) >=0.9 and float(score)<=1.0:
        print ("A")
    elif float(score) >=0.8:
        print ("B")
    elif float(score) >=0.7:
        print ("C")
    elif float(score) >=0.6:
        print ("D")
    elif float(score) <0.6 and float(score)>=0:
        print ("F")  
    else:
        print ("You are out of range")
except:
    print("You have entried some incorrect value ...")
    