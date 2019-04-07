#Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the hour
#out from the 'From ' line by finding the time and then splitting the string a
#second time using a colon.Once you have accumulated the counts for each hour,
#print out the counts, sorted by hour as shown below.

fname = input("Enter the file name: ")
fhand = open(fname)
temp = dict()
count = 0
list = []
for line in fhand:
    if line.startswith("From "):
        text = line.rstrip()
        words = text.split()
        period = words[5]
        time = period.split(':')
        #print(time)
        hour = time[0]
        temp[hour] = temp.get(hour, 0) + 1
#print(temp)
list = sorted(temp.items())
for (k,v) in list:
    print(k,v)
quit()


        #print(hour)
        #count = count + 1
#print(count)
