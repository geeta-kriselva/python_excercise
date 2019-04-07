# Checking, if user input number is prime a number. if not printing all the facors.
n= input("Enter the number: ")
try:
    num = int(n)
except:
    print("Enter only integer number")
    quit()
if num > 1:
    factor = []
    a = 0
    for i in range(2,num+1):

        if (num % i) == 0:
           factor.insert(a,i)
           a = a + 1



    #if len(factor) <= 1:
            #print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
        for i in range (len(factor)):
            print("The factor is: ", factor[i])


else:
    print(num, "is a prime number")
