# 8.5 Abra el archivo mbox-short.txt y léalo línea por línea. Cuando encuentre una línea que comience con 'De '
# como la siguiente línea:
# De stephen.marquard@uct.ac.za sábado 5 de enero 09:14:16 2008
# Analizará la línea De usando split() e imprimirá la segunda palabra en la línea (es decir, la dirección completa d
# e la persona que envió el mensaje). Luego imprima un recuento al final.
# Sugerencia: asegúrese de no incluir las líneas que comienzan con 'De:'. Mire también la última línea del resultado
# de muestra para ver cómo imprimir el recuento.
#
# Puede descargar los datos de muestra en http://www.py4e.com/code3/mbox-short.txt


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "data.txt"

fh = open(fname)
count = 0
correos = []

for line in fh:
    words = line.split()
    if not words:
        continue
    elif words[0] == "From":
        correos.append(words[1])

count = len(correos)

for i in correos:
    print(i)

print("There were", count, "lines in the file with From as the first word")
