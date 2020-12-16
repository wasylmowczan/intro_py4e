hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    rt = float(rate)
except: 
    print("Error, please enter numeric input")
if h>40 :
    reg = h * rt
    opt = (h-40.0) * (0.5 * rt)
    pay = reg + opt
else :
    pay = h * rt
print(pay)
    