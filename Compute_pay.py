# compute pay using function
def computepay(h,rph):
    if h<=40:
        pay = h*rph
        return pay
    else:
        h1 = h-40
        p1 = h1*1.5*rph
        p2 = 40*rph
        pay = p1+p2
        return pay


hrs = input("Enter hours:")
rate = input("Enter rate per hour:")
try:
    h = float(hrs)
    rph = float(rate)
except:
    print("Enter only numeric values")
    quit()
payment = computepay(h,rph)
print(payment)
