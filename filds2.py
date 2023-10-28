# Abra el archivo romeo.txt y léalo línea por línea. Para cada línea, divida
# la línea en una lista de palabras usando el método split().
#  El programa debería crear una lista de palabras. Para cada palabra en cada línea,
#  verifique si la palabra ya está en la lista y, si no, agréguela a la lista.
#  Cuando se complete el programa, ordene e imprima las palabras resultantes en el orden sort()
#  de Python como se muestra en el resultado deseado.
# Puede descargar los datos de muestra en http://www.py4e.com/code3/romeo.txt


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for i in line:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)


