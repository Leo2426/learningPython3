dictionary = {
    "name": "Dictionary",
    "pages": 20,
    "author": "Leonardo Taype"
}
#
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())

# Recorrer el dictionary con key y value por seaparado
for key, value in dictionary.items():
    print(key, " : ", value)

# print(dictionary.get("name", "No hay esta propiedad"))


# Write a program to read through the mbox-short.txt and figure out who has sent the
# greatest number of mail messages. The program looks for 'From ' lines and takes the
# second word of those lines as the person who sent the mail. The program creates a Python
# dictionary that maps the sender's mail address to a count of the number of times they appear
# in the file. After the dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "data.txt"

fh = open(fname)
count = 0
correos = {}

for line in fh:
    words = line.split()
    if not words:
        continue
    elif words[0] == "From":
        correos[words[1]] = correos.get(words[1], 0) + 1

max = 0
max_email = ""

for key, value in correos.items():
    if value > max:
        max = value
        max_email = key

print(max_email, max)

