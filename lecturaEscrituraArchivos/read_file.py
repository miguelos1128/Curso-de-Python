#leer un archivo liena por linea

with open('cuento.txt', 'r') as file: # type: ignore
    for lineas in file:
        print(lineas)

#Leer todas las lineas en una lista
"""with open('cuento.txt',  'r') as file:
    lines =  file.readlines()
    print(lines)"""

#Añadir texto
"""with open('cuento.txt',  'a') as file:
    file.write("\n\nBy:Miguel angel ")"""

#Sobre escribir el texto
"""with open('cuento.txt',  'w') as file:
    file.write("\n\nBy:ChatGPT111")"""