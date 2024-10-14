squares = [x**2 for x in range(1,11)]
print("cuadrados:", squares)

#°F = (9/5 * °C + 32)
celsius = [0, 10 , 20, 30 , 40]
farenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Temperatura en °F:", farenheit)


#numeros Pares
envens = [x for x in range (1,21) if x%2 ==0]
print(envens)
#numeros In Pares
impares = [x for x in range (1,21) if x%2 !=0]
print(impares)

matrix =  [[1,2,3],
           [4,5,6],
           [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range (len(matrix[0]))]

print(matrix)
print(transposed)

#Código en varias lienas de código

transposed = []
for i in range (len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print("Transpuesta",transposed)
print("**************** Ejercios:***************")

##Retos del la clase

#1.Doble de los Números
    #Dada una lista de números [1, 2, 3, 4, 5], 
    # crea una nueva lista que contenga el doble 
    # de cada número usando una List Comprehension.

lista = [1, 2, 3, 4, 5]

doble_lista = [x*2 for x in lista]
print(doble_lista)

# 2. Filtrar y Transformar en un Solo Paso
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] 
# y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

words = ["sol", "mar", "montaña", "rio", "estrella"]

filtered_words = [word.upper() for word in words if len(words) >3]
print(filtered_words)

# Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas:
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

personas_of_madrid = [name["nombre"] for name in personas if name["ciudad"]=="Madrid" and name["edad"] > 30 ]
print(personas_of_madrid)

# List Comprehension con un else
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
# crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers2 = [number*2 if number%2 ==0 else number for number in numbers]
print(numbers2)