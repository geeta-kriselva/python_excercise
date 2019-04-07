#Finding largest and smallest number from user input data
largest = None
smallest = None

while True:
    num = input ("Enter a number: ")
    if num == 'done':
        break
    try:
        number = int(num)
    except:
        print ("Invalid input")
        continue
#execute only once at the beginning of the program
    if largest is None:
        largest = number
        smallest = number
#begin comparison
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number
        continue
print ("Maximum is ", largest)
print ("Minium is ", smallest)
