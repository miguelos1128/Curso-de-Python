try:
    divisor  =  int(input("Ingrssa un número divisor: "))
    result =  100/divisor
    print(result)
    
except ZeroDivisionError as e:
    print("Error: Eldivisor no puede ser 0")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Error: Debes introducir un número")
    print("Ha ocurrido un error: ", e)