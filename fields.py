# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

lines = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    index = line.find(':') + 1
    lines.append(float(line.strip()[index:]))


total = 0
count = 0

for x in lines:
    total += x
    count += 1

average = total / count

print("Average spam confidence:", average)
