def computepay(hours,rate):
    try:
        h=float(hours)
        r=float(rate)
        if h>40:
            reg = h * r
            opt = (h-40.0) * (0.5 * r)
            pay = reg + opt
            return pay
        else:
            return h * r
    except :
        pass

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print("Pay",p) 
    