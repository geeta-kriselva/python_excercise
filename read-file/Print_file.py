#Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
#Also print the total number of lines in the file.

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("The file", fname, "does not exist")
    quit()
fread = fhand.read()
fstrip = fread.rstrip()
#final = fstrip.capitalize()
print("\n", fstrip.upper())
count = 0
fhand = open(fname)
for line in fhand:
    count = count + 1
print("\nTotal number of lines are: ",count)
