to_do = ["dirgirnos al Hote",
         "Ir almorzar",
         "Vistar Museo",
         "Volver al Hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))

mix = ["uno",2,3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0] )
print("Segundo elemento", mix[1] )
print("Ultimo elemento", mix[-1] )

print(mix[0:2])#devuelve la poscione de la 0 a alas 2 en cadenas

print(mix)
mix.append(False)
print(mix)#ingresa al final de una lista
mix.insert(1,["a","b"])#ingresa en la posición 1
print(mix)
print(mix.index(["a","b"]))#devuelbe la posción donde se encuentra 

numbers= [1,2,100,5,90,45]
print("Mayor",max(numbers))#devuleve el valor mas gender
print("Menor",min(numbers))#devuleve el valor mas gender

del numbers[-1]#Elimina la ultima posición
print(numbers)
del numbers[:2]#elimina de la posción 0 a 2
print(numbers)
del numbers
print(numbers)
