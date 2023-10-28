import re

field = open("data.txt")
lines = []
numbers = []
for line in field:
    number = re.findall("([0-9]+)", line)
    if len(number) < 1:
        continue
    else:
        for n in number:
            numbers.append(int(n))

print(sum(numbers))


