nota = "   Hola    "

# # Imprimir desde la tercera letra hasta la ultima primera letra
# print(nota[2:])
#
# # Imprimir desde la primera letra hasta la tercera letra
# print(nota[:3])
#
# # Imprimir desde la primera letra hasta la ultima letra
# print(nota[:])
#
# # Imprimir desde la primera letra hasta la ultima letra saltando de 2 en 2
# print(nota[::2])
#

# for n in nota:
#     print(n)

text = "X-DSPAM-Confidence:    0.8475"
start_position = text.find(':') + 1    # Encuentra la posición del ':' y suma 1 para omitir el espacio
number_str = text[start_position:]     # Obtiene la subcadena a partir de la posición encontrada
# number = float(number_str)             # Convierte la subcadena en un número de punto flotante
print(number_str)
