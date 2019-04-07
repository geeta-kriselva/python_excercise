# Compute grade for user input 
score = input("Enter Score: ")

try:
    s = float(score)
except:
    print("Enter a numeric value")
    quit()
if s<0.0 or s>1.0:
    print("Enter a value only between 0.0 to 1.0")
    quit()
if s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
else:
    s<=0.6
    print("F")
