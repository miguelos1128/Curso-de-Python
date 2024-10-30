add = lambda a, b: a + b
print(add(10,8))

multiply = lambda a, b: a * b
print(multiply(10,4))

#Cuadrado de cada número
numbers = range(11)
square_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrados:", square_numbers)

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Pares:", even_numbers)