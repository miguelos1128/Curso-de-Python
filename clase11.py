numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = { "nombre":"Miguel",
               "Apellido":"Osornio",
               "Altura":1.70,
               "Edad":26}
print(information)
del information["Edad"]
print(information)
claves = information.keys()#Obtener Claves
print(claves)
print(type(claves))
values = information.values()#Obtener valores
print(values)
pairs = information.items()#obtener pares
print(pairs)

contacts = {"Miguel":{ 
               "Apellido":"Osornio",
               "Altura":1.70,
               "Edad":26},
               "Mau":{ 
               "Apellido":"Oidor",
               "Altura":1.60,
               "Edad":27}}
print("Contactos",contacts)
print("Contactos",contacts["Mau"])