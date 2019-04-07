# Compute the sum of numbers in a series until the final sum is less than 50
total = 0
i = 1
while total <= 50:
    total = total + i
    i = i + 1

print ("Sum of numbers is: ", total )
i = i - 1
print ("The last number added in series is: ",i)
quit()
