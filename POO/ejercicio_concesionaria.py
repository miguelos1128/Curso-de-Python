from typing import Any

class Vehiculo:
    #Declarar Clase Vehiculos.
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True
    #Metodo vender vehiculo
    def sell(self):
        if self.disponible:
            self.disponible = False
            print(f">> El Vehiculo {self.marca} ha sido vendido.")
        else:
            print(f" X EL vehiculo {self.marca} no sesta disponible.")

    #Metodo hacer disponible
    def avaliable(self):
        self.disponible = True
        print(f" << El Vehiculo {self.marca} se ha vuelto disponible.")

#CLase Cliente
class Cliente:
    #Delcarar clase
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.vehiculos_comprados = []

    #Metodo comprar vehiculo
    def comprar_vehiculos(self, vehiculo):
        if vehiculo.disponible:
            vehiculo.sell()
            self.vehiculos_comprados.append(vehiculo)
        else:
            print(f" X El Vehiculo {vehiculo.marca} no se encuentra disponible.")

    #Metodo devolber vehiculo   
    def devolber_vehiculos(self, vehiculo):
        if vehiculo in self.vehiculos_comprados:
            vehiculo.avaliable()
            self.vehiculos_comprados.remove(vehiculo)
        else:
            print(f" X El Vehiculo {vehiculo.marca} no se encuentra en la lista de compras.")

     #Mostrar vehiculos del cliente
    def mostrar_vehiculos_cliente(self):
        print(f"Vehiculos del cliente: {self.nombre} ")
        for vehicle in self.vehiculos_comprados:
            print(f"-{vehicle.marca} Año: {vehicle.modelo} $ {vehicle.precio}")       
#Clase Concesionario
class Concesionario:
    #Declarar CLase
    def __init__ (self):
        self.vehiculos = []
        self.clientes = []

    #Metodo Agregar vehiculo
    def add_vehiculo(self, vehicle):
        self.vehiculos.append(vehicle)
        print(f"El Vehiculo {vehicle.marca} ha sido agregado al concesionario.")

    #Metodo Registrar cliente
    def add_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"El Cliente {cliente.nombre} ha sido registrado.")
    #Mostrar vehiculos disponibles
    def mostrar_vehiculos(self):
        print("Vehiculos Disponibles:")
        for vehicle in self.vehiculos:
            if vehicle.disponible:
                print(f"-{vehicle.marca} Año: {vehicle.modelo} $ {vehicle.precio}")

#Crear Vehiculos
auto1 = Vehiculo("Pointer", "2006", 64000)
auto2 = Vehiculo("Polo", "2021", 260000)
auto3 = Vehiculo("Honda", "Civic", 290000)
auto4 = Vehiculo("Toyota", "Corola", 290000)

#Crear Cliente
cliente1 = Cliente("Miguel Angel", "001")
cliente2 = Cliente("Maura Oidor", "002")

#Crear Consecionario
concesionario = Concesionario()
concesionario.add_vehiculo(auto1)
concesionario.add_vehiculo(auto2)
concesionario.add_cliente(cliente1)
concesionario.add_cliente(cliente2)

#Mostrar Vehiculos disponibles
concesionario.mostrar_vehiculos()

#Comprar Vehiculo
cliente1.comprar_vehiculos(auto1)
cliente1.comprar_vehiculos(auto2)

#Mostrar Vehiculos disponibles
concesionario.mostrar_vehiculos()

#Mostrar Vehiculos por cliente
cliente1.mostrar_vehiculos_cliente()
cliente2.mostrar_vehiculos_cliente()

#Devolber Vehiculo
cliente1.devolber_vehiculos(auto1)

#Mostrar Vehiculos disponibles
concesionario.mostrar_vehiculos()