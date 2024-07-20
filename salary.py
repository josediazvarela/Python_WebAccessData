hrs = input("Enter Hours:")

if float(hrs) > 40 :
    e = float(hrs) - 40
    hrs=40.0
else :
    e = float(0)


# print(float(e)*1.5*10.50)
# print (float(hrs)*10.50)
s = float(e)*1.5*10.50 + float(hrs)*10.50    
print(s)

