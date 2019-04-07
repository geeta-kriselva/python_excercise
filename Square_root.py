#Finding the square root of a number
n = input("Enter the number: ")
try:
    num = int(n)
except:
    print("Enter only interger values")
    quit()

if num > 1:
    s = 0
    for i in range(2,num):
        if i**2 == num:
            s = i
            print("Square root is: ", s)
            break
    if s == 0:
        print("The given number is not a perfect square")
else:
    print("Enter only positive integer values")
quit()
