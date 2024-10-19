n = 5
if n>5:
    print("n es mayor que 5")
elif n==5:
    print("n es igual a 5")
else:
    print("n es menor que 5")
print("estamos Fuera del IF")    
x = 15
y =20
if x>10 and y>15:
    print("x y y son mayores que 10 y 15")

if x>10 or y>15:
    print("X es mayor que 10 o Y es mayo que 25")

if not x>20 :
    print("x no es mayor que 10")

#If anidados
is_meber = False
age =  15
if is_meber:
    if age >= 15:
        print("Bienvenido a la blblioteca ya que tienes mas de 15 años")
    else:
        print("No puedes entrar a la biblioteca")
else:
    print("No puedes entrar a la biblioteca")