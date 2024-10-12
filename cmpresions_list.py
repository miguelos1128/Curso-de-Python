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