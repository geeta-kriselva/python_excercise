fname = input("Enter the file name: ")
fhand = open(fname)
import re

x = sum([int(i) for i in re.findall('[0-9]+',fhand.read())])
print(x)

#Alternate method:
# for line in fhand:
#     text = line.rstrip()
#     if re.search('[0-9]+', text):
#         num = re.findall('[0-9]+',text)
#         num = [int(i) for i in num]
#         x = sum(num)
#         list.append(x)
# total = sum(list)
# print(total)
# quit()
