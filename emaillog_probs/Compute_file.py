# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        text = line.strip()
        num = text.find(':')
        ev = line[num+1:]
        decimal = float(ev)
        #print(decimal)
        total = total + decimal
        count = count + 1
        #print(count)
print("Sum of values in the given line:", total)
print("Total number of lines:" ,count)
average = total/count
print("Average spam confidence: ",average)
