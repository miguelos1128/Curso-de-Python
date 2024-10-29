def add (a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def calculator():
    while True:
        print("Seleccione una operación")
        print(" 1. Suma")
        print(" 2. Resta")
        print(" 3. Mutiplicación")
        print(" 4. Division")
        print(" 5. Exit")

        options = input("Ingrese su opcion del 1 al 5: ")

        if options == "5":
            print("Saliendo de la calculadora")
            break

        if options in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if options == "1":
                print("La suma es:", add(num1, num2))
            elif options == "2":
                print("La resta es:", subtract(num1, num2))
            elif options == "3":
                print("La multiplicación es:", multiply(num1, num2))
            elif options == "4":
                print("La división es:", divide(num1, num2))
        else:
            print("Opción inválida, intenta de nuevo")

calculator()
        