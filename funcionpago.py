def computepay(h,r):       
# hrs = input("Enter Hours:")
    if float(h) >40.0 :
        e=float(h) -40
        h=40.0
        s=float(e)*float(r)*1.5+float(h)*float(r)
    else:
        s=float(h)*10.5
    return s


h = input("enty worked hours")
r = input("entry rate each hour")
p = computepay(h,r)

print("Pay",p)
# return 42.37
