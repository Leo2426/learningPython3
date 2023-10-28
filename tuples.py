# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "data.txt"

fh = open(fname)
count = 0
horas = {}

for line in fh:
    words = line.split()
    if not words:
        continue
    elif words[0] == "From":
        horas[words[5][:2]] = horas.get(words[5][:2], 0) + 1

for key, value in sorted(horas.items()):
    print(key, value)



