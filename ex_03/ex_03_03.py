score = input("Enter Score: ")
try:
    x = float(score)
except:
    print("Wront score")
if 0.0 < x > 1.0:
    print("Score is out of range")
elif x >= 0.9:
    print("A")
elif x >= 0.8:
    print("B")
elif x >= 0.7:
    print("C")
elif x >= 0.6:
    print("D")
elif x < 0.6:
    print("F")