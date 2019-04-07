#Write a program to read through the mbox-short.txt and figure out who has sent
#the greatest number of mail messages. The program looks for 'From ' lines and
#takes the second word of those lines as the person who sent the mail. The
#program creates a Python dictionary that maps the sender's mail address to a
#count of the number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum loop to find
#the most prolific committer.

fname = input("Enter file name: ")
fh = open(fname)
count = 0
list1 = []
address = dict()
for line in fh:
    if line.startswith("From "):
        text = line.rstrip()
        words = text.split()
        name = words[1]
        address[name] = address.get(name, 0) + 1
#print(address)
bigcount = None
mailadd = None
for name,count in address.items():
    if bigcount is None or count > bigcount:
        mailadd = name
        bigcount = count
print(mailadd, bigcount)
quit()
