#Codigo para calcular el Factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factroial_5 = print(factorial(5))

#Codigo para calcular la serie de fibonacci

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return  fibonacci(n - 1) +  fibonacci(n - 2) 

number = 4
calcula_fibonacci = print("La serie de", number, "es:",fibonacci(number))

#La sumatoria de un número 
def sumatoria (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumatoria(n - 1)
    
numero = 4

calcula_sumatoria = print("La sumatoria del número ", numero, " es:", sumatoria(numero))